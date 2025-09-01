import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 12))

while True:
    event, values = window.read()  # This must be INSIDE the loop
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo_item = values['todo'] + "\n"  # Changed variable name
            todos.append(new_todo_item)
            functions.write_todos(todos)
            # Clear the input box after adding
            window['todo'].update('')
        case sg.WIN_CLOSED:  # Handle window closing
            break

window.close()