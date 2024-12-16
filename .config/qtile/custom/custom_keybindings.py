from libqtile.config import Key
from libqtile.lazy import lazy
from functions import shiftBar,randomWall,prevWall,nextWall
from variables import *

keys = [
    Key(
        [mod, "shift"],
        "b",
        shiftBar(),
        desc="Shifts bar from top to bottom or vice-versa",
    ),
    Key(
        [mod, "shift"],
        "w",
        randomWall(),
        desc="Change to random wallpaper",
    ),
    Key(
        [mod, "shift"],
        "left",
        prevWall(),
        desc="Change to previous wallpaper",
    ),
    Key(
        [mod, "shift"],
        "right",
        nextWall(),
        desc="Change to next wallpaper",
    ),
    Key([mod], "m", lazy.spawn(f"{terminal_x11} ncmpcpp"), desc="Start ncmpcpp"),
    Key([mod, "shift"], "p", lazy.spawn("mpc -p 6200 toggle"), desc="Toggle Mpd music"),
    ## Keybindings to control mouse,
    Key(["mod1"],"k",lazy.spawn("xdotool mousemove_relative -- 0 -25"), desc="Move mouse to up"),
    Key(["mod1"],"j",lazy.spawn("xdotool mousemove_relative -- 0 25"), desc="Move mouse to down"),
    Key(["mod1"],"h",lazy.spawn("xdotool mousemove_relative -- -25 0"), desc="Move mouse to left"),
    Key(["mod1"],"l",lazy.spawn("xdotool mousemove_relative -- 25 0"), desc="Move mouse to right"),
    Key(["mod1"],"q",lazy.spawn("xdotool click 1"), desc="Left click using the mouse"),
    Key(["mod1"],"r",lazy.spawn("xdotool click 2"), desc="Middle click using the mouse"),
    Key(["mod1"],"e",lazy.spawn("xdotool click 3"), desc="Right click using the mouse"),
    Key(["mod1","shift"],"q",lazy.spawn("xdotool mousedown 1"), desc="Hold left click"),
    Key(["mod1","shift"],"e",lazy.spawn("xdotool mousedown 3"), desc="Hold right click"),
    Key(["mod1","control"],"q",lazy.spawn("xdotool mouseup 1"), desc="Release left click"),
    Key(["mod1","control"],"e",lazy.spawn("xdotool mouseup 3"), desc="Release right click"),

]



