import functions
import FreeSimpleGUI as sg
import os
import sys

def resource_path(relative_path):
    """Garante que os arquivos funcionem tanto no .py quanto no .exe"""
    try:
        base_path = sys._MEIPASS  # usado pelo PyInstaller
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# caminho do arquivo de tarefas
TODO_FILE = resource_path("todos.txt")

# cria o arquivo caso não exista
if not os.path.exists(TODO_FILE):
    with open(TODO_FILE, "w") as file:
        pass

sg.theme("DarkTeal12")

label = sg.Text("Type in a to-do", text_color='white')
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button(size=10, image_source=resource_path("add.png"), mouseover_colors='grey',
                       tooltip="Add Todo", key='Add')
list_box = sg.Listbox(values=functions.get_todos(TODO_FILE), key='todos',
                      enable_events=True, size=(45, 10))
edit_button = sg.Button(size=10, image_source=resource_path("edit.png"), mouseover_colors='grey',
                        tooltip="Edit Now", key='Edit')
complete_button = sg.Button(size=10, image_source=resource_path("complete.png"), mouseover_colors='grey',
                            tooltip="Go Complete", key='Complete')
exit_button = sg.Button("Exit", size=10)

window = sg.Window('My To-Do App',
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 12))

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Exit":
        break

    match event:
        case "Add":
            todos = functions.get_todos(TODO_FILE)
            new_todo_item = values['todo'].strip()
            if new_todo_item:
                todos.append(new_todo_item)
                functions.write_todos(todos, TODO_FILE)
                window['todos'].update(values=todos)
                window['todo'].update('')

        case "Edit":
            try:
                if values['todos']:
                    todo_to_edit = values['todos'][0]
                    new_todo_item = values['todo'].strip()
                    if new_todo_item:
                        todos = functions.get_todos(TODO_FILE)
                        index = todos.index(todo_to_edit)
                        todos[index] = new_todo_item
                        functions.write_todos(todos, TODO_FILE)
                        window['todos'].update(values=todos)
                else:
                    sg.popup("Please select an item first.", font=("Helvetica", 12))
            except (IndexError, KeyError):
                sg.popup("Please select an item first.", font=("Helvetica", 12))

        case "Complete":
            try:
                if values['todos']:
                    todo_to_complete = values['todos'][0]
                    todos = functions.get_todos(TODO_FILE)
                    todos.remove(todo_to_complete)
                    functions.write_todos(todos, TODO_FILE)
                    window['todos'].update(values=todos)
                    window['todo'].update(value='')
                else:
                    sg.popup("Please select an item first.", font=("Helvetica", 12))
            except (IndexError, KeyError):
                sg.popup("Please select an item first.", font=("Helvetica", 12))

        case 'todos':
            if values['todos']:
                window['todo'].update(value=values['todos'][0])

window.close()
