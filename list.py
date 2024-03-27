from task import Task


class TodoList:
    def __init__(self,) -> None:
        self.tasks: dict[int ,Task] = {}
        for i in range(1, 10):
            self.add_task(f'Do something {i}', 20+i, 3, 2020+i)

    def add_task(self, description: str, day: int, month: int, year: int) -> None:
        new_task = Task(description ,day, month, year)
        self.tasks[Task.task_ID] = new_task
        Task.task_ID +=1

    def edit_task(self, ID: int, new_description: str, new_day: int, new_month: int, new_year: int) -> bool:
        if ID in self.tasks:
            self.tasks[ID] = Task(new_description, new_day, new_month, new_year)
            return True
        return False

    def delete_task(self, ID: int) -> bool:
        return bool(self.tasks.pop(ID, None))
        
    def get_tasks(self) -> list:
        tasks_list = []
        for task_id, task in self.tasks.items():
            task_info = [
                task_id,
                task.description,
                task.date.strftime("%d-%m-%y")
            ]
            tasks_list.append(task_info)
        return tasks_list
