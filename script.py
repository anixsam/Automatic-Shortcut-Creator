import os
import subprocess
import sys
import json

system_drives = ['C','D']

config_json = open("./config/settings.json", "r")
settings_list = json.load(config_json)
config_json.close()

dest = settings_list['destination_to_shortcut']


def run(cmd):
    subprocess.run(["powershell", "-Command", cmd], capture_output=True)

while True:
    try:
        os.system('wmic logicaldisk get caption > output.txt')
        drives = open("output.txt","r")
        drives_list = drives.readlines()
        drives.close()
        drives_list.pop(0)
        external_drives = []
        for x in drives_list:
            output = x.rsplit('\x00')
            if len(output) != 2 and output[1] not in system_drives :
                external_drives.append(output[1])
        old_extern = open("external.txt","r")
        old_external_drives = old_extern.read()
        old_extern.close()


        extern = open("external.txt","w")

        for x in old_external_drives:
            if x not in external_drives:
                run("del " + dest +x+".lnk") 

        for x in external_drives:
            if x not in old_external_drives:
                run("./set-shortcut/set-shortcut " + dest + x + ".lnk " + x + ":/")
            extern.write(x)

        extern.close()

    except:
        print("Error")
        sys.exit()

    