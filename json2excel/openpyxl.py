import openpyxl
import json
import PySimpleGUI as sg


#Get File to read
infile = sg.popup_get_file('Please enter a file name', title="JSON 2 Excel Utility",
                           button_color="grey", background_color="blue")

json_data = {}

with open(infile) as json_file:
    json_data = json.load(json_file)
    print(json_data)