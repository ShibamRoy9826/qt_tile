export XAUTHORITY=/home/shibam/.Xauthority
export DISPLAY=:0
export DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/1000/bus"

# Variables
RINGTONE="$HOME/Music/WaterDroplet.mp3"
ICON="$HOME/Pictures/icons/water.svg"

notify-send "Water Reminder" "Drink some water buddy, You will die otherwise... I can't live without you :(" -u normal -i $ICON

/usr/bin/sudo -u shibam /usr/bin/paplay --server=/run/user/1000/pulse/native $RINGTONE > /dev/null 2>&1
