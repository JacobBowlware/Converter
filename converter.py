import PySimpleGUI as sg

result = 0

layout = [
    [sg.Input(key = '-INPUT-'), sg.Spin(['lbs - kg', 'mi - km', 'sec - min'], key = '-CONVERSION-'), sg.Button('Convert', key = '-CONVBUTTON-')],
    [sg.Text(f'Output:', key = '-OUTPUT-')]
]

window = sg.Window('Converter', layout)

while True:

    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    if event == '-CONVBUTTON-':
        input_num = values['-INPUT-']
        if input_num.isnumeric():
            match values['-CONVERSION-']:
                case 'lbs - kg':
                    result = float(input_num) * 2.20462
                    output_string = f"{input_num} lbs = {result} kg"
                
                case 'mi - km':
                    result = float(input_num) * 0.6214
                    output_string = f"{input_num} mi = {result} km"
                
                case 'sec - min':
                    result = float(input_num) / 60
                    output_string = f"{input_num} sec = {result} min"

            window['-OUTPUT-'].update(output_string)
window.close()


