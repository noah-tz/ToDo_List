from main_guy import ListGuy
from list import TodoList


def main():
    list_assignment = TodoList()
    main_gui = ListGuy(list_assignment)
    main_gui.read()

if __name__ == '__main__':
    main()