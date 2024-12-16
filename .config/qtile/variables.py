from os import getlogin, makedirs, path
from subprocess import run

from libqtile import hook, qtile
from toml import dump, load

####### Variables =====================================================================
mod = "mod4"
username=getlogin()
config_file = f"/home/{username}/.config/qtile/config.toml"
defaultConf = f"""

[[modes]]
normal_color = "#212444"
focus_color = "#c03c5c"
border_width = 2
floating_border_width = 2
border_width_single = 2
gaps = 8

[[modes]]
normal_color = "#212444"
focus_color = "#c03c5c"
border_width = 3
floating_border_width = 1
border_width_single = 3
gaps = 5

[general]
launcher = "rofi -show drun -theme /home/{username}/.config/rofi/launcher/launcher.rasi"
powermenu = "sh -c ~/.config/rofi/powermenu/powermenu.sh"
browser = "zen-browser"
file_manager = "thunar"
terminal_x11 = "st"
terminal_wayland = "foot"
scratchpad_enabled = true

[bar]
bar_position = "top"
bar_logo = "\U000f08c7 "
bar_fg_primary = false
always_dark_fg = false
always_light_fg = false

[screenshot]
screenshot_directory = "/home/{username}/Pictures/Screenshots"
screenshot_format = "Screenshot-%d-%b-%y__%H-%M-%S.png"
screenshot_command = "scrot -z -F ':f:'"
screenshot_copy_command = "scrot -z -F '-' | xclip -sel clipboard -t image/png"
screenshot_command_select = "scrot -z -s -F ':f:'"
screenshot_copy_command_select = "cat :f: | xclip -sel clipboard -t image/png"
screenshot_notification = true
screenshot_title = "Screenshot Captured!"
screenshot_message = "The screenshot has been captured and stored at :f: "

[mode_settings]
mode = "focus"

[colors]
bg = "#21244480"
bg2 = "#21244499"
fg = "#cdd6f4"
fg2 = "#9399b2"
urgent = "#f38ba8"
primary = "#c03c5c"
"""


#######  Config File  =================================================================

# Creating Config if it doesn't exist
if not path.isfile(config_file):
    with open(config_file, "w") as f:
        f.write(defaultConf)

# Reading config
with open(config_file, "r") as fl:
    config = load(fl)

# Creating screenshot directory if it doesn't exist
scr_dir = config["screenshot"]["screenshot_directory"]
if not path.exists(scr_dir):
    makedirs(scr_dir)


####### Some more Variables ============================================================
launcher = config["general"]["launcher"]
powermenu_cmd = config["general"]["powermenu"]
browser = config["general"]["browser"]
file_manager = config["general"]["file_manager"]
terminal_x11 = config["general"]["terminal_x11"]
terminal_wayland = config["general"]["terminal_wayland"]

# Terminal
if qtile.core.name == "x11":
    term = config["general"]["terminal_x11"]
else:
    term = config["general"]["terminal_wayland"]

md={"normal":[[],[]],"focus":[[],[]]} # first list for keybindings, second for bars
mode_list=["normal","focus"]

#### Bar =============================================================================
time_format = "%-I:%M %p"
date_format = "%A , %-d %B %Y"

#### Colors ==========================================================================
bg = config["colors"]["bg"]
bg2 = config["colors"]["bg2"]
fg = config["colors"]["fg"]
fg2 = config["colors"]["fg2"]
urgent = config["colors"]["urgent"]
primary = config["colors"]["primary"]
