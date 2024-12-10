
export XAUTHORITY=/home/shibam/.Xauthority
export DISPLAY=:0
export DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/1000/bus"

# Variables
#BATTERY=$(cat /sys/class/power_supply/BAT0/status)
RINGTONE="$HOME/Music/notificationSound.mp3"
DISCONNECTED="$HOME/Music/disconnected.mp3"

CHARGINGICON="$HOME/Pictures/icons/battery-charging.svg"
DISCHARGINGICON="$HOME/Pictures/icons/battery-discharging.svg"

# Checking battery status..

if [ "$1" = "0" ]; then
	notify-send "Disconnected" "You unplugged the charger, Battery is Discharging...." -u normal -i $DISCHARGINGICON
	/usr/bin/sudo -u shibam /usr/bin/paplay --server=/run/user/1000/pulse/native $DISCONNECTED > /dev/null 2>&1

elif [ "$1" = "1" ]; then
	notify-send "Charging" "The charger is plugged in, i am happy:)" -u normal -i $CHARGINGICON
	/usr/bin/sudo -u shibam /usr/bin/paplay --server=/run/user/1000/pulse/native $RINGTONE > /dev/null 2>&1

else
	echo "All is well:)"
fi

