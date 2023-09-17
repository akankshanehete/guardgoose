from taipy import Gui
from taipy.gui import Html
from datetime import datetime

goosestatus = 'o';
latest = "Nothing to see here.";

if goosestatus == "s":
    latest = "Now\nPerson detected near device!"
elif goosestatus == "t":
    latest = "Now\nAttention! Your device has been moved!"
else:
    latest = "Nothing to see here."



page = """

# Notifications

<|layout|columns=1|
<|card newcard-bg|
%s
{: .m1}
|>
>
<|layout|columns=1 1|
<|card card-bg|
1 hour ago\n
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
<|card card-bg|
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

""" % (latest)

def getnotifpage():
    return page

Gui(page, css_file="styles.css").run( use_reloader=True, port=5001, dark_mode=False)

