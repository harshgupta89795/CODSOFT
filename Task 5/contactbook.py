import FreeSimpleGUI as sg
import pandas as pd

df=pd.read_csv("contact.csv").sort_values(by="Name", ascending=True)
df=df.sort_values(by="Name",ascending=True)

window1 = sg.Window("Contact Book", [
    [sg.InputText(tooltip="Enter Name or Phone Number", key="srch"),sg.Button("Search")],
    [sg.Button("Add Contact")],
    [sg.Button("View")],
    [sg.Button("Exit")]
])
while True:
    event,value=window1.read()
    if event in (sg.WIN_CLOSED,'Exit'):
        break
    if event=='Add Contact':
        window2 = sg.Window("Add a Contact", [
            [sg.Text("Enter the Name:"),sg.InputText(key="name")],
            [sg.Text("Enter the Phone Number:"),sg.InputText(key="phone")],
            [sg.Text("Enter the Email Address:"),sg.InputText(key="email")],
            [sg.Text("Enter the Address:"),sg.InputText(key="address")],
            [sg.Button("Save"),sg.Button("Cancel")]
        ])
        e,V=window2.read()
        if e=='Save':
            new_entry=pd.DataFrame([{
                "Name":V['name'],
                "Email":V['email'],
                "Phone":V['phone'],
                "Address":V['address']
            }])
            df=pd.concat([df, new_entry],ignore_index=True)
            df.to_csv("contact.csv",index=False)
            sg.popup("New contact added successfully!")
        window2.close()
    elif event=='Search':
        found=False
        for index,val in df.iterrows():
            if value['srch'] in (val['Name'],str(val['Phone'])):
                found=True
                window3 = sg.Window("Contact Details", [
                    [sg.Text(f"Name:{val['Name']}")],
                    [sg.Text(f"Email:{val['Email']}")],
                    [sg.Text(f"Phone:{val['Phone']}")],
                    [sg.Text(f"Address:{val['Address']}")],
                    [sg.Button("Update"),sg.Button("Delete"),sg.Button("Back")]
                ])
                eve,value1=window3.read()
                if eve=='Delete':
                    df=df[df['Name']!=val['Name']]
                    df.to_csv("contact.csv",index=False)
                    sg.popup(f"{val['Name']} Deleted")
                elif eve=='Update':
                    window4=sg.Window("Update Details",[
                        [sg.Text("Edit the Name:"),sg.Input(default_text=val['Name'],key="name")],
                        [sg.Text("Edit the Phone Number:"),sg.Input(default_text=val['Phone'],key="phone")],
                        [sg.Text("Edit the Email Address:"),sg.Input(default_text=val['Email'],key="email")],
                        [sg.Text("Edit the Address:"),sg.Input(default_text=val['Address'],key="address")],
                        [sg.Button("Save Changes"),sg.Button("Cancel")]
                    ])
                    e,v=window4.read()
                    if e=='Save Changes':
                        for ind in df.index:
                            if df.loc[ind,'Name']==val['Name']:
                                df.at[ind,'Name']=v['name']
                                df.at[ind,'Email']=v['email']
                                df.at[ind,'Phone']=str(v['phone'])
                                df.at[ind,'Address']=v['address']
                                df.to_csv("contact.csv",index=False)
                                sg.popup("Changes saved successfully!")
                                break
                    window4.close()
                window3.close()
        if not found:
            sg.popup("Contact not Found!")
    elif event=='View':
        headings=list(df.columns)
        data=df.values.tolist()
        window5=sg.Window("Contact Display", [
            [sg.Text("Contacts")],
            [sg.Table(values=data, headings=headings, num_rows=min(20, len(data)))],
            [sg.Button("Close")]
        ])
        if window5.read()[0]=='Close':
            window5.close()
window1.close()