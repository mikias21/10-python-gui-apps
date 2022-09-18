import PySimpleGUI as sg 

layout = [
    [
        sg.Input(key='-INPUT-'), 
        sg.Spin(['km to mile', 'kg to pound', 'sec to min'], key='-UNITS-'), 
    ],
    [sg.Button("Convert", key='-CONVERT-')],
    [sg.Text('Output', key='-OUTPUT-')]
]

window = sg.Window(title="Converter", layout=layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    
    if event == '-CONVERT-':
        input_value = values['-INPUT-']
        output_str = ''
        if input_value.isnumeric():
            if values['-UNITS-'] == 'km to mile':
                output = round(float(input_value) * 0.6214, 2)
                output_str = f"{input_value} km are {output} miles"
                window['-OUTPUT-'].update(output_str)
            if values['-UNITS-'] == 'kg to pound':
                output = round(float(input_value) * 2.20462, 2)
                output_str = f"{input_value} kg are {output} pounds"
                window['-OUTPUT-'].update(output_str)
            if values['-UNITS-'] == 'sec to min':
                output = round(float(input_value) / 60, 2)
                output_str = f"{input_value} sec are {output} mins"
                window['-OUTPUT-'].update(output_str)
            
        else:
            window['-OUTPUT-'].update("Only numeric inputs allowed ")

window.close()