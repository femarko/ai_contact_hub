from enum import StrEnum


class EmailSubject(StrEnum):
    OWNER = "Новое обращение"
    USER = "Мы получили ваше обращение"