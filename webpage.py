from taipy.gui import Gui, notify
import pandas as pd


text = "Protecting your study space, one honk at a time!"

stylekit = {
  "light_goose_cream": "#e8ddc0",
  "dark_brown_goose": "#5f5145",
  "light_goose_tan": "#bfb299",
  "goose_black": "#2d2a29",
  "medium_goose_brown": "#756c5f",
}

# Definition of the page
page = """
# GuardGoose
<|{text}|>
<br></br>
<|button|class_name=fullwidth plain|label=Activate Goose|on_action=activate_goose|> 

<|button|class_name=fullwidth plain|label=I'm Back|on_action=deactivate_goose|>

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

Gui(page).run(dark_mode=False)
