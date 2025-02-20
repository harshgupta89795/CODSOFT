import FreeSimpleGUI as sg
import random

sg.theme("Black")
outcome=['Rock','Paper','Scissor']

layout = [
    [sg.Text("Computer",size=(10, 1)),sg.Push(),sg.Text("User",size=(10, 1),justification="right")],
    [sg.Push(),sg.InputText(tooltip="Enter your move",key="user",size=(10, 1),justification="left")],
    [sg.Text("",key="c_move",size=(10, 1)),sg.Push(),sg.Text("",key="u_move",size=(10, 1),justification="right")],
    [sg.Push(), sg.Button("Play"), sg.Push()]
]
window=sg.Window("Rock-Paper-Scissors Game",layout,size=(400,150),font=("Times New Roman", 16))
while True:
    event,value=window.read()
    match event:
        case sg.WIN_CLOSED:
            break
        case 'Play':
            result=random.choice(outcome)
            user_choice=value['user']
            window['c_move'].update(value=result)
            window['u_move'].update(value=user_choice)
            if user_choice not in outcome:
                sg.popup("Invalid Move!",font=("Times New Roman", 16))
            elif (result == 'Rock' and user_choice == 'Paper') or\
                 (result == 'Paper' and user_choice == 'Scissor') or\
                 (result == 'Scissor' and user_choice == 'Rock'):
                sg.popup("User Wins!",font=("Arial", 16))
            elif result==user_choice:
                sg.popup("It's a Tie!",font=("Times New Roman", 16))
            else:
                sg.popup("Computer Wins!",font=("Times New Roman", 16))

window.close()

