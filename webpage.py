from taipy import Gui
import pandas as pd

text = "Original text"

page = """
# Getting started with Taipy GUI

My text: <|{text}|>

<|{text}|input|>
"""

Gui(page).run(dark_mode=False)
