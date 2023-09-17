from taipy import Gui
import serialcom
import serial as ser



# variables that will dyamically change based on input (for example buttons)
text = "Protecting your study space, one honk at a time!"

root_md = """
<title>Guard Goose</title>
<|navbar|>
#GuardGoose
"""
home = """ Home
<|{text}|>
<br></br>

<|goose.png|image|class_name=image|>
<br></br>
<|button|class_name=fullwidth plain|id=activate-goose-btn|label=Activate Goose|on_action=activate_goose|> 

<|button|class_name=fullwidth plain|id=deactivate-goose-btn|label=I'm Back|on_action=deactivate_goose|>

"""


profile = """ Profile """
notifs = """ Notifications """

def activate_goose(state):
    #notify(state, 'info', f'The text is: {state.text}')
    serialcom.turnOn()
    serialcom.writeToSer()
    state.text = "Goose Activated! On high alert."
    
    while True:
        serialcom.write((serialcom.deviceStatus).to_bytes(1, byteorder='big'))
        arduinoData = ser.read()

        if (arduinoData == b'3'):
            # theft alert
            print('t')
        elif (arduinoData == b'2'):
            # suspicious activity
            print('s')


def deactivate_goose(state):
    #notify(state, 'info', f'The text is: {state.text}')
    serialcom.turnOff()
    serialcom.writeToSer()
    state.text = "Goose Deactivated! Have a productive study sesh. "

def on_change(state, var_name, var_value):
    if var_name == "text" and var_value == "Reset":
        state.text = ""
        return


pages = {
    "/": root_md,
    "Home": home,
    "Profile": profile,
    "Notifs": notifs
}
Gui(pages=pages, css_file="styles.css").run(dark_mode=False)




