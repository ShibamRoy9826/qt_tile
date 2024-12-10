#!/usr/bin/env bash

# CMDs
uptime=`uptime -p | sed -e 's/up //' -e 's/ hours\?/ hr/' -e 's/ minutes\?/ m/' | tr -d ','`
host=`whoami`

# Options
shutdown=''
reboot=''
lock=''
suspend=''
logout=''

# Rofi CMD
rofi_cmd() {
	rofi -dmenu \
		-p "$uptime" \
		-mesg "$uptime" \
		-theme $HOME/.config/rofi/powermenu/powermenu.rasi
}


# Pass variables to rofi dmenu
run_rofi() {
	echo -e "$shutdown\n$suspend\n$logout\n$reboot\n$lock" | rofi_cmd
}

# Execute Command
run_cmd() {
  if [[ $1 == '--shutdown' ]]; then
    shutdown now
  elif [[ $1 == '--reboot' ]]; then
    reboot
  elif [[ $1 == '--suspend' ]]; then
    mpc -q -p 6200 pause
    # amixer set Master mute
    pactl set-sink-mute @DEFAULT_SINK@ toggle
    systemctl suspend
  elif [[ $1 == '--logout' ]]; then
    pkill -u $(whoami)
  fi
}

# Actions
chosen="$(run_rofi)"
case ${chosen} in
    $shutdown)
		run_cmd --shutdown
        ;;
    $reboot)
		run_cmd --reboot
        ;;
    $lock)
		if [[ -x '/usr/bin/betterlockscreen' ]]; then
			betterlockscreen -l
		elif [[ -x '/usr/bin/i3lock' ]]; then
			i3lock
		fi
        ;;
    $suspend)
		run_cmd --suspend
        ;;
    $logout)
		run_cmd --logout
        ;;
esac
