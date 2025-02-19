def get_todos():
    with open("todos.txt",'r') as file:
        result=file.readlines()
    return result

def write_todos(todos):
    with open("todos.txt",'w') as file:
        result=file.writelines(todos)
