export XAUTHORITY=/home/shibam/.Xauthority
export DISPLAY=:0
export DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/1000/bus"

# Variables
RINGTONE="$HOME/.local/share/qt_tile/audio/WaterDroplet.mp3"
ICON="$HOME/.local/share/qt_tile/icons/water.svg"

notify-send "Water Reminder" "Drink some water buddy, Its not healthy to stay without water yk :(" -u normal -i $ICON

/usr/bin/sudo -u shibam /usr/bin/paplay --server=/run/user/1000/pulse/native $RINGTONE > /dev/null 2>&1
