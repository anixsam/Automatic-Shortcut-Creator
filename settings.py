import json
from operator import le
from os import remove
import tkinter as tk
from tkinter import filedialog


def Add():
    new_drive_letter = drives.get("1.0", "end-1c")

    config_json = open("./config/settings.json","r")
    settings_list = json.load(config_json)
    config_json.close()

    system_drives = settings_list['system_drives']

    if new_drive_letter != "" and new_drive_letter not in system_drives:
        system_drives.append(new_drive_letter)

    settings_list['system_drives'] = system_drives
    settings_list['numberOfSysDrive'] = len(system_drives)
    config_json = open("./config/settings.json","w")
    json.dump(settings_list,config_json)
    config_json.close()

    drives.delete('1.0',"end")

    driveList.delete(0,len(system_drives))

    for i in range(0,len(system_drives)):
        driveList.insert(i+1,system_drives[i])

def removeData(value):
    config_json = open("./config/settings.json","r")
    settings_list = json.load(config_json)
    config_json.close()
    length = settings_list['numberOfSysDrive']

    system_drives = driveList.get(0,length-2)
    settings_list['system_drives'] = system_drives
    settings_list['numberOfSysDrive'] = len(system_drives)

    config_json = open("./config/settings.json","w")
    json.dump(settings_list,config_json)
    config_json.close()

    driveList.delete(value)

def browse():
    folderPath = filedialog.askdirectory()

    config_json = open("./config/settings.json","r")
    settings_list = json.load(config_json)
    config_json.close()

    settings_list['destination_to_shortcut'] = folderPath

    folderPathText.delete('1.0',"end")
    folderPathText.insert('1.0',folderPath)

    config_json = open("./config/settings.json","w")
    json.dump(settings_list,config_json)
    config_json.close()
    

window = tk.Tk()
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.geometry("500x400")
window.resizable(False, False)
window.title("Settings")
window.configure(bg="#5595ed")

settingsPage = tk.Frame(window, bg="#5595ed")
settingsPage.grid(row=0, column=0, sticky='nsew')

canvas_settings = tk.Canvas(
    settingsPage,
    bg="#5595ed",
    height=500,
    width=400,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas_settings.place(x=0, y=0)

canvas_settings.create_text(
    120, 
    20, 
    text="Select the System Drives", 
    fill="#ffffff",
    font=("None", int(15.0)),
    )

drives = tk.Text(window,height = 1, width = 2)
drives.place(x=240, y=10)

addButton = tk.Button(settingsPage,text="Add",command= lambda: Add(),height=1,width=5)
addButton.place(x=270, y=9)

driveList = tk.Listbox(height=4,width=10)
driveList.place(x=330, y=9)

removeButton = tk.Button(window, text = "Delete", command = lambda:removeData(tk.ANCHOR),height=1,width=5) 
removeButton.place(x=270,y=50) 

config_json = open("./config/settings.json","r")
settings_list = json.load(config_json)
config_json.close()

canvas_settings.create_text(
    165, 
    100, 
    text="Select the target folder for shortcut", 
    fill="#ffffff",
    font=("None", int(15.0)),
    )

browseButton = tk.Button(settingsPage,text="Browse",command= lambda: browse(),height=1,width=6)
browseButton.place(x=15, y=120)

folderPathText = tk.Text(window,height = 1, width = 45)
folderPathText.place(x=80, y=122)

system_drives = settings_list['system_drives']

for i in range(0,len(system_drives)):
        driveList.insert(i+1,system_drives[i])

while True:
    config_json = open("./config/settings.json","r")
    settings = json.load(config_json)
    config_json.close() 

    window.update()




window.mainloop()
