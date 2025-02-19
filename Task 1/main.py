import FreeSimpleGUI as sg
import functions
import time

sg.theme("Black")
label_time=sg.Text("",key='clock')
add=sg.Button("Add")
edit=sg.Button("Edit")
done=sg.Button("Done")
ext=sg.Button("Exit")
input_box=sg.InputText(tooltip="Enter a Todo",key="todo")
list_box=sg.Listbox(values=functions.get_todos(),size=[45,10],key='list')
window=sg.Window("TO DO List",[[label_time],[input_box,add],[list_box,done,edit],[ext]],font=('Times New Roman',15))
while True:
    event,value=window.read(timeout=100)
    window['clock'].update(value=time.strftime("%b %d,%Y"))
    match event:
        case 'Add':
            todos=functions.get_todos()
            new_todo=value['todo']+'\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['list'].update(values=todos)
        case 'Edit':
            try:
                todos=functions.get_todos()
                todo_to_edit=value['list'][0]
                new_todo=value['todo']+'\n'
                index=todos.index(todo_to_edit)
                todos[index]=new_todo
                functions.write_todos(todos)
                window['list'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first",font=('Times New Roman',20))
        case 'Done':
            try:
                todos = functions.get_todos()
                todo_to_remove=value['list'][0]
                index=todos.index(todo_to_remove)
                todos.remove(todos[index])
                functions.write_todos(todos)
                window['list'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first",font=('Times New Roman',20))
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break

window.close()
