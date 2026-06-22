from typing import Protocol


class AiServiceProtocol(Protocol):
    async def analyze(self, text: str) -> dict[str, str]: ...
