from main_guy import Communicator
from list import TodoList


def main():
    list_assignment = TodoList()
    main_gui = Communicator(list_assignment)
    main_gui.handel_event()

if __name__ == '__main__':
    main()