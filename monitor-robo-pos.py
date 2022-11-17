
import matplotlib.pyplot as plt
import numpy as np

import blitting

x = np.linspace(0, 2 * np.pi, 100)


import sys
import time
from networktables import NetworkTables
# To see messages from networktables, you must setup logging
import logging

from collections import deque
from dataclasses import dataclass, field

lwnt_keep = 100
quiver_len = 3.0

Xs = deque(maxlen=lwnt_keep)
Ys = deque(maxlen=lwnt_keep)
H = None


def valueChanged(table, key, value, isNew):
    #print("valueChanged: key: '%s'; value: %s; isNew: %s" % (key, value, isNew))
    if key=='Robot':
        Xs.append(value[0])
        Ys.append(value[1])
        global H
        H = value[2]



def connectionListener(connected, info):
    print(info, "; Connected=%s" % connected)


def listen_to_robot():
    logging.basicConfig(level=logging.DEBUG)

    ip = "127.0.0.1"

    NetworkTables.initialize(server=ip)
    NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)

    sd = NetworkTables.getTable("SmartDashboard")

    print("sd.SubTables:", sd.getSubTables())
    sd_field = sd.getSubTable('Field')
    sd_field.addEntryListener(valueChanged, immediateNotify=True, localNotify=True)


# make a new figure
fig, ax = plt.subplots()
# add a line
(ln,) = ax.plot(list(Xs), list(Ys), marker='o', animated=True)
plt.xlim(-20,+20)
plt.ylim(-20,+20)

# add a frame number
fr_number = ax.annotate(
    "0",
    (0, 1),
    xycoords="axes fraction",
    xytext=(10, -10),
    textcoords="offset points",
    ha="left",
    va="top",
    animated=True,
)


qv = ax.quiver([10], [10], [0], [0], scale=1.0, scale_units='x', color='white')

bm = blitting.BlitManager(fig.canvas, [ln, fr_number, qv])

# make sure our window is on the screen and drawn
plt.show(block=False)
plt.pause(.1)

listen_to_robot()

i=0
while(True):
    # update the artists
    ln.set_xdata(list(Xs))
    ln.set_ydata(list(Ys))
    fr_number.set_text("frame: {i}".format(i=i))

    if H is not None:
        dx = np.cos(np.pi * H / 180.0)*quiver_len
        dy = np.sin(np.pi * H / 180.0)*quiver_len

        if len(Xs) > 0:
            x = Xs[-1]
            y = Ys[-1]

            qv.set_offsets([x,y])
            qv.set_UVC([dx], [dy])
            qv.set_color('black')
    # tell the blitting manager to do its thing
    bm.update()
    i=i+1

