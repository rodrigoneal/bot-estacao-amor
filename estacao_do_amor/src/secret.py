def params_bot(config: dict[str, str]) -> dict[str, str]:
    params = [
        "api_id",
        "api_hash",
        "bot_token",
    ]
    return {param: config[param.upper()] for param in params}
