from taipy.gui import Gui, notify, navigate
import pandas as pd


text = "Protecting your study space, one honk at a time!"

# Definition of the page
page = """
# GuardGoose
<|{text}|class_name=title-text|>
<br></br>

<|goose.png|image|label=this is an image|class_name=image|>
<br></br>
<|button|class_name=fullwidth plain|id=activate-goose-btn|label=Activate Goose|on_action=activate_goose|> 

<|button|class_name=fullwidth plain|id=deactivate-goose-btn|label=I'm Back|on_action=deactivate_goose|>


"""

def activate_goose(state):
    #notify(state, 'info', f'The text is: {state.text}')
    state.text = "Goose Activated! On high alert."

def deactivate_goose(state):
    #notify(state, 'info', f'The text is: {state.text}')
    state.text = "Goose Deactivated! Have a productive study sesh. "

def on_change(state, var_name, var_value):
    if var_name == "text" and var_value == "Reset":
        state.text = ""
        return
    


Gui(page, css_file="styles.css").run(dark_mode=False)




