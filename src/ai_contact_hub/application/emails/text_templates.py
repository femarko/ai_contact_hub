def owner_notification(
    name: str,
    email: str,
    message: str,
    context: str | None = None
) -> str:
    return f"""
Новое обращение

Имя:
{name}

Email:
{email}

Сообщение:
{message}

Примечания:
{context if context is not None else ""}
"""


def user_confirmation(
    name: str,
    message: str
) -> str:

    return f"""
Здравствуйте, {name}!

Мы получили ваше обращение:

``{message}``

Спасибо!
"""
