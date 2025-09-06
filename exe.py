import sys

def get_base():
    if sys.platform == "win32":
        return "Win32GUI"
    return None

def get_setup_config():
    return {
        "name": "MyToDoApp",
        "version": "1.0",
        "description": "App de tarefas",
        "executables": [
            {"script": "gui.py", "base": get_base()}  # corrigido para gui.py
        ],
        "options": {
            "build_exe": {
                "include_files": [
                    "add.png",
                    "edit.png",
                    "complete.png",
                    "todos.txt",
                ]
            }
        }
    }
