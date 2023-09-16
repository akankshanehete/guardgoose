from taipy.gui import Gui, notify



# Definition of the page
notifs= """
# Notifications
"""

Gui(notifs, css_file="styles.css").run(dark_mode=False)