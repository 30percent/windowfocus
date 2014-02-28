__author__ = 'm'
import wnck


def createSections(screen, split):
    screen_W = screen.get_width()
    screen_H = screen.get_height()
    x = y = 0

    sections = []
    for y in range(0, split, 1):
       for x in range(0, split, 1):
           section = [x*screen_W/split, y*(screen_H/split), screen_W/split, screen_H/split]
           sections.append(section)
    return sections

def withinarea(wind, area):
    if wind[0] >= area[0] and wind[0]+wind[2] <= area[0]+area[2]:
        if wind[1] >= area[1] and wind[1]+wind[3] <= area[1]+area[3]:
            return True
    return False

