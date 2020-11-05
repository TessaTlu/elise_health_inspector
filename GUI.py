from PIL import Image
import PySimpleGUI as sg
from heart_disease import heart
import numpy as np


sg.theme('DarkAmber')
layout_1 = [[sg.Text('Hello there!'),
            sg.Text('Choose your warrior!')],
            [sg.Button('heart'), sg.Button('x-ray'), sg.Button('Exit')]]
window_ = sg.Window('Health_disease', icon='icon.ico').Layout(layout_1)
while True:
    event, values = window_.read()
    if event == 'heart':
        heart()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'x-ray':
        layout = [
            [sg.Text('File 1'), sg.InputText(), sg.FileBrowse()],
            [sg.Output(size=(88, 5))],
            [sg.Submit()]
        ]
        window = sg.Window('x-ray', icon='icon.ico').Layout(layout)
        while True:  # The Event Loop
            event, values = window.read()

            if event in (None, 'Exit', 'Cancel'):
                break
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            if event == 'Submit':
                print("Passed")
                img = Image.open(values[0], 'r')
                data = np.array(img)
                img.show()


