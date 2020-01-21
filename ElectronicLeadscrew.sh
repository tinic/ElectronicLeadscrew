#!/bin/sh
#export QT_DEBUG_PLUGINS=1
export QT_PLUGIN_PATH=/usr/lib/plugins
export QT_QPA_FONTDIR=/usr/lib/fonts
export QT_QPA_PLATFORM_PLUGIN_PATH=/usr/lib/plugins/platforms
export QT_QPA_EVDEV_TOUCHSCREEN_PARAMETERS=/dev/input/event3
export QT_QPA_PLATFORM=eglfs
#export QT_LOGGING_RULES=qt.qpa.input=true
export QT_QPA_EGLFS_TSLIB=1
halrun ElectronicLeadscrew.hal

