import PySimpleGUI as sg
import datetime
from list import TodoList


class ListGuy:
    def __init__(self, list_assignment: TodoList) -> None:
        self.window: sg.Window
        self.list = list_assignment
        self.data = list_assignment.get_assignments()
        self._initial_window()


    def _initial_window(self) -> None:
        columns_table = [
            'assignment ID',
            'description assignment',
            'date todo'
        ]
        layout_table_assignment = [
            sg.Table(
                values=self.data,
                headings=columns_table,
                key='-TABLE_ASSIGNMENTS-'
            )
        ]
        year_today = datetime.datetime.now().year
        layout_page = [
            [layout_table_assignment],
            [
                sg.Text('enter description for new assignment'),
                sg.Input(key='-description_for_new_assignment-'),
                sg.Text('select day'), sg.DropDown(list(range(1, 32)), key='-day_new_assignment-', default_value=1),
                sg.Text('select month'), sg.DropDown(list(range(1, 13)), key='-month_new_assignment-', default_value=1),
                sg.Text('select year'), sg.DropDown(list(range(year_today, year_today +10)), key='-year_new_assignment-', default_value=year_today),
                sg.Button('add', key='-add_assignment-')
            ],
            [
                sg.Text("enter assignment ID to edit"),
                sg.Input(key='-ID_to_edit-', size=7),
                sg.Text("new description"),
                sg.Input(key='-new_description-'),
                sg.Text('select day'), sg.DropDown(list(range(1, 32)), key='-day_edit_assignment-', default_value=1),
                sg.Text('select month'), sg.DropDown(list(range(1, 13)), key='-month_edit_assignment-', default_value=1),
                sg.Text('select year'), sg.DropDown(list(range(year_today, year_today +10)), key='-year_edit_assignment-', default_value=year_today),
                sg.Button('edit', key='-edit_assignment-'),
            ],
            [
                sg.Text("enter assignment ID to delete"),
                sg.Input(key='-ID_to_delete-', size=7),
                sg.Button('delete', key='-delete_assignment-')
            ],
        ]
        self.window = sg.Window('ToDo List', layout_page)


    def _refresh_data(self) -> None:
        self.data = self.list.get_assignments()
        self.window.close()
        self._initial_window()


    def handel_event(self) -> None:
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED:
                break
            elif (
                event == '-delete_assignment-' and
                values['-ID_to_delete-'].isdigit() and
                self.list.delete_assignment(int(values['-ID_to_delete-']))
            ):
                self._refresh_data()
            elif event == '-add_assignment-':
                description = values['-description_for_new_assignment-']
                self.list.add_assignment(
                    description if description else 'Empty',
                    int(values['-day_new_assignment-']),
                    int(values['-month_new_assignment-']),
                    int(values['-year_new_assignment-'])
                )
                self._refresh_data()
            elif event == '-edit_assignment-':
                description = values['-new_description-']
                if(
                    event == '-edit_assignment-' and
                    values['-ID_to_edit-'].isdigit() and
                    self.list.edit_assignment(
                        int(values['-ID_to_edit-']),
                        description if description else 'Empty',
                        int(values['-day_edit_assignment-']),
                        int(values['-month_edit_assignment-']),
                        int(values['-year_edit_assignment-'])
                    )
                ):
                    self._refresh_data()
            
        self.window.close()
                

