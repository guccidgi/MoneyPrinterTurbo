import os
import shutil
import socket

import toml
from loguru import logger

# 導入環境變數配置模組
from app.config.env_config import get_env_config

root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
config_file = f"{root_dir}/config.toml"

# 檢查是否在 Zeabur 或其他雲端環境中運行
is_cloud_env = os.environ.get("ZEABUR") == "true" or os.environ.get("MPT_USE_ENV_CONFIG") == "true"


def load_config():
    # 如果在雲端環境中運行，優先使用環境變數配置
    if is_cloud_env:
        logger.info("Running in cloud environment, loading config from environment variables")
        return get_env_config()
    
    # 否則從 config.toml 檔案讀取配置
    # fix: IsADirectoryError: [Errno 21] Is a directory: '/MoneyPrinterTurbo/config.toml'
    if os.path.isdir(config_file):
        shutil.rmtree(config_file)

    if not os.path.isfile(config_file):
        example_file = f"{root_dir}/config.example.toml"
        if os.path.isfile(example_file):
            shutil.copyfile(example_file, config_file)
            logger.info("copy config.example.toml to config.toml")

    logger.info(f"load config from file: {config_file}")

    try:
        _config_ = toml.load(config_file)
    except Exception as e:
        logger.warning(f"load config failed: {str(e)}, try to load as utf-8-sig")
        with open(config_file, mode="r", encoding="utf-8-sig") as fp:
            _cfg_content = fp.read()
            _config_ = toml.loads(_cfg_content)
    return _config_


def save_config():
    # 如果在雲端環境中運行，不允許保存配置到檔案
    if is_cloud_env:
        logger.warning("Running in cloud environment, cannot save config to file")
        return
    
    with open(config_file, "w", encoding="utf-8") as f:
        _cfg["app"] = app
        _cfg["azure"] = azure
        _cfg["siliconflow"] = siliconflow
        _cfg["ui"] = ui
        f.write(toml.dumps(_cfg))


_cfg = load_config()
app = _cfg.get("app", {})
whisper = _cfg.get("whisper", {})
proxy = _cfg.get("proxy", {})
azure = _cfg.get("azure", {})
siliconflow = _cfg.get("siliconflow", {})
ui = _cfg.get(
    "ui",
    {
        "hide_log": False,
    },
)

hostname = socket.gethostname()

log_level = _cfg.get("log_level", "DEBUG")
listen_host = _cfg.get("listen_host", "0.0.0.0")
listen_port = _cfg.get("listen_port", 8080)
project_name = _cfg.get("project_name", "MoneyPrinterTurbo")
project_description = _cfg.get(
    "project_description",
    "<a href='https://github.com/harry0703/MoneyPrinterTurbo'>https://github.com/harry0703/MoneyPrinterTurbo</a>",
)
project_version = _cfg.get("project_version", "1.2.6")
reload_debug = False

imagemagick_path = app.get("imagemagick_path", "")
if imagemagick_path and os.path.isfile(imagemagick_path):
    os.environ["IMAGEMAGICK_BINARY"] = imagemagick_path

ffmpeg_path = app.get("ffmpeg_path", "")
if ffmpeg_path and os.path.isfile(ffmpeg_path):
    os.environ["IMAGEIO_FFMPEG_EXE"] = ffmpeg_path

logger.info(f"{project_name} v{project_version}")
