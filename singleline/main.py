import PySimpleGUI as sg 

print(
    sg.Window('Single Line', 
            [
                [sg.Input(), sg.Button("OK"), sg.Button("Cancle")]
            ]
        ).read()
)