import PySimpleGUI

layout = [  [PySimpleGUI.Text("What's your name?")],     # Part 2 - The Layout
            [PySimpleGUI.Input()],
            [PySimpleGUI.Text("What's your age?")],
            [PySimpleGUI.Input()],
            [PySimpleGUI.Button('Ok')] ]

window = PySimpleGUI.Window('Window Title', layout)
values = window.read()
print(values[1][0], values[1][1])
window.close()


