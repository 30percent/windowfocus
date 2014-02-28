__author__ = 'm'

import wnck
import time
import screensection
import PySideHello


def getWindow(title):
    screen = wnck.screen_get_default()
    screen.force_update()
    window_list = screen.get_windows()
    for w in window_list:
        if w.get_name() == title:
            return w
    print "oops " + title

SPLIT=2;
screen = wnck.screen_get_default()
screen.force_update()
window_list = screen.get_windows()

#

screen_W = screen.get_width()
screen_H = screen.get_height()

sto= screensection.createSections(screen, SPLIT)


flags=wnck.WINDOW_CHANGE_X | wnck.WINDOW_CHANGE_Y | wnck.WINDOW_CHANGE_WIDTH | wnck.WINDOW_CHANGE_HEIGHT

names = []
t = 0
for w in window_list:
    names.append(w.get_name())

print names
selected = PySideHello.GuiStart(names)

selected_list = []
for i, name in enumerate(selected):
    selected_list.append(getWindow(name))

for w in selected_list:
    print w.get_name()

for i, window in enumerate(selected_list):
    sect = sto[i]
    print sect
    window.set_geometry(wnck.WINDOW_GRAVITY_NORTHWEST, flags, sect[0], sect[1], sect[2], sect[3])
    window.activate(int(time.time()))
    print window.get_name() + " ye"

#target.activate(int(time.time()))