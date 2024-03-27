from datetime import date


class Task:
    task_ID = 1
    def __init__(self, description: str, day: int, month: int, year: int) -> None:
        self.description = description
        self.date = date(year, month, day)
