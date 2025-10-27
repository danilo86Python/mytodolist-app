import functions
import time

now = time.strftime("%b %d %Y %H %M %S")
print('It is', now)

while True:
    user_action = input('Type add, show, edit, complete, or exit: ')
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:].strip()
        if not todo:  # Check if input is empty after "add"
            print("Please enter a todo item after 'add'")
            continue

        todos = functions.get_todos()
        todos.append(todo + '\n')
        functions.write_todos(todos)
        print(f"Added: {todo}")

    elif user_action.startswith('show'):
        todos = functions.get_todos()
        if not todos:  # Check if list is empty
            print("No todos found. Add some todos first!")
            continue

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f'{index + 1}-{item}'
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()
            if not todos:  # check if list is empty
                print("No todos to edit. Add some todos first!")
                continue

            if number < 0 or number >= len(todos):
                print("Invalid todo number.")
                continue

            new_todo = input('Enter new todo: ')
            todos[number] = new_todo
            functions.write_todos(todos)
            print(f"Todo #{number + 1} updated.")

        except ValueError:
            print('Please enter a valid number after "edit".')
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            number = number - 1

            todos = functions.get_todos()
            if not todos:  # Check if list is empty
                print("No todos to complete. Add some todos first!")
                continue

            if number < 0 or number >= len(todos):
                print("Invalid todo number.")
                continue

            todo_to_remove = todos[number].strip('\n')
            todos.pop(number)
            functions.write_todos(todos)
            message = f'Todo "{todo_to_remove}" was removed from the list.'
            print(message)

        except ValueError:
            print('Please enter a valid number after "complete".')
            continue
        except IndexError:
            print('There is no item with that number.')
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print('Command is not valid. Please use: add, show, edit, complete, or exit')

print('Bye')