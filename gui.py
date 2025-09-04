import functions
import FreeSimpleGUI as sg
import time
sg.theme("DarkTeal12")
clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do", text_color='white')
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add", size=10)
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit", size=10)
complete_button = sg.Button("Complete", size=10)
exit_button = sg.Button("Exit", size=10)

window = sg.Window('My To-Do App',
                   layout=[[clock],
                            [label],
                            [input_box, add_button],
                            [list_box, edit_button, complete_button],
                            [exit_button]],
                   font=('Helvetica', 12))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d %Y %H %M %S"), text_color='yellow')
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo_item = values['todo'] + "\n"  # Changed variable name
            todos.append(new_todo_item)
            functions.write_todos(todos)
            window['todo'].update('')

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo_item = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo_item
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 12))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 12))
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:  # Handle window closing
            break

window.close()