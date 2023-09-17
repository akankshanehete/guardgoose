from taipy import Gui
from taipy.gui import Html
#import serialcom
import serial as ser
import serialcom



# variables that will dyamically change based on input (for example buttons)
text = "Protecting your study space, one honk at a time!"

root_md = """
<title>Guard Goose</title>
<|navbar|>
#Guard🦆Goose
"""
home = """ Home
<|{text}|>
<br></br>

<|goose.png|image|class_name=image|>
<br></br>
<|button|class_name=fullwidth plain|id=activate-goose-btn|label=Activate Goose|on_action=activate_goose|> 

<|button|class_name=fullwidth plain|id=deactivate-goose-btn|label=I'm Back|on_action=deactivate_goose|>

"""


def activate_goose(state):
    serialcom.turnOn()
    serialcom.writeToSer()
    state.text = "Goose Activated! On high alert."
    
    # while True:
    #     arduinoData = serialcom.serial.read()

    #     if (arduinoData == b'3'):
    #         # theft alert
    #         print('t')
    #     elif (arduinoData == b'2'):
    #         # suspicious activity
    #         print('s')


def deactivate_goose(state):
    serialcom.turnOff()
    serialcom.writeToSer()
    state.text = "Goose Deactivated! Have a productive study sesh. "

def on_change(state, var_name, var_value):
    if var_name == "text" and var_value == "Reset":
        state.text = ""
        return

# profile page variables

profilepic = "IMG_0002-modified.png"
name = "Kristine"
uni = "McMaster University"
phone = "6479694546"
email = "kristine.uchendu@gmail.com"

profile = Html("""

<center>                           
<p class="page-header-text">Your Profile</p>
</center> 

<center><taipy:part >

<taipy:image width="200px">{profilepic}</taipy:image>

<br></br>               
<taipy:input class="input-field">{name}</taipy:input>
<br></br>
<taipy:input class="input-field">{uni}</taipy:input>
<br></br>
<taipy:input class="input-field">{phone}</taipy:input>
<br></br>
<taipy:input class="input-field">{email}</taipy:input>

</taipy:part></center>

""")
               
notifs = """ 
# Notifications

<|layout|columns=1|
<|card newcard-bg|
Attention! Your device has been moved!
{: .m1}
|>
>
<|layout|columns=1 1|
<|card card-bg|
1 min ago\n
Person detected near device!
{: .m1}
|>
<|card card-bg|
2 hours ago\n
Person detected near device!
{: .m1}
|>
<|card card-bg|
2 hours ago\n
Person detected near device!
{: .m1}
|>
<|card card-bg|
7 hours ago\n
Person detected near device!
{: .m1}
|>
<|card card-bg|
11 hours ago\n
Person detected near device!
{: .m1}
|>
<|card bigalert-bg|
13 hours ago\n
Attention! Your device has been moved!
{: .m1}
|>
<|card card-bg|
16 hours ago\n
Person detected near device!
{: .m1}
|>
<|card card-bg|
17 hours ago\n
Person detected near device!
{: .m1}
|>
|>

"""

pages = {
    "/": root_md,
    "Home": home,
    "Profile": profile,
    "Notifs": notifs
}
Gui(pages=pages, css_file="styles.css").run(dark_mode=False)




