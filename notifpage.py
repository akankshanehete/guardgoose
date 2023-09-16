from taipy import Gui
from taipy.gui import Html

htmlpage = Html("""
<title>Guard Goose</title>
<h1>Notifications</h1>

<taipy:pane anchor="top">
<taipy:button>
i
</taipy:button>
</taipy:pane>

<center><taipy:layout>

<br></br>
<br></br>
<taipy:input>{"name"}</taipy:input>
<br></br>
<taipy:input>{"uni"}</taipy:input>
<br></br>
<taipy:input>{"phone"}</taipy:input>
<br></br>
<taipy:input>{"email"}</taipy:input>

</taipy:layout></center>

""")

Gui(htmlpage).run(stylekit = {"light_goose_cream": "#e8ddc0",
  "dark_brown_goose": "#5f5145",
  "light_goose_tan": "#bfb299",
  "goose_black": "#2d2a29",
  "medium_goose_brown": "#756c5f"
  }, use_reloader=True, port=5001)