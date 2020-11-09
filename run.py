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
window_ = sg.Window('Indi', icon='icon.ico').Layout(layout_1)
while True:
    event, values = window_.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'heart':
        person()
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
                result = scan_result(values[0])
                
                print("I think you should know that my accuracy on detecting pneumonia is 92 percents")
                print("So keep that in mind")
                if(result==0):
                    print("Most likely you have a pneumonia. This diagnosis is not a verdict")
                    print("You have to consult a doctor about that as soon as possible")
                else:
                    print("I did not find any reason to be worry")
                    print("but if you have symptoms of pneumonia, you should consult your doctor")
        break







