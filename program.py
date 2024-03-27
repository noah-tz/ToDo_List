from gui import Gui
from list import TodoList
import PySimpleGUI as sg

class Program:
    def __init__(self) -> None:
        self._list_assignment = TodoList()
        self._data = self._list_assignment.get_assignments()
        self._gui = Gui()
        self._gui.initial_window(self._data)
        
    def _refresh_data(self) -> None:
        self._data = self._list_assignment.get_assignments()
        self._gui.refresh_gui(self._data)

    def run(self) -> None:
        while True:
            event, values = self._gui.get_event()
            match event:
                case sg.WINDOW_CLOSED:
                    break
                case '-delete_assignment-':
                    if(
                       values['-ID_to_delete-'].isdigit() and
                        self._list_assignment.delete_assignment(int(values['-ID_to_delete-'])) 
                    ):
                        self._refresh_data()
                        
                case '-add_assignment-':
                    description = values['-description_for_new_assignment-']
                    self._list_assignment.add_assignment(
                        description if description else 'Empty',
                        int(values['-day_new_assignment-']),
                        int(values['-month_new_assignment-']),
                        int(values['-year_new_assignment-'])
                    )
                    self._refresh_data()
                case '-edit_assignment-':
                    description = values['-new_description-']
                    if(
                        event == '-edit_assignment-' and
                        values['-ID_to_edit-'].isdigit() and
                        self._list_assignment.edit_assignment(
                            int(values['-ID_to_edit-']),
                            description if description else 'Empty',
                            int(values['-day_edit_assignment-']),
                            int(values['-month_edit_assignment-']),
                            int(values['-year_edit_assignment-'])
                        )
                    ):
                        self._refresh_data()
      
        self._gui.close_gui()