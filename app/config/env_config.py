import os
import json
from typing import Dict, Any, Optional


def get_env_var(key: str, default: Any = None) -> Any:
    """從環境變數獲取值，支援 JSON 格式的複雜配置"""
    value = os.environ.get(key)
    if value is None:
        return default
    
    # 嘗試解析 JSON 格式的值
    try:
        return json.loads(value)
    except json.JSONDecodeError:
        return value


def get_env_config() -> Dict[str, Any]:
    """從環境變數構建配置字典"""
    config = {
        "log_level": get_env_var("MPT_LOG_LEVEL", "DEBUG"),
        "listen_host": get_env_var("MPT_LISTEN_HOST", "0.0.0.0"),
        "listen_port": int(get_env_var("MPT_LISTEN_PORT", "8080")),
        "project_name": get_env_var("MPT_PROJECT_NAME", "MoneyPrinterTurbo"),
        "project_version": get_env_var("MPT_PROJECT_VERSION", "1.2.6"),
        "reload_debug": get_env_var("MPT_RELOAD_DEBUG", "false").lower() == "true",
        "app": {
            "video_source": get_env_var("MPT_VIDEO_SOURCE", "pexels"),
            "hide_config": get_env_var("MPT_HIDE_CONFIG", "false").lower() == "true",
            "pexels_api_keys": get_env_var("MPT_PEXELS_API_KEYS", []),
            "pixabay_api_keys": get_env_var("MPT_PIXABAY_API_KEYS", []),
            "llm_provider": get_env_var("MPT_LLM_PROVIDER", "openai"),
            "pollinations_api_key": get_env_var("MPT_POLLINATIONS_API_KEY", ""),
            "pollinations_base_url": get_env_var("MPT_POLLINATIONS_BASE_URL", "https://pollinations.ai/api/v1"),
            "pollinations_model_name": get_env_var("MPT_POLLINATIONS_MODEL_NAME", "openai-fast"),
            "ollama_base_url": get_env_var("MPT_OLLAMA_BASE_URL", ""),
            "ollama_model_name": get_env_var("MPT_OLLAMA_MODEL_NAME", ""),
            "openai_api_key": get_env_var("MPT_OPENAI_API_KEY", ""),
            "openai_base_url": get_env_var("MPT_OPENAI_BASE_URL", ""),
            "openai_model_name": get_env_var("MPT_OPENAI_MODEL_NAME", "gpt-4o-mini"),
            "moonshot_api_key": get_env_var("MPT_MOONSHOT_API_KEY", ""),
            "moonshot_base_url": get_env_var("MPT_MOONSHOT_BASE_URL", "https://api.moonshot.cn/v1"),
            "moonshot_model_name": get_env_var("MPT_MOONSHOT_MODEL_NAME", "moonshot-v1-8k"),
            "oneapi_api_key": get_env_var("MPT_ONEAPI_API_KEY", ""),
            "oneapi_base_url": get_env_var("MPT_ONEAPI_BASE_URL", ""),
            "oneapi_model_name": get_env_var("MPT_ONEAPI_MODEL_NAME", ""),
            "g4f_model_name": get_env_var("MPT_G4F_MODEL_NAME", "gpt-3.5-turbo"),
            "azure_api_key": get_env_var("MPT_AZURE_API_KEY", ""),
            "azure_base_url": get_env_var("MPT_AZURE_BASE_URL", ""),
            "azure_model_name": get_env_var("MPT_AZURE_MODEL_NAME", "gpt-35-turbo"),
            "azure_api_version": get_env_var("MPT_AZURE_API_VERSION", "2024-02-15-preview"),
            "gemini_api_key": get_env_var("MPT_GEMINI_API_KEY", ""),
            "gemini_model_name": get_env_var("MPT_GEMINI_MODEL_NAME", "gemini-1.0-pro"),
            "qwen_api_key": get_env_var("MPT_QWEN_API_KEY", ""),
            "qwen_model_name": get_env_var("MPT_QWEN_MODEL_NAME", "qwen-max"),
            "deepseek_api_key": get_env_var("MPT_DEEPSEEK_API_KEY", ""),
            "deepseek_base_url": get_env_var("MPT_DEEPSEEK_BASE_URL", "https://api.deepseek.com"),
            "deepseek_model_name": get_env_var("MPT_DEEPSEEK_MODEL_NAME", "deepseek-chat"),
            "subtitle_provider": get_env_var("MPT_SUBTITLE_PROVIDER", ""),
            "imagemagick_path": get_env_var("MPT_IMAGEMAGICK_PATH", ""),
            "ffmpeg_path": get_env_var("MPT_FFMPEG_PATH", ""),
            "endpoint": get_env_var("MPT_ENDPOINT", ""),
            "material_directory": get_env_var("MPT_MATERIAL_DIRECTORY", ""),
            "enable_redis": get_env_var("MPT_ENABLE_REDIS", "false").lower() == "true",
            "redis_host": get_env_var("MPT_REDIS_HOST", "localhost"),
            "redis_port": int(get_env_var("MPT_REDIS_PORT", "6379")),
            "redis_db": int(get_env_var("MPT_REDIS_DB", "0")),
            "redis_password": get_env_var("MPT_REDIS_PASSWORD", ""),
            "max_concurrent_tasks": int(get_env_var("MPT_MAX_CONCURRENT_TASKS", "5")),
        },
        "whisper": {
            "model_size": get_env_var("MPT_WHISPER_MODEL_SIZE", "large-v3"),
            "device": get_env_var("MPT_WHISPER_DEVICE", "CPU"),
            "compute_type": get_env_var("MPT_WHISPER_COMPUTE_TYPE", "int8"),
        },
        "proxy": {
            "http": get_env_var("MPT_PROXY_HTTP", ""),
            "https": get_env_var("MPT_PROXY_HTTPS", ""),
        },
        "azure": {
            "speech_api_key": get_env_var("MPT_AZURE_SPEECH_API_KEY", ""),
            "speech_region": get_env_var("MPT_AZURE_SPEECH_REGION", ""),
        },
        "ui": {
            "hide_log": get_env_var("MPT_UI_HIDE_LOG", "false").lower() == "true",
        },
    }
    
    return config
