from assignment import Assignment


class TodoList:
    def __init__(self,) -> None:
        self.assignments: dict[int ,Assignment] = {}
        for i in range(1, 10):
            self.add_assignment(f'Do something {i}', 20+i, 3, 2020+i)

    def add_assignment(self, description: str, day: int, month: int, year: int) -> None:
        new_assignment = Assignment(description ,day, month, year)
        self.assignments[Assignment.assignment_ID] = new_assignment
        Assignment.assignment_ID +=1

    def edit_assignment(self, ID: int, new_description: str, new_day: int, new_month: int, new_year: int) -> bool:
        if ID in self.assignments:
            self.assignments[ID] = Assignment(new_description, new_day, new_month, new_year)
            return True
        return False

    def delete_assignment(self, ID: int) -> bool:
        return bool(self.assignments.pop(ID, None))
        
    def get_assignments(self) -> list:
        assignments_list = []
        for assignment_id, assignment in self.assignments.items():
            assignment_info = [
                assignment_id,
                assignment.description,
                assignment.date.strftime("%d-%m-%y")
            ]
            assignments_list.append(assignment_info)
        return assignments_list
