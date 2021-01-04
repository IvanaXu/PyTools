import PySimpleGUI as sg

filename = sg.popup_get_file('Enter the file you wish to process')
sg.popup('You entered', filename)

