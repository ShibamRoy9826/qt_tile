#!/bin/sh
libinput-gestures-setup start &
mpd &
picom -b &
easyfeh -res &
dunst &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
