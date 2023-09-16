from taipy import Gui
from taipy.gui import Html

profilepic = "IMG_0002-modified.png"
name = "Kristine"
uni = "McMaster University"
phone = "6479694546"
email = "kristine.uchendu@gmail.com"

htmlpage = Html("""

<h1>Profile</h1>

<center><taipy:part >

<taipy:image width="200px">{profilepic}</taipy:image>

<br></br>
<br></br>
<taipy:input>{name}</taipy:input>
<br></br>
<taipy:input>{uni}</taipy:input>
<br></br>
<taipy:input>{phone}</taipy:input>
<br></br>
<taipy:input>{email}</taipy:input>

</taipy:part></center>

""")

Gui(htmlpage).run(dark_mode=False, use_reloader=True, port=5001)