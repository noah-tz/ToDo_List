import PySimpleGUI as sg
import datetime


class Gui:
    def __init__(self) -> None:
        self._window: sg.Window


    def initial_window(self, data) -> None:
        columns_table = [
            'assignment ID',
            'description assignment',
            'date todo'
        ]
        layout_table_assignment = [
            sg.Table(
                values=data,
                headings=columns_table,
                key='-TABLE_ASSIGNMENTS-',
                size=(20, 20),
            )
        ]
        year_today = datetime.datetime.now().year
        layout_page = [
            [layout_table_assignment],
            [sg.HSep(color='black')],
            [
                [sg.Text('enter description for new assignment')],
                [sg.Input(key='-description_for_new_assignment-')],
                [sg.Text('select day'), sg.DropDown(list(range(1, 32)), key='-day_new_assignment-', default_value=1),
                sg.Text('select month'), sg.DropDown(list(range(1, 13)), key='-month_new_assignment-', default_value=1),
                sg.Text('select year'), sg.DropDown(list(range(year_today, year_today +10)), key='-year_new_assignment-', default_value=year_today),
                sg.Button('add', key='-add_assignment-')]
            ],
            [sg.HSep(color='black')],
            [
                [sg.Text("enter assignment ID to edit"),
                sg.Input(key='-ID_to_edit-', size=7)],
                [sg.Text("new description")],
                [sg.Input(key='-new_description-')],
                [sg.Text('select day'), sg.DropDown(list(range(1, 32)), key='-day_edit_assignment-', default_value=1),
                sg.Text('select month'), sg.DropDown(list(range(1, 13)), key='-month_edit_assignment-', default_value=1),
                sg.Text('select year'), sg.DropDown(list(range(year_today, year_today +10)), key='-year_edit_assignment-', default_value=year_today),
                sg.Button('edit', key='-edit_assignment-')]
            ],
            [sg.HSep(color='black')],
            [
                sg.Text("enter assignment ID to delete"),
                sg.Input(key='-ID_to_delete-', size=7),
                sg.Button('delete', key='-delete_assignment-')
            ],
        ]
        self._window = sg.Window('ToDo List', layout_page, size=(500, 600))


    def refresh_gui(self, data) -> None:
        self._window.close()
        self.initial_window(data)

    def get_event(self) -> tuple[str, dict]:
        return self._window.read()
    
    def close_gui(self) -> None:
        self._window.close()


                

