from taipy.gui import Gui
from webpage import page

root_md="<|navbar|>"
page1_md= "## This is page 2"
page2_md="## This is page 2"

pages = {
    "/": root_md,
    "Page-1": page1_md,
    "Page-2": page2_md
}

Gui(pages=pages).run()