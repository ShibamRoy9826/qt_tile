
export XAUTHORITY=/home/shibam/.Xauthority
export DISPLAY=:0
export DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/1000/bus"

# Variables
RINGTONE="$HOME/.local/share/qt_tile/audio/notificationSound.mp3"
DISCONNECTED="$HOME/.local/share/qt_tile/audio/disconnected.mp3"

CONNECTEDICON="$HOME/.local/share/qt_tile/icons/connection.svg"
DISCONNECTEDICON="$HOME/.local/share/qt_tile/icons/battery-discharging.svg"

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

