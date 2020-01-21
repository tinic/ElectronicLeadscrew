#!/bin/sh

#export QT_DEBUG_PLUGINS=1
export QT_PLUGIN_PATH=/usr/lib/plugins
export QT_QPA_FONTDIR=/usr/lib/fonts
export QT_QPA_PLATFORM_PLUGIN_PATH=/usr/lib/plugins/platforms

# Make sure you set this to your touch point device, could be anything from event0 to event5
# AND also make sure that the local user has permission for this device. Usually you can add
# the user to the input group. Google "/dev/input/event0 permissions" if you have issues.
export QT_QPA_EVDEV_TOUCHSCREEN_PARAMETERS=/dev/input/event3

# For debugging you proabably want to comment this out as this forces full screen
# mode and disables the mouse.
# But note that was the only way I could get touch points to work on my system.
export QT_QPA_PLATFORM=eglfs

#export QT_LOGGING_RULES=qt.qpa.input=true
export QT_QPA_EGLFS_TSLIB=1

halrun ElectronicLeadscrew.hal

