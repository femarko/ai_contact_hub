from dataclasses import dataclass
from typing import Callable, Protocol


class EmailClient(Protocol):
    async def send(
        self,
        to: str,
        subject: str,
        body: str,
    ) -> None: ...


@dataclass(frozen=True)
class EmailTemplate:
    subject: str
    text_builder: Callable[..., str]
