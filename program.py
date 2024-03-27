from gui import Gui
from list import TodoList
import PySimpleGUI as sg

class Program:
    def __init__(self) -> None:
        self._list_task = TodoList()
        self._data = self._list_task.get_tasks()
        self._gui = Gui()
        self._gui.initial_window(self._data)
        
    def _refresh_data(self) -> None:
        self._data = self._list_task.get_tasks()
        self._gui.refresh_gui(self._data)

    def run(self) -> None:
        while True:
            event, values = self._gui.get_event()
            match event:
                case sg.WINDOW_CLOSED:
                    break
                case '-delete_task-':
                    if(
                       values['-ID_to_delete-'].isdigit() and
                        self._list_task.delete_task(int(values['-ID_to_delete-'])) 
                    ):
                        self._refresh_data()
                        
                case '-add_task-':
                    description = values['-description_for_new_task-']
                    self._list_task.add_task(
                        description if description else 'Empty',
                        int(values['-day_new_task-']),
                        int(values['-month_new_task-']),
                        int(values['-year_new_task-'])
                    )
                    self._refresh_data()
                case '-edit_task-':
                    description = values['-new_description-']
                    if(
                        event == '-edit_task-' and
                        values['-ID_to_edit-'].isdigit() and
                        self._list_task.edit_task(
                            int(values['-ID_to_edit-']),
                            description if description else 'Empty',
                            int(values['-day_edit_task-']),
                            int(values['-month_edit_task-']),
                            int(values['-year_edit_task-'])
                        )
                    ):
                        self._refresh_data()
      
        self._gui.close_gui()