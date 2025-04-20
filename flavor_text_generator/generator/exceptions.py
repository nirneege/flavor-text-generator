class ConnectionError(Exception):
    """LLMサービスへの接続エラー"""

    pass


class RuntimeError(Exception):
    """LLMサービスの実行時エラー"""

    pass


class ValueError(Exception):
    """LLMサービスからの無効な値エラー"""

    pass
