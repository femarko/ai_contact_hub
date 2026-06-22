from typing import Callable

from ai_contact_hub.application.interfaces import AiServiceProto

class AIService:
    def __init__(
            self,
            ai_client: AiServiceProto,
            fallback: Callable[..., dict[str, str]],
            ) -> None:
        self.ai_client = ai_client
        self.fallback = fallback

    async def analyze(self, text: str) -> dict[str, str]:
        try:
            result = await self.ai_client.analyze(text)
        except Exception:
            result = self.fallback(text)
        return result
