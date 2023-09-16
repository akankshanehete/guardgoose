from taipy import Gui
from taipy.gui import Html
from datetime import datetime


thiefalert = """
<taipy:text>{datetime.date}</taipy:text> <taipy:text>{datetime.time}</taipy:text>
<taipy:text>{"You're device is in motion. Honking in progress."}</taipy:text> 
"""
susalert = """
<center><taipy:part>
<taipy:text>{datetime.date}</taipy:text> <taipy:text>{datetime.time}</taipy:text>
<taipy:text>{"There's seems to be someone near your device"}</taipy:text> 
</taipy:part></center>
"""

htmlpage = Html("""

<h1>Notifications</h1>
<center>
<taipy:button>
NEW NOTIFICATION
</taipy:button>
</center>

<center><taipy:layout>
<taipy:text></taipy:text>
<taipy:text></taipy:text>
<taipy:text></taipy:text>
<taipy:text></taipy:text>
<taipy:text></taipy:text>
<taipy:text></taipy:text>
<taipy:text></taipy:text>
<taipy:text></taipy:text>
</taipy:layout></center>

""")

def getnotifpage():
    return htmlpage

Gui(htmlpage).run(use_reloader=True, port=5001)