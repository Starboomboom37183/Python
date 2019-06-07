import PySimpleGUI as sg

# layout = [
#     [sg.Multiline('This is the default Text should you decide not to type anything\nthis is second line', size=(35, 3)),
#      sg.Multiline('A second multi-line', size=(35, 3),key="multiline")],
#     [sg.OK(), sg.Cancel()]
# ]
#
# window = sg.Window('Everything bagel', layout, default_element_size=(40, 1), grab_anywhere=False)
# while True:
#     event, values = window.Read()
#     print(values)
#     if event == "OK":
#         window.Element("multiline").Update("my new text result!")

import PySimpleGUI as sg
import os
import time
# Design pattern 1 - First window does not remain active

layout = [[sg.Multiline("",size=(80,20),key = "multi") ],
          [sg.Input(),sg.FolderBrowse(key="file"),sg.OK(),sg.Button("Start"),sg.Cancel()]
        ]

win1 = sg.Window('Window 1', layout)
win2_active = False
win3_active = False
while True:
    ev1, vals1 = win1.Read(timeout=100)
    print(ev1)
    if ev1 is None:
        break
    if ev1 == "OK" and vals1["file"]:
        file_list = os.listdir(vals1["file"])
        new_value = ""
        for file in file_list:
            new_value = new_value+file + "\n"
        win1.Element("multi").Update(new_value)
    if ev1 =="Cancel":
        break
    if ev1 == "Start" and not win3_active:
        win3_active = True
        layout3 = [[sg.Text(text="",key="fromulti",size=(20,2))],
                  [sg.ProgressBar(1000, orientation='h', size=(20, 20), key='progbar')],
                  [sg.Text(text="",key="percent",justification="center",size =(20,2))]]

        window3 = sg.Window('Custom Progress Meter', layout3)
        # loop that would normally do something useful
        for i in range(1000):
            # check to see if the cancel button was clicked and exit loop if clicked
            event, values = window3.Read(timeout=100)
            if event == 'Cancel' or event is None:
                break
                # update bar with loop value +1 so that bar eventually reaches the maximum
            time.sleep(0.1)
            window3.Element('fromulti').Update(vals1["multi"])
            window3.Element('progbar').UpdateBar(i + 1)
            window3.Element("percent").Update(str(round((i+1)/10,1))+str("%"))
        # done with loop... need to destroy the window as it's still open
        window3.Close()
        win3_active = False


win1.Close()