![logo](https://github.com/ShibamRoy9826/qt_tile/blob/main/assets/Qt_Tile_Icon_Light.png?raw=true)

A Simple and easy to setup qtile rice, which comes with an installer for **Arch Users** :)

Its made so that people can configure qtile much more easily and in a more organised manner!

## Features 😎

- Comes with a super simple installer(For Arch Users Only)
- Modes like focus mode and normal mode
- Organised file structure
- There are keybindings for most of the operations!
- Beautiful animations made with [pijulius-picom](https://github.com/pijulius/picom)
- Fully customized app launcher and powermenu (A Small section of the powermenu was taken from [adi1090x-rofi](https://github.com/adi1090x/rofi))
- Some Scripts to perform extra tasks too(Optional, you can tell the installer not to install it)

## Installation 🛠️

> [!WARNING]
> The installer still faced limited testing, it mostly works, but still it may not install everything properly!
> Please raise an issue if you face any trouble

Installation is really simple, just run these commands:

```bash
git clone https://github.com/ShibamRoy9826/qt_tile.git
cd qt_tile
python installer.py
```

Next, make your choices as the installer asks you questions, most of the questions are just in the format of yes or no.
Once you're done, it will ask for a confirmation and automatically start the installation!

> [!NOTE]
> If picom causes lag in your system, or behaves in a weird way, make sure to change your backend to "xrender", to do that, edit `$HOME/.config/picom.conf` and replace `backend='glx'` with `backend='xrender'`

<h2>
    Usage <img src="https://github.com/Anmol-Baranwal/Cool-GIFs-For-GitHub/assets/74038190/7b282ec6-fcc3-4600-90a7-2c3140549f58" width="30">
</h2>

These configs make customization way much more easier! you can simply edit `$HOME/.config/qtile/config.toml`

This is the default, the options are pretty much self-explainatory:
```
# Options for the normal mode
[[modes]]
normal_color = "#1e1e2e"
focus_color = "#6c7086"
border_width = 2
floating_border_width = 2
border_width_single = 2
gaps = 8

# Options for the focus mode

[[modes]]
normal_color = "#1e1e2e"
focus_color = "#6c7086"
border_width = 3
floating_border_width = 1
border_width_single = 3
gaps = 5


[general]
launcher = "rofi -show drun -theme ~/.config/rofi/launcher/launcher.rasi"
powermenu = "sh -c ~/.config/rofi/powermenu/powermenu.sh"
browser = "zen-browser"
file_manager = "thunar"
terminal_x11 = "kitty"
terminal_wayland = "foot"
scratchpad_enabled = true

[bar]
bar_position = "top"
bar_logo = "\U000f08c7 "
bar_logo_fg_color = true
bar_fg_primary = false
always_dark_fg = false
always_light_fg = true

[screenshot]
screenshot_directory = "~/Pictures/Screenshots"
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
bg = "#11111b"
bg2 = "#1e1e2e"
fg = "#cdd6f4"
fg2 = "#9399b2"
urgent = "#f38ba8"
primary = "#89b4fa"
```

## Keybindings ⌨️
---
Here are all the main keybindings, they too can be customized by modifying `modes.py` the modes.py includes separate keybindings for each mode, by default they are the same, but you can customize it!

<div align="center">

| Keys | Action |
| :--- | :--- |
| <kbd>Super</kbd> + <kbd>Q</kbd> | Close focused window|
| <kbd>Super</kbd> + <kbd>Shift</kbd> + <kbd>M</kbd> | Shift mode |
| <kbd>Super</kbd> + <kbd>H</kbd> | Move focus to left window|
| <kbd>Super</kbd> + <kbd>J</kbd> | Move focus to down window|
| <kbd>Super</kbd> + <kbd>K</kbd> | Move focus to up window|
| <kbd>Super</kbd> + <kbd>L</kbd> | Move focus to right window|
| <kbd>Super</kbd> + <kbd>Control</kbd> + <kbd>H</kbd>| Grow window to left|
| <kbd>Super</kbd> + <kbd>Control</kbd> + <kbd>J</kbd>| Grow window to down|
| <kbd>Super</kbd> + <kbd>Control</kbd> + <kbd>K</kbd>| Grow window to up|
| <kbd>Super</kbd> + <kbd>Control</kbd> + <kbd>L</kbd>| Grow window to right|
| <kbd>Super</kbd> + <kbd>Left</kbd> | Move to previous Group/workspace|
| <kbd>Super</kbd> + <kbd>Right</kbd> | Move to next Group/workspace|
| <kbd>Super</kbd> + <kbd>Shift</kbd> + <kbd>N</kbd> | Reset window sizes|
| <kbd>Super</kbd> + <kbd>Shift</kbd> + <kbd>Enter</kbd> | Toggle splitting |
| <kbd>Super</kbd> + <kbd>Enter</kbd> | Launch Terminal|
| <kbd>Super</kbd> + <kbd>B</kbd> | Launch Browser|
| <kbd>Super</kbd> + <kbd>E</kbd> | Launch File Manager|
| <kbd>Super</kbd> + <kbd>D</kbd> | Launch Application Launcher|
| <kbd>Super</kbd> + <kbd>Shift</kbd> + <kbd>S<kbd> | Launch Powermenu |
| <kbd>Super</kbd> + <kbd>Tab</kbd> | Toggle between layouts |
| <kbd>Super</kbd> + <kbd>S</kbd> | Toggle scratchpad terminal |
| <kbd>Super</kbd> + <kbd>Tab</kbd> | Toggle scratchpad screen recorder|
| <kbd>Super</kbd> + <kbd>F</kbd> | Toggle Fullscreen |
| <kbd>Super</kbd> + <kbd>V</kbd> | Toggle Floating |
| <kbd>Super</kbd> + <kbd>Control</kbd> + <kbd>R</kbd> | Reload Configuration |
| <kbd>Super</kbd> + <kbd>Control</kbd> + <kbd>Q</kbd> | Reload Configuration |

</div>

There are some mouse bindings too,
- You can drag and move windows by holding left click while pressing the Super key
- You can resize windows by holding and moving right click while pressing the super key

## Shell 📟

If you installed zsh from the installer, its using [zinit](https://github.com/zdharma-continuum/zinit) with [powerlevel10k](https://github.com/romkatv/powerlevel10k) , performance benchmarks are mentioned in their repository. I have commented the lines in `.zshrc` by which you can enable lazy-loading too!
There are some plugins too, the list includes:
- zsh-syntax-highlighting
- zsh-completions
- zsh-autosuggestions
- fzf-tab
There are some keybindings too:

<div align="center">

| Keys | Action |
| :--- | :--- |
| <kbd>Ctrl</kbd> + <kbd>B</kbd> | Move to previous word | 
| <kbd>Ctrl</kbd> + <kbd>W</kbd> | Move to next word |
| <kbd>Ctrl</kbd> + <kbd>D</kbd> | Delete previous word |
| <kbd>Ctrl</kbd> + <kbd>J</kbd> | Move backwords in history |
| <kbd>Ctrl</kbd> + <kbd>K</kbd> | Move forward in history |

</div>

There are some aliases too, which you can check at `~/.zshrc`

## Gestures

There are many gestures too if you said yes for gestures in the installer. You can configure them yourself by running [gestures](https://gitlab.com/cunidev/gestures) which is a GUI for libinput-gestures, its installed automatically during the installation. The gestures that are included with this rice are:

<div align="center">

| Keys | Action |
| :--- | :--- |
|  3 finger swipe up | Opens up thunar | 
|  3 finger swipe left | Moves to the previous workspace | 
|  3 finger swipe right | Moves to the next workspace | 
|  4 finger swipe right | Closes the current application | 
|  4 finger swipe left | Closes the current application | 
|  3 finger pinch clockwise | Opens up ncmpcpp(To play some music) | 
|  3 finger pinch anticlockwise | Opens up ncmpcpp(To play some music) | 
|  4 finger pinch anticlockwise | Toggles fullscreen | 
|  4 finger pinch clockwise | Toggles fullscreen | 
 
</div>

## Customization 🛠️

Along with the configuration there is a separate folder called custom, where you can define your own custom functions, custom layouts and keybindings!

> [!TIP]
> As a few examples, some of the keybindings are already included by default in the `custom/custom_keybindings.py`
Custom Layouts(Scratchpads) are there in `custom/custom_layouts.py` which by default includes the recorder scratchpad and the terminal scratchpad. Customize them as per your needs!

<div align="center">


| Keys | Action |
| :--- | :--- |
| <kbd>Super</kbd> + <kbd>Shift</kbd> + <kbd>B</kbd> | Shift Bar position |
| <kbd>Super</kbd> + <kbd>Shift</kbd> + <kbd>W</kbd> | Change to a random wallpaper |
| <kbd>Super</kbd> + <kbd>Shift</kbd> + <kbd>Left</kbd> | Change to previous wallpaper |
| <kbd>Super</kbd> + <kbd>Shift</kbd> + <kbd>Right</kbd> | Change to next wallpaper |
| <kbd>Super</kbd> + <kbd>M</kbd> | Launch Ncmpcpp |
| <kbd>Super</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> | Toggle mpd music |
| <kbd>Alt</kbd> + <kbd>H</kbd> | Move Cursor to left |
| <kbd>Alt</kbd> + <kbd>J</kbd> | Move Cursor to left |
| <kbd>Alt</kbd> + <kbd>K</kbd> | Move Cursor to left |
| <kbd>Alt</kbd> + <kbd>L</kbd> | Move Cursor to left |
| <kbd>Alt</kbd> + <kbd>Q</kbd> | Left click with mouse |
| <kbd>Alt</kbd> + <kbd>R</kbd> | Middle click with mouse |
| <kbd>Alt</kbd> + <kbd>E</kbd> | Right click with mouse |
| <kbd>Super</kbd> + <kbd>Shift</kbd> + <kbd>Q</kbd> | Hold Left click |
| <kbd>Super</kbd> + <kbd>Shift</kbd> + <kbd>E</kbd> | Hold Right click |
| <kbd>Super</kbd> + <kbd>Control</kbd> + <kbd>Q</kbd> | Release left click |
| <kbd>Super</kbd> + <kbd>Control</kbd> + <kbd>E</kbd> | Release right click |

</div>

## More Customization (Tips) 🛠️

1) If you have [EasyFeh](https://github.com/ShibamRoy9826/easyfeh) installed then, you can use the color changing script(You need to enable that too during installation...) to automatically change system color scheme! To do that, just modify this in the easyfeh config at `$HOME/.config/easyfeh/config.toml` like this

```
[palette]
save_palette = true
palette_path = "/home/{username}/.config/easyfeh/palette.txt"
dominant_color_quality = 5
general_palette_copy = true
complete_palette_path = "/home/{username}/.config/easyfeh/full_palette.txt"
autogenerate_palette = true
```
and also:

```
[triggers]
notify_on_change = false
command_on_change = true
notif_message = "Wallpaper Changed!"
notif_body = "Wallpaper has been set to :f: "
command = "python ~/scripts/changeColors.py && xdotool key ctrl+super+r"
```
Make sure to replace `{username}` with your username.
If you didn't install the scripts while running the installer, no problem, you can manually download the scripts from [here](https://github.com/ShibamRoy9826/qt_tile/tree/main/.config/scripts) and place them at `~/scripts` or any other place where you want(But just make sure to use that path in the config mentioned above).

2) If you're using zen-browser-bin, you can use zen-browser-avx2-bin instead if your CPU supports AVX2, you can check if your CPU supports that by running this:
```bash
grep -q -i avx2 /proc/cpuinfo && echo true
```
You can read more at [zen documentation](https://docs.zen-browser.app/guides/generic-optimized)

3) You can setup cronjobs for the water reminder, and eye blink reminder to work, the scripts are included at [here](https://github.com/ShibamRoy9826/qt_tile/tree/main/.config/scripts) incase you didn't download them while running the installer(Put them at `~/Scripts` if yyou want to use this tip). 
First of all you may want to install cronie

```bash
sudo pacman -S cronie
```

Once you're done with the installation, you need to enable it  and start it

```bash
sudo systemctl enable cronie
sudo systemctl start cronie
```

Now, you can setup the tasks now, by running `crontab -e`, justwrite these as your editor opens up:
```bash
*/30 * * * * /home/{username}/scripts/WaterReminder.sh
*/20 * * * * /home/{username}/scripts/LessEyeStrain.sh
0 * * * * /home/{username}/scripts/nightLight.sh
```
That's it! now you should receive notifications for water reminder, for blinking your eyes, and even the automatic nightlight(requires sct to be installed)

4) The scripts are pretty much simple, you can customize them yourself to have some fun! they are stored at `~/scripts` if you installed them while running the installer

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

## FAQ ❔

### 1) What things does the installer install?

It mostly installs just what you want it to install(It asks for many things). Ofcourse, it also install the dependencies for your choices, and there are some mandatory packages for this rice to work, here's the list:
- qtile
- wget
- git
- brightnessctl
- Iosevka Nerd Fonts
- papirus-icon-theme
- zoxide
- xdotool
- unzip
- python-psutil
- python-mpd2
- qtile-extras-git
- python-pulsectl-asyncio

### 2) What things does it install altogether if I say yes to everything?

It includes the packages mentioned above, along with these packages:
- kitty
- zsh + powerlevel10k + zinit + eza + fzf
- easyfeh
- rofi
- xclip
- dunst
- scrot
- mpd + mpc
- ncmpcpp
- zen-browser-bin
- thunar
- colloid-gtk-theme-git
- picom-pijulius + meson + ninja + uthash
- libinput-gestures
- yt-dlp + python-youtube-search-python + sct
- python-httpx
- simplescreenrecorder
- Some extra scripts
- some asset files stored at `~/.local/share/qt_tile/`


### 3) How does it download the packages?

It uses pacman to download most packages, but if the package doesn't exist in the extra repository, it's downloaded from the AUR

### 4) Why are you using powerlevel10k its not maintained anymore!

I know powerlevel10k isn't maintained anymore, but that shouldn't be a problem, its just a zsh theme and already quite feature rich, besides it's very easy to customize and looks pretty good. You can definitely provide suggestions via raising an issue.

### 5) Why is mpd not working? I am trying to run it...!

Mpd is configured a little different, its running at port 6200, I don't know but I was facing some issues with the default, so i changed the port and its working, didn't bother to change it... However, I would definitely change it if creates any problems in the future.


## Credits 🙏

The rofi powermenu is a little inspired by [adi1090x-rofi](https://github.com/adi1090x/rofi), and the default rofi config too. 
Thanks to him for the amazing design ideas!

Thanks to the developers of all the other packages too that this rice uses, without them this rice would never have been complete.

## Contributing 🤝

Everyone is welcome to contribute to the code!
You can also raise an issue, or suggest any features that you think would be great :)

> ✨ Please star this repository if you liked this project 😁
