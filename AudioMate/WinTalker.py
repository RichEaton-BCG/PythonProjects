import pyttsx3
import PySimpleGUI as sg 


text = sg.popup_get_file('Please enter a file name', title="Audio Mate v001", button_color="grey", background_color="blue")
# sg.popup('Results', 'The value returned from popup_get_file', text)

engine = pyttsx3.init()
voices = engine.getProperty('voices')
infile = 'PyAudioReader\TestFile.txt'
f = open(text, 'r')
theText = f.read()
f.close()
engine.say(theText)
engine.runAndWait()


"""
sg.theme('DarkAmber')   # Add a touch of color

# All the stuff inside your window.
layout = [[sg.Text('Some text on Row 1')],
          [sg.Text('Enter something on Row 2'), sg.InputText()],
          [sg.Button('Ok'), sg.Button('Cancel')]]

# Create the Window

window = sg.Window('Audio Reader v.001', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()
"""
