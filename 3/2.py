# !/usr/bin/python
# -*- coding: UTF-8 -*-

import PySimpleGUI as sg

"""      
Demonstrates using a "tight" layout with a Dark theme.      
Shows how button states can be controlled by a user application.  The program manages the disabled/enabled      
states for buttons and changes the text color to show greyed-out (disabled) buttons      
"""

layout = [
    [sg.Canvas(size=(100, 100), background_color='red', key='canvas')],
    [sg.T('Change circle color to:'), sg.Button('Red'), sg.Button('Blue')]
]

window = sg.Window('Canvas test', layout)
window.Finalize()

canvas = window.Element('canvas')
cir = canvas.TKCanvas.create_oval(50, 50, 100, 100)

while True:
    event, values = window.Read()
    if event is None:
        break
    if event == 'Blue':
        canvas.TKCanvas.itemconfig(cir, fill="Blue")
    elif event == 'Red':
        canvas.TKCanvas.itemconfig(cir, fill="Red")