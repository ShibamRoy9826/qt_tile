
export XAUTHORITY=/home/shibam/.Xauthority
export DISPLAY=:0
export DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/1000/bus"

# Variables
#BATTERY=$(cat /sys/class/power_supply/BAT0/status)
RINGTONE="$HOME/Music/notificationSound.mp3"
DISCONNECTED="$HOME/Music/disconnected.mp3"

CONNECTEDICON="$HOME/Pictures/icons/connection.svg"
# CHARGINGICON="$HOME/Pictures/icons/battery-charging.svg"
DISCONNECTEDICON="$HOME/Pictures/icons/battery-discharging.svg"

# Checking battery status..

if [ "$1" = "0" ]; then
	notify-send "Disconnected" "A USB Device was just disconnected ... Bye buddy..." -u normal -i $DISCONNECTEDICON
	/usr/bin/sudo -u shibam /usr/bin/paplay --server=/run/user/1000/pulse/native $DISCONNECTED > /dev/null 2>&1

elif [ "$1" = "1" ]; then
	notify-send "Connected" "A USB Device has been plugged I just found a new friend!" -u normal -i $CONNECTEDICON 
	/usr/bin/sudo -u shibam /usr/bin/paplay --server=/run/user/1000/pulse/native $RINGTONE > /dev/null 2>&1

else
	echo "All is well:)"
fi

