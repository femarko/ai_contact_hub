import httpx


class GroqClient:

    def __init__(
        self,
        api_key: str,
        model: str = "openai/gpt-oss-20b",
        base_url: str = "https://api.groq.com/openai/v1"
    ) -> None:
        self.api_key = api_key
        self.model = model
        self.base_url = base_url
        
    async def analyze(self, text: str):
        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "system",
                    "content": """
                    Analyze user message.
                    Return JSON:
                    {
                      "sentiment": "positive|neutral|negative",
                      "category": "sales|support|other"
                    }
                    """
                },
                {
                    "role": "user",
                    "content": text
                }
            ]
        }
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.post(
                f"{self.base_url}/chat/completions",
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                },
                json=payload
            )
            response.raise_for_status()
            data = response.json()
            return data["choices"][0]["message"]["content"]


