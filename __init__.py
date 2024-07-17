# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo, qconnect
# import all of the Qt GUI library
from aqt.qt import *

from . import content_creatory

import re

from aqt import gui_hooks

# We're going to add a menu item below. First we want to create a function to
# be called when the menu item is activated.

def testFunction() -> None:
    # get the number of cards in the current collection, which is stored in
    # the main window
    cardCount = mw.col.cardCount()

    # show a message box
    showInfo("Maara ist die geilste. Card count: %d" % cardCount)

# create a new menu item, "test"
action = QAction("test", mw)
# set it to call testFunction when it's clicked
qconnect(action.triggered, testFunction)
# and add it to the tools menu
mw.form.menuTools.addAction(action)

def myfunc(card):
    print("question shown, card question is:", card.question())

def myfunc_answ(card):
    print("start total")
    print(card.a())
    print(card.id)
    print("end total")
    print("start get_content")
    content_creatory.create_mind_map(card.id)



gui_hooks.reviewer_did_show_question.append(myfunc)
gui_hooks.reviewer_did_show_answer.append(myfunc_answ)