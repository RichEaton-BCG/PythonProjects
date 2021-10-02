import pandas as pd
import json
import xlwt
import PySimpleGUI as sg

#Get File to read
infile = sg.popup_get_file('Please enter a file name', title="JSON 2 Excel Utility",
                       button_color="grey", background_color="blue")

df = pd.DataFrame
df = pd.read_json(infile)

df.to_excel('json2excel\data_out\converted.xls')

# Closing file
#f.close()


#conv = Converter()
#conv.convert(infile, Writer(file='json2excel\data_out\converted.xls'))


