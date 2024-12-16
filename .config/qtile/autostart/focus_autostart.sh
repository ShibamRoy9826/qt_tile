#!/bin/sh
libinput-gestures-setup start &
mpd &
easyfeh -res &
dunst &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
