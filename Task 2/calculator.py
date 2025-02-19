import FreeSimpleGUI as sg

sg.theme("Black")
add=sg.Button("+",size=(7,1))
subt=sg.Button("-",size=(7,1))
mult=sg.Button("*",size=(7,1))
div=sg.Button("/",size=(7,1))
label1=sg.Text("Enter number 1:")
num1=sg.InputText(tooltip="Enter the number",key="num1")
label2=sg.Text("Enter number 2:")
num2=sg.InputText(tooltip="Enter the number",key="num2")
output_label=sg.Text("",key="output")
ac=sg.Button("AC",size=(7,1))
close=sg.Button("Close")
window=sg.Window("Simple Calculator",[[label1,num1],[label2,num2],[add,subt,mult,div,ac,output_label],[close]])

while True:
    event,value=window.read()
    match event:
        case "+":
            result=int(value['num1'])+int(value['num2'])
            window['output'].update(value=f"Result:{result}",text_color="white")
        case "-":
            result = int(value['num1'])-int(value['num2'])
            window['output'].update(value=f"Result:{result}", text_color="white")
        case "*":
            result = int(value['num1'])*int(value['num2'])
            window['output'].update(value=f"Result:{result}", text_color="white")
        case "/":
            result = int(value['num1'])/int(value['num2'])
            window['output'].update(value=f"Result:{result}", text_color="white")
        case "AC":
            window['num1'].update(value="")
            window['num2'].update(value="")
            window['output'].update(value="")
        case "Close":
            break
        case sg.WIN_CLOSED:
            break
window.close()
