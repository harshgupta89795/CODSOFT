import FreeSimpleGUI as sg
import random
import string

sg.theme("Black")
label_1=sg.Text("Enter the Length of the Password:")
length_box=sg.InputText(tooltip="Enter length",key="length")
complexity=sg.Text("""Length should be >=8
At least one UpperCase Letter
At least one LowerCase Letter
At least one number
At least one special character""")

generate=sg.Button("Generate")
label0=sg.Text("Password:")
result=sg.Text("",key="password")
num_list=['0','1','2','3','4','5','6','7','8','9']

window=sg.Window("Password Generator",[[label_1,length_box],[complexity],[generate,label0,result]])
while True:
    event,value=window.read()
    match event:
        case sg.WIN_CLOSED:
            break
        case 'Generate':
            length=int(value['length'])
            if length>=8:
                num_count=int(random.randint(1,length))
                random_num = "".join(random.sample(num_list,num_count))
                length1=int(length-num_count)
                if length1 > 1:
                    special_count=int(random.randint(1,length1))
                else:
                    special_count=1
                random_special="".join(random.choices(string.punctuation,k=special_count))
                length2=int(length1-special_count)
                if length2 > 1:
                    lower_count=int(random.randint(1,length2))
                else:
                    lower_count=1
                random_lcase_letter ="".join(random.choices(string.ascii_lowercase,k=lower_count))
                length3=int(length2-lower_count)
                upper_count=length3
                random_uppercase_letter="".join(random.choices(string.ascii_uppercase,k=upper_count))
                random_num=random_num+random_special+random_lcase_letter+random_uppercase_letter
                random_num=list(random_num)
                random.shuffle(random_num)
                sample="".join(random_num)
                window['password'].update(value=sample)
            else:
                sg.popup("Length should be minimum 8")
                window['length'].update(value="")
                window['password'].update(value="")

window.close()