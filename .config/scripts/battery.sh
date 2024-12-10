export XAUTHORITY=/home/shibam/.Xauthority
export DISPLAY=:0
export DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/1000/bus"

# Variables
BATTERY_LEVEL=$(cat /sys/class/power_supply/BAT0/capacity)
BATTERY=$(cat /sys/class/power_supply/BAT0/status)
RINGTONE="$HOME/Music/notificationSound.mp3"
RINGTONE_CRITICAL="$HOME/Music/notificationCritical.mp3"
ICON="$HOME/Addons/CustomScripts/Res/battery.svg"

FULL=/tmp/batteryfull
LOW=/tmp/batterylow
MID=/tmp/batterymid
OKAY=/tmp/batteryokay

# Checking battery percentage..
checkBattery(){
	if [ "$BATTERY_LEVEL" -lt 15 ] && [ ! -f $LOW ]; then
	
		notify-send "Critical Battery! " "Battery is about to die:(  Please feed me!!!..." -u critical
		/usr/bin/sudo -u shibam /usr/bin/paplay --server=/run/user/1000/pulse/native $RINGTONE_CRITICAL > /dev/null 2>&1
		touch $LOW

		rm $FULL
		rm $OKAY
		rm $MID

	elif [ "$BATTERY_LEVEL" -lt 30 ] && [ ! -f $OKAY ]; then
		notify-send "Okaish battery..." "Am hungry...Give me energy if possible..." -u normal
		/usr/bin/sudo -u shibam /usr/bin/paplay --server=/run/user/1000/pulse/native $RINGTONE > /dev/null 2>&1
		touch $OKAY

		rm $FULL
		rm $LOW
		rm $MID

	elif [ "$BATTERY_LEVEL" -eq 50 ] && [ ! -f $MID ]; then
		notify-send "Half discharged" "Battery hit 50%..." -u normal
		/usr/bin/sudo -u shibam /usr/bin/paplay --server=/run/user/1000/pulse/native $RINGTONE > /dev/null 2>&1
		touch $MID

		rm $FULL
		rm $LOW
		rm $OKAY

	elif [ "$BATTERY_LEVEL" -eq 99 ] && [ ! -f $FULL ]; then
		notify-send "Fully Charged! " "Wooohoo! I am feeling energetic!" -u normal
		/usr/bin/sudo -u shibam /usr/bin/paplay --server=/run/user/1000/pulse/native $RINGTONE > /dev/null 2>&1
		touch $FULL

		rm $OKAY
		rm $LOW
		rm $MID
	else 
		echo "All is well..."

	fi
}


if [ "$BATTERY" = "Discharging" ]; then
	checkBattery
else
	if [ "$BATTERY_LEVEL" -eq 99 ] && [ ! -f $FULL ]; then
		notify-send "Fully Charged! " "Wooohoo! I am feeling energetic!" -u normal
		/usr/bin/sudo -u shibam /usr/bin/paplay --server=/run/user/1000/pulse/native $RINGTONE > /dev/null 2>&1
		touch $FULL
		rm $OKAY
		rm $LOW
		rm $MID
	fi
fi
