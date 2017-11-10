from guizero import App, Text, PushButton, info, yesno, TextBox
from SecNetNmapShortcuts import common
import webbrowser
import time
import os

def do_nothing():
    print("Button was pressed")

def close_confirmation():
    if yesno("Quit?", "Did you want to close the app?"):
        app.destroy()

def wrap_button1():
    out = common.sweep('10.218.2.0/24')
    output.set(out)

def wrap_button2():
    html_file = common.XMLToHTML(common.intenseScan('10.218.2.42'))
    webbrowser.open_new_tab('file://'+os.path.abspath(html_file))
    time.sleep(5)
    if not yesno("Keep HTML?","Do you want to save the HTML file for this scan?"):
        os.remove(html_file)

def wrap_button3():
    out = common.sweep('10.218.1.0/24')
    output.set(out)

app = App("Easy Script Holder",layout="grid",width=490)
top_text = Text(app, text="This will hold buttons to execute your scripts", grid=[0,1])
spacer = Text(app,grid=[1,0])
button1 = PushButton(app,wrap_button1,text="Sweep .2 network", grid=[2,0])
button2 = PushButton(app,wrap_button2,text="Intense Scan",grid=[2,1])
button3 = PushButton(app,wrap_button3,text="Sweep .1 network",grid=[2,2])
description = Text(app,grid=[3,0],align="right",text="Scan Address:")
scanAddress = TextBox(app, grid=[3,1], width=20)
output = Text(app,grid=[4,1])
app.on_close(close_confirmation)
app.display()