import PySimpleGUI as sg
import datetime


class Gui:
    def __init__(self) -> None:
        self._window: sg.Window


    def initial_window(self, data) -> None:
        columns_table = [
            'task ID',
            'description task',
            'date todo'
        ]
        layout_table_task = [
            sg.Table(
                values=data,
                headings=columns_table,
                key='-TABLE_ASSIGNMENTS-',
                size=(20, 13),
            )
        ]
        year_today = datetime.datetime.now().year
        layout_page = [
            [layout_table_task],
            [sg.HSep(color='black', pad=20)],
            [
                [sg.Text('enter description for new task')],
                [sg.Input(key='-description_for_new_task-')],
                [sg.Text('select day'), sg.DropDown(list(range(1, 32)), key='-day_new_task-', default_value=1),
                sg.Text('select month'), sg.DropDown(list(range(1, 13)), key='-month_new_task-', default_value=1),
                sg.Text('select year'), sg.DropDown(list(range(year_today, year_today +10)), key='-year_new_task-', default_value=year_today),
                sg.Button('add', key='-add_task-')]
            ],
            [sg.HSep(color='black', pad=20)],
            [
                [sg.Text("enter task ID to edit"),
                sg.Input(key='-ID_to_edit-', size=7)],
                [sg.Text("new description")],
                [sg.Input(key='-new_description-')],
                [sg.Text('select day'), sg.DropDown(list(range(1, 32)), key='-day_edit_task-', default_value=1),
                sg.Text('select month'), sg.DropDown(list(range(1, 13)), key='-month_edit_task-', default_value=1),
                sg.Text('select year'), sg.DropDown(list(range(year_today, year_today +10)), key='-year_edit_task-', default_value=year_today),
                sg.Button('edit', key='-edit_task-')]
            ],
            [sg.HSep(color='black', pad=20)],
            [
                sg.Text("enter task ID to delete"),
                sg.Input(key='-ID_to_delete-', size=7),
                sg.Button('delete', key='-delete_task-')
            ],
        ]
        self._window = sg.Window('ToDo List', layout_page, size=(550, 600))


    def refresh_gui(self, data) -> None:
        self._window.close()
        self.initial_window(data)

    def get_event(self) -> tuple[str, dict]:
        return self._window.read()
    
    def close_gui(self) -> None:
        self._window.close()


                

