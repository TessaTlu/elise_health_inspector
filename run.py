from pneumonia_predict import scan_result
from enter_results import person
# heart()
# input()
# path_of_xray='test_image_for_pneumania_predict.jpeg'
# print(scan_result(path_of_xray))
# input()
from PIL import Image
import PySimpleGUI as sg

sg.theme('DarkAmber')
layout_1 = [[sg.Text('Hello there!  '),
             sg.Text('Choose your warrior!     ')],
            [sg.Button('heart'), sg.Button('x-ray'), sg.Button('Exit')]]
window_ = sg.Window('Health_disease', icon='icon.ico').Layout(layout_1)
while True:
    event, values = window_.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'heart':
        person()
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
                result = scan_result(values[0])
                if(result==0):
                    print("Pneumani")
                else:
                    print("Normal")

        








