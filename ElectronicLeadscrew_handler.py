#####################################
# **** PUBLIC CONSTANT SECTION **** #
#####################################

# ui parameters
LATHE_VALUES = [
	[
		## Z
		[ 	0.01, 0.02, 0.04, 0.07, 0.10,
			0.20, 0.25, 0.35, 0.40, 0.45, 
			0.50, 0.60, 0.70, 0.80, 1.00,
			1.25, 1.50, 1.75, 2.00, 2.50, 
			3.00, 3.50, 4.00, 4.50, 5.00
		],
		## X
		[ 	0.01, 0.02, 0.04, 0.07, 0.10,
			0.20, 0.25, 0.35, 0.40, 0.45, 
			0.50, 0.60, 0.70, 0.80, 1.00,
			1.25, 1.50, 1.75, 2.00, 2.50, 
			3.00, 3.50, 4.00, 4.50, 5.00
		],
		## Angle
		[ 	1.4908, 1.4287, 1.4307, 1.4377, 1.4876, 
			1.5072, 1.4933, 1.4894, 1.789910608, 0.00,
			4.50, 5.62, 7.50, 10.0, 12.5,
			15.0, 20.0, 25.0, 30.0, 35.0, 
			40.0, 45.0, 50.0, 55.5, 60.0
		]
	],
	[
		## Z
		[ 	25.4 * 0.001, 25.4 * 0.002, 25.4 * 0.005, 25.4 * 0.010, 25.4 * 0.020,
			25.4 / 64, 25.4 / 56, 25.4 / 48, 25.4 / 44, 25.4 / 40, 
			25.4 / 36, 25.4 / 32, 25.4 / 28, 25.4 / 24, 25.4 / 20, 
			25.4 / 18, 25.4 / 16, 25.4 / 14, 25.4 / 12, 25.4 / 11, 
			25.4 / 10, 25.4 /  9, 25.4 /  8, 25.4 /  7, 25.4 /  6
		],
		## X
		[ 	25.4 * 0.001, 25.4 * 0.002, 25.4 * 0.005, 25.4 * 0.010, 25.4 * 0.020,
			25.4 / 64, 25.4 / 56, 25.4 / 48, 25.4 / 44, 25.4 / 40, 
			25.4 / 36, 25.4 / 32, 25.4 / 28, 25.4 / 24, 25.4 / 20, 
			25.4 / 18, 25.4 / 16, 25.4 / 14, 25.4 / 12, 25.4 / 11, 
			25.4 / 10, 25.4 /  9, 25.4 /  8, 25.4 /  7, 25.4 /  6
		],
		## Angle
		[ 	1.4908, 1.4287, 1.4307, 1.4377, 1.4876, 
			1.5072, 1.4933, 1.4894, 1.789910608, 0.00,
			4.50, 5.62, 7.50, 10.0, 12.5,
			15.0, 20.0, 25.0, 30.0, 35.0, 
			40.0, 45.0, 50.0, 55.5, 60.0
		]
	]
]
		
LATHE_VALUES_LABELS = [
	[
		## Z
		[ 	"0.01", "0.02", "0.04", "0.07", "0.10",
			"0.20", "0.25", "0.35", "0.40", "0.45", 
			"0.50", "0.60", "0.70", "0.80", "1.00",
			"1.25", "1.50", "1.75", "2.00", "2.50", 
			"3.00", "3.50", "4.00", "4.50", "5.00"
		],
		## X
		[ 	"0.01", "0.02", "0.04", "0.07", "0.10",
			"0.20", "0.25", "0.35", "0.40", "0.45", 
			"0.50", "0.60", "0.70", "0.80", "1.00",
			"1.25", "1.50", "1.75", "2.00", "2.50", 
			"3.00", "3.50", "4.00", "4.50", "5.00"
		],
		## Angle
		[ 	"MT#0", "MT#1", "MT#2", "MT#3", "MT#4",
			"MT#5", "MT#6", "MT#7", "NPT ", "	", 
			"4.50", "5.62", "7.50", "10.0", "12.5",
			"15.0", "20.0", "25.0", "30.0", "35.0", 
			"40.0", "45.0", "50.0", "55.5", "60.0"
		]
	],
	[
		## Z
		[ 	".001", ".002", ".005", ".010", ".020",
			"64tpi", "56tpi", "48tpi", "44tpi", "40tpi", 
			"36tpi", "32tpi", "28tpi", "24tpi", "20tpi", 
			"18tpi", "16tpi", "14tpi", "12tpi", "11tpi", 
			"10tpi", "9tpi",  "8tpi",  "7tpi",  "6tpi"
		],
		## X
		[ 	".001", ".002", ".005", ".010", ".020",
			"64tpi", "56tpi", "48tpi", "44tpi", "40tpi", 
			"36tpi", "32tpi", "28tpi", "24tpi", "20tpi", 
			"18tpi", "16tpi", "14tpi", "12tpi", "11tpi", 
			"10tpi", "9tpi",  "8tpi",  "7tpi",  "6tpi"
		],
		## Angle
		[ 	"MT#0", "MT#1", "MT#2", "MT#3", "MT#4",
			"MT#5", "MT#6", "MT#7", "NPT ", "	", 
			"4.50", "5.62", "7.50", "10.0", "12.5",
			"15.0", "20.0", "25.0", "30.0", "35.0", 
			"40.0", "45.0", "50.0", "55.5", "60.0"
		]
	]
]

#####################################
# **** PRIVATE CONSTANT SECTION **** #
#####################################

# constant strings
BUTTON_EXIT = "button_exit"
BUTTON_STOP = "button_stop"
BUTTON_IDLE = "button_idle"
BUTTON_REVERSE = "button_reverse"
BUTTON_UNIT = "button_unit"
BUTTON_UP = "button_up"
BUTTON_DOWN = "button_down"
BUTTON_LEFT = "button_left"
BUTTON_RIGHT = "button_right"
MOVE_TYPE_TAB = "move_type_tab"
Z_AXIS_COORD = "z_axis_coord"
X_AXIS_COORD = "x_axis_coord"
A_AXIS_ANGLE = "a_axis_angle"
Z_AXIS_ZERO = "z_axis_zero"
X_AXIS_ZERO = "x_axis_zero"
A_AXIS_ZERO = "a_axis_zero"
R_RPM_VALUE = "r_rpm_value"

############################
# **** IMPORT SECTION **** #
############################

import sys
import os
import linuxcnc
import hal
import math
import time

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QPushButton, QTabWidget, QLabel

from qtvcp.widgets.mdi_line import MDILine as MDI_WIDGET
from qtvcp.widgets.gcode_editor import GcodeEditor as GCODE
from qtvcp.lib.keybindings import Keylookup
from qtvcp.core import Status, Action

# Set up logging
from qtvcp import logger
LOG = logger.getLogger(__name__)

# Set the log level for this module
#LOG.setLevel(logger.INFO) # One of DEBUG, INFO, WARNING, ERROR, CRITICAL

###########################################
# **** INSTANTIATE LIBRARIES SECTION **** #
###########################################

KEYBIND = Keylookup()
STATUS = Status()
ACTION = Action()

###################################
# **** HANDLER CLASS SECTION **** #
###################################

class HandlerClass:
	########################
	# **** INITIALIZE **** #
	########################
	# widgets allows access to  widgets from the qtvcp files
	# at this point the widgets and hal pins are not instantiated
	def __init__(self, halcomp,widgets,paths):
		self.hal = halcomp
		self.w = widgets
		self.PATHS = paths

	##########################################
	# SPECIAL FUNCTIONS SECTION	    	  #
	##########################################

	# at this point:
	# the widgets are instantiated.
	# the HAL pins are built but HAL is not set ready
	# This is where you make HAL pins or initialize state of widgets etc
	def initialized__(self):
		self.setup_lathe_ui_hal()
		self.setup_ui_map()
		self.setup_initial_parameters()
		self.setup_initial_ui_state()
		self.setup_ui_signals()
		self.disable_enable_move_buttons()
		self.hal.ready()
		self.setup_timer()

	########################
	# CALLBACKS FROM STATUS #
	########################


	#######################
	# HELPER FUNCTIONS	#
	#######################

	def setup_timer(self):
		self.timer = QTimer()
		self.timer.timeout.connect(self.timer_fired)
		self.timer.setInterval(25)
		self.timer.start()

	def timer_fired(self):
		if (self.br_time > 0):
			velocity = (time.time() - self.br_time) * 3
			velocity = min(velocity, 6.0)
			self.hal_pin_velocity_z_cmd.set(+velocity);
		if (self.bl_time > 0):
			velocity = (time.time() - self.bl_time) * 3
			velocity = min(velocity, 6.0)
			self.hal_pin_velocity_z_cmd.set(-velocity);
		if (self.bu_time > 0):
			velocity = (time.time() - self.bu_time) * 3
			velocity = min(velocity, 3.0)
			self.hal_pin_velocity_x_cmd.set(+velocity);
		if (self.bd_time > 0):
			velocity = (time.time() - self.bd_time) * 3
			velocity = min(velocity, 3.0)
			self.hal_pin_velocity_x_cmd.set(-velocity);
		pos_z = self.hal_pin_position_z.get() - self.z_axis_zero_offset
		pos_x = self.hal_pin_position_x.get() - self.x_axis_zero_offset
		pos_a = ((self.hal_pin_position_a.get() - self.a_axis_zero_offset) % 1.0) * 360.0;
		# This is ridiculous but leading zero formatting of floating point numbers is broken in PyQt
		if self.lathe_unit == 0:
			pos_z_str = "{0:s}{1:04d}.{2:03d}mm".format("+" if pos_z >= 0 else "-",int(abs(pos_z)),int((abs(pos_z)%1)*1000))
			pos_x_str = "{0:s}{1:04d}.{2:03d}mm".format("+" if pos_x <= 0 else "-",int(abs(pos_x)),int((abs(pos_x)%1)*1000))
		if self.lathe_unit == 1:
			pos_z_str = "{0:s}{1:03d}.{2:04d}in".format("+" if pos_z >= 0 else "-",int(abs(pos_z)),int((abs(pos_z)%1)*10000))
			pos_x_str = "{0:s}{1:03d}.{2:04d}in".format("+" if pos_x <= 0 else "-",int(abs(pos_x)),int((abs(pos_x)%1)*10000))
		pos_a_str = "{0:03d}.{1:02d}deg".format(abs(int(pos_a)), abs(int((pos_a%1)*100)))
		r_rpm = self.hal_pin_speed_rps.get() * 60
		r_rpm_str = "{0:04d}rpm".format(int(r_rpm))
		self.widget_map[Z_AXIS_COORD].setText(pos_z_str)
		self.widget_map[X_AXIS_COORD].setText(pos_x_str)
		self.widget_map[A_AXIS_ANGLE].setText(pos_a_str)
		self.widget_map[R_RPM_VALUE].setText(r_rpm_str)

	def setup_lathe_ui_hal(self):
		self.hal = hal.component("lathe_ui")
		self.hal_pin_position_z = self.hal.newpin("position_z", hal.HAL_FLOAT, hal.HAL_IN)
		self.hal_pin_position_x = self.hal.newpin("position_x", hal.HAL_FLOAT, hal.HAL_IN)
		self.hal_pin_position_a = self.hal.newpin("position_a", hal.HAL_FLOAT, hal.HAL_IN)
		self.hal_pin_speed_rps = self.hal.newpin("speed_rps", hal.HAL_FLOAT, hal.HAL_IN)
		self.hal_pin_forward_z = self.hal.newpin("forward_z", hal.HAL_FLOAT, hal.HAL_OUT)
		self.hal_pin_forward_x = self.hal.newpin("forward_x", hal.HAL_FLOAT, hal.HAL_OUT)
		self.hal_pin_enable_z = self.hal.newpin("enable_z", hal.HAL_BIT, hal.HAL_OUT)
		self.hal_pin_enable_x = self.hal.newpin("enable_x", hal.HAL_BIT, hal.HAL_OUT)
		self.hal_pin_enable_stepper_z = self.hal.newpin("enable_stepper_z", hal.HAL_BIT, hal.HAL_OUT)
		self.hal_pin_enable_stepper_x = self.hal.newpin("enable_stepper_x", hal.HAL_BIT, hal.HAL_OUT)
		self.hal_pin_offset_z_encoder = self.hal.newpin("offset_z_encoder", hal.HAL_FLOAT, hal.HAL_OUT)
		self.hal_pin_offset_z_stepper = self.hal.newpin("offset_z_stepper", hal.HAL_FLOAT, hal.HAL_OUT)
		self.hal_pin_offset_x_encoder = self.hal.newpin("offset_x_encoder", hal.HAL_FLOAT, hal.HAL_OUT)
		self.hal_pin_offset_x_stepper = self.hal.newpin("offset_x_stepper", hal.HAL_FLOAT, hal.HAL_OUT)
		self.hal_pin_control_z_type = self.hal.newpin("control_z_type", hal.HAL_BIT, hal.HAL_OUT)
		self.hal_pin_control_x_type = self.hal.newpin("control_x_type", hal.HAL_BIT, hal.HAL_OUT)
		self.hal_pin_velocity_z_cmd = self.hal.newpin("velocity_z_cmd", hal.HAL_FLOAT, hal.HAL_OUT)
		self.hal_pin_velocity_x_cmd = self.hal.newpin("velocity_x_cmd", hal.HAL_FLOAT, hal.HAL_OUT)

	def update_lathe_ui_hal(self):
		if self.lathe_stop:
			self.hal_pin_enable_stepper_z.set(False)
			self.hal_pin_enable_stepper_x.set(False)
		else:
			self.hal_pin_enable_stepper_z.set(True)
			self.hal_pin_enable_stepper_x.set(True)
		self.hal_pin_offset_z_encoder.set(-self.hal_pin_position_a.get())
		self.hal_pin_offset_x_encoder.set(-self.hal_pin_position_a.get())
		self.hal_pin_offset_z_stepper.set(+self.hal_pin_position_z.get())
		self.hal_pin_offset_x_stepper.set(+self.hal_pin_position_x.get())
		self.hal_pin_forward_z.set(self.lathe_forward_z);
		if (self.lathe_forward_x == 0) or (self.lathe_idle == True):
			self.hal_pin_enable_x.set(False)
		else:
			self.hal_pin_enable_x.set(True)
		self.hal_pin_forward_x.set(self.lathe_forward_x);
		if (self.lathe_forward_z == 0) or (self.lathe_idle == True):
			self.hal_pin_enable_z.set(False)
		else:
			self.hal_pin_enable_z.set(True)
	
	def setup_ui_map(self):
		self.widget_map = {}
		for i in list(range(25)):
			self.widget_map["value_0_{:02d}".format(i)] = self.w.findChild(QPushButton, "value_0_{:02d}".format(i))
		for i in list(range(25)):
			self.widget_map["value_1_{:02d}".format(i)] = self.w.findChild(QPushButton, "value_1_{:02d}".format(i))
		for i in list(range(25)):
			self.widget_map["value_2_{:02d}".format(i)] = self.w.findChild(QPushButton, "value_2_{:02d}".format(i))
		self.widget_map[BUTTON_EXIT] = self.w.findChild(QPushButton, BUTTON_EXIT)
		self.widget_map[BUTTON_STOP] = self.w.findChild(QPushButton, BUTTON_STOP)
		self.widget_map[BUTTON_IDLE] = self.w.findChild(QPushButton, BUTTON_IDLE)
		self.widget_map[BUTTON_REVERSE] = self.w.findChild(QPushButton, BUTTON_REVERSE)
		self.widget_map[BUTTON_UNIT] = self.w.findChild(QPushButton, BUTTON_UNIT)
		self.widget_map[BUTTON_LEFT] = self.w.findChild(QPushButton, BUTTON_LEFT)
		self.widget_map[BUTTON_RIGHT] = self.w.findChild(QPushButton, BUTTON_RIGHT)
		self.widget_map[BUTTON_UP] = self.w.findChild(QPushButton, BUTTON_UP)
		self.widget_map[BUTTON_DOWN] = self.w.findChild(QPushButton, BUTTON_DOWN)
		self.widget_map[MOVE_TYPE_TAB] = self.w.findChild(QTabWidget, MOVE_TYPE_TAB)
		self.widget_map[Z_AXIS_COORD] = self.w.findChild(QLabel, Z_AXIS_COORD)
		self.widget_map[X_AXIS_COORD] = self.w.findChild(QLabel, X_AXIS_COORD)
		self.widget_map[A_AXIS_ANGLE] = self.w.findChild(QLabel, A_AXIS_ANGLE)
		self.widget_map[Z_AXIS_ZERO] = self.w.findChild(QPushButton, Z_AXIS_ZERO)
		self.widget_map[X_AXIS_ZERO] = self.w.findChild(QPushButton, X_AXIS_ZERO)
		self.widget_map[A_AXIS_ZERO] = self.w.findChild(QPushButton, A_AXIS_ZERO)
		self.widget_map[R_RPM_VALUE] = self.w.findChild(QLabel, R_RPM_VALUE)

	def setup_ui_signals(self):
		self.widget_map[BUTTON_EXIT].clicked.connect(self.button_exit_clicked)
		self.widget_map[BUTTON_UNIT].clicked.connect(self.button_unit_clicked)
		self.widget_map[BUTTON_LEFT].pressed.connect(self.button_left_pressed)
		self.widget_map[BUTTON_LEFT].released.connect(self.button_left_released)
		self.widget_map[BUTTON_RIGHT].pressed.connect(self.button_right_pressed)
		self.widget_map[BUTTON_RIGHT].released.connect(self.button_right_released)
		self.widget_map[BUTTON_UP].pressed.connect(self.button_up_pressed)
		self.widget_map[BUTTON_UP].released.connect(self.button_up_released)
		self.widget_map[BUTTON_DOWN].pressed.connect(self.button_down_pressed)
		self.widget_map[BUTTON_DOWN].released.connect(self.button_down_released)
		self.widget_map[BUTTON_STOP].toggled.connect(self.button_stop)
		self.widget_map[BUTTON_IDLE].toggled.connect(self.button_idle)
		self.widget_map[BUTTON_REVERSE].toggled.connect(self.button_reverse)
		self.widget_map[MOVE_TYPE_TAB].currentChanged.connect(self.move_type_changed)
		self.widget_map[Z_AXIS_ZERO].clicked.connect(self.z_axis_zero_clicked)
		self.widget_map[X_AXIS_ZERO].clicked.connect(self.x_axis_zero_clicked)
		self.widget_map[A_AXIS_ZERO].clicked.connect(self.a_axis_zero_clicked)
		for i in list(range(25)):
			self.widget_map["value_0_{:02d}".format(i)].toggled.connect(getattr(self, "value_0_{:02d}".format(i)))
		for i in list(range(25)):
			self.widget_map["value_1_{:02d}".format(i)].toggled.connect(getattr(self, "value_1_{:02d}".format(i)))
		for i in list(range(25)):
			self.widget_map["value_2_{:02d}".format(i)].toggled.connect(getattr(self, "value_2_{:02d}".format(i)))

	def stop_now(self):
		widget = self.widget_map[BUTTON_STOP]
		widget.blockSignals(True)
		widget.setChecked(True)
		widget.blockSignals(False)
		self.lathe_stop = True
		self.disable_enable_move_buttons()
		self.update_lathe_ui_hal()

	def run_now(self):
		self.engage_now()
		widget = self.widget_map[BUTTON_STOP]
		widget.blockSignals(True)
		widget.setChecked(False)
		widget.blockSignals(False)
		self.lathe_stop = False
		self.disable_enable_move_buttons()
		self.update_lathe_ui_hal()

	def idle_now(self):
		self.stop_now()
		widget = self.widget_map[BUTTON_IDLE]
		widget.blockSignals(True)
		widget.setChecked(True)
		widget.blockSignals(False)
		self.lathe_idle = True
		self.disable_enable_move_buttons()
		self.update_lathe_ui_hal()

	def engage_now(self):
		widget = self.widget_map[BUTTON_IDLE]
		widget.blockSignals(True)
		widget.setChecked(False)
		widget.blockSignals(False)
		self.lathe_idle = False
		self.disable_enable_move_buttons()
		self.update_lathe_ui_hal()

	def forward(self):
		widget = self.widget_map[BUTTON_REVERSE]
		widget.blockSignals(True)
		widget.setChecked(False)
		widget.blockSignals(False)
		self.lathe_reverse = False
		self.setup_machine_parameters()
		self.update_lathe_ui_hal()

	def reverse(self):
		widget = self.widget_map[BUTTON_REVERSE]
		widget.blockSignals(True)
		widget.setChecked(True)
		widget.blockSignals(False)
		self.lathe_reverse = True
		self.setup_machine_parameters()
		self.update_lathe_ui_hal()

	def setup_initial_parameters(self):
		self.br_time = 0;
		self.bl_time = 0;
		self.bu_time = 0;
		self.bd_time = 0;
		self.z_axis_zero_offset = 0
		self.x_axis_zero_offset = 0
		self.a_axis_zero_offset = 0
		self.lathe_idle = True
		self.lathe_stop = True
		self.lathe_reverse = False
		self.lathe_forward_z = 0
		self.lathe_forward_x = 0
		self.lathe_mode = 0
		self.lathe_unit = 0
		self.idle_now()
		self.lathe_param_selection = [
			[4, 3, 8],
			[4, 3, 8]
		]
		self.setup_machine_parameters()
	
	def setup_machine_parameters(self):
		self.lathe_forward_z = 0
		self.lathe_forward_x = 0
		if self.lathe_mode == 0:
			self.lathe_forward_z = abs(LATHE_VALUES[self.lathe_unit][0][self.lathe_param_selection[self.lathe_unit][0]])
			self.lathe_forward_x = 0
		if self.lathe_mode == 1:
			self.lathe_forward_z = 0
			self.lathe_forward_x = -abs(LATHE_VALUES[self.lathe_unit][1][self.lathe_param_selection[self.lathe_unit][1]])
		if self.lathe_mode == 2:
			self.lathe_forward_z = abs(LATHE_VALUES[self.lathe_unit][0][self.lathe_param_selection[self.lathe_unit][0]])
			self.lathe_forward_x = self.lathe_forward_z * math.tan(math.radians(LATHE_VALUES[self.lathe_unit][2][self.lathe_param_selection[self.lathe_unit][2]]))
		if self.lathe_reverse == False:
			self.lathe_forward_z = -(self.lathe_forward_z)
			self.lathe_forward_x = -(self.lathe_forward_x)
		self.update_lathe_ui_hal()

	def setup_parameters_for_selection(self, page, which):
		self.lathe_param_selection[self.lathe_unit][page] = which
		self.setup_machine_parameters()

	def setup_initial_ui_state(self):
		self.populate_labels()
		self.widget_map[MOVE_TYPE_TAB].setCurrentIndex(self.lathe_mode);
		self.set_checked_for_page_0(self.lathe_param_selection[self.lathe_unit][0])
		self.set_checked_for_page_1(self.lathe_param_selection[self.lathe_unit][1])
		self.set_checked_for_page_2(self.lathe_param_selection[self.lathe_unit][2])

	def disable_enable_move_buttons(self):
		if self.lathe_mode == 0 and not self.lathe_idle and self.lathe_stop:
			self.widget_map[BUTTON_LEFT].setEnabled(True)
			self.widget_map[BUTTON_RIGHT].setEnabled(True)
		else:
			self.widget_map[BUTTON_LEFT].setEnabled(False)
			self.widget_map[BUTTON_RIGHT].setEnabled(False)
		if self.lathe_mode == 1 and not self.lathe_idle and self.lathe_stop:
			self.widget_map[BUTTON_UP].setEnabled(True)
			self.widget_map[BUTTON_DOWN].setEnabled(True)
		else:
			self.widget_map[BUTTON_UP].setEnabled(False)
			self.widget_map[BUTTON_DOWN].setEnabled(False)
		if self.lathe_mode == 2 and not self.lathe_idle and self.lathe_stop:
			self.widget_map[BUTTON_UP].setEnabled(True)
			self.widget_map[BUTTON_DOWN].setEnabled(True)
			self.widget_map[BUTTON_LEFT].setEnabled(True)
			self.widget_map[BUTTON_RIGHT].setEnabled(True)		
	
	def populate_labels(self):
		for i in list(range(25)):
			widget = self.widget_map["value_0_{:02d}".format(i)]
			widget.blockSignals(True)
			widget.setText(LATHE_VALUES_LABELS[self.lathe_unit][0][i])
			widget.blockSignals(False)
		for i in list(range(25)):
			widget = self.widget_map["value_1_{:02d}".format(i)]
			widget.blockSignals(True)
			widget.setText(LATHE_VALUES_LABELS[self.lathe_unit][1][i])
			widget.blockSignals(False)
		for i in list(range(25)):
			widget = self.widget_map["value_2_{:02d}".format(i)]
			widget.blockSignals(True)
			widget.setText(LATHE_VALUES_LABELS[self.lathe_unit][2][i])
			widget.blockSignals(False)

	def set_checked_for_page_0(self, which):
		for i in list(range(25)):
			widget = self.widget_map["value_0_{:02d}".format(i)]
			widget.blockSignals(True)
			if i != which:
				if widget.isChecked():
					widget.setChecked(False)
			else:
				if not widget.isChecked():
					widget.setChecked(True)
			widget.blockSignals(False)

	def set_checked_for_page_1(self, which):
		for i in list(range(25)):
			widget = self.widget_map["value_1_{:02d}".format(i)]
			widget.blockSignals(True)
			if i != which:
				if widget.isChecked():
					widget.setChecked(False)
			else:
				if not widget.isChecked():
					widget.setChecked(True)
			widget.blockSignals(False)
   
   	def set_checked_for_page_2(self, which):
		for i in list(range(25)):
			widget = self.widget_map["value_2_{:02d}".format(i)]
			widget.blockSignals(True)
			if i != which:
				if widget.isChecked():
					widget.setChecked(False)
			else:
				if not widget.isChecked():
					widget.setChecked(True)
			widget.blockSignals(False)

	#######################
	# CALLBACKS FROM FORM #
	#######################
	
	def move_type_changed(self, which):
		self.stop_now()
		self.lathe_mode = which
		self.disable_enable_move_buttons()
		self.setup_machine_parameters()

	def button_stop(self, state):
		if state:
			self.stop_now()
		else:
			self.run_now()
			
	def button_idle(self, state):
		if state:
			self.idle_now()
		else:
			self.engage_now()

	def button_reverse(self, state):
		if state:
			self.reverse()
		else:
			self.forward()
	
	def z_axis_zero_clicked(self):
		self.z_axis_zero_offset = self.hal_pin_position_z.get();

	def x_axis_zero_clicked(self):
		self.x_axis_zero_offset = self.hal_pin_position_x.get();

	def a_axis_zero_clicked(self):
		self.a_axis_zero_offset = self.hal_pin_position_a.get();

	def button_exit_clicked(self):
		self.idle_now()
		self.w.close()

	def button_unit_clicked(self):
		self.stop_now()
		self.lathe_unit ^= 1;
		button = self.widget_map["button_unit"]
		if self.lathe_unit == 0:
			button.setText("mm")
		if self.lathe_unit == 1:
			button.setText("in")
		self.populate_labels()
		self.setup_machine_parameters()

	def button_left_pressed(self):
		if self.lathe_mode == 1:
			return
		if not self.lathe_stop or self.lathe_idle:
			return
		self.bl_time = time.time();
		self.hal_pin_enable_stepper_z.set(True)
		self.hal_pin_control_z_type.set(1)
		self.hal_pin_velocity_z_cmd.set(0)

	def button_left_released(self):
		if self.lathe_mode == 1:
			return
		self.bl_time = 0;
		self.hal_pin_velocity_z_cmd.set(0)
		self.hal_pin_control_z_type.set(0)
		self.hal_pin_enable_stepper_z.set(False)

	def button_right_pressed(self):
		if self.lathe_mode == 1:
			return
		if not self.lathe_stop or self.lathe_idle:
			return
		self.br_time = time.time();
		self.hal_pin_enable_stepper_z.set(True)
		self.hal_pin_control_z_type.set(1)
		self.hal_pin_velocity_z_cmd.set(0);

	def button_right_released(self):
		if self.lathe_mode == 1:
			return
		self.br_time = 0;
		self.hal_pin_velocity_z_cmd.set(0)
		self.hal_pin_control_z_type.set(0)
		self.hal_pin_enable_stepper_z.set(False)

	def button_up_pressed(self):
		if self.lathe_mode == 0:
			return
		if not self.lathe_stop or self.lathe_idle:
			return
		self.bu_time = time.time();
		self.hal_pin_enable_stepper_x.set(True)
		if self.lathe_mode != 1:
			self.hal_pin_enable_x.set(True)
		self.hal_pin_control_x_type.set(1)
		self.hal_pin_velocity_x_cmd.set(0);

	def button_up_released(self):
		if self.lathe_mode == 0:
			return
		self.bu_time = 0;
		self.hal_pin_velocity_x_cmd.set(0);
		self.hal_pin_control_x_type.set(0)
		if self.lathe_mode != 1:
			self.hal_pin_enable_x.set(False)
		self.hal_pin_enable_stepper_x.set(False)

	def button_down_pressed(self):
		if self.lathe_mode == 0:
			return
		if not self.lathe_stop or self.lathe_idle:
			return
		self.bd_time = time.time();
		self.hal_pin_enable_stepper_x.set(True)
		self.hal_pin_control_x_type.set(1)
		self.hal_pin_velocity_x_cmd.set(0);

	def button_down_released(self):
		if self.lathe_mode == 0:
			return
		self.bd_time = 0;
		self.hal_pin_velocity_x_cmd.set(0);
		self.hal_pin_control_x_type.set(0)
		self.hal_pin_enable_stepper_x.set(False)
		
	def value_0_00(self, state):
		self.set_checked_for_page_0(0)
		self.setup_parameters_for_selection(0,0)
		
	def value_0_01(self, state):
		self.set_checked_for_page_0(1)
		self.setup_parameters_for_selection(0,1)
		
	def value_0_02(self, state):
		self.set_checked_for_page_0(2)
		self.setup_parameters_for_selection(0,2)
		
	def value_0_03(self, state):
		self.set_checked_for_page_0(3)
		self.setup_parameters_for_selection(0,3)
		
	def value_0_04(self, state):
		self.set_checked_for_page_0(4)
		self.setup_parameters_for_selection(0,4)
		
	def value_0_05(self, state):
		self.set_checked_for_page_0(5)
		self.setup_parameters_for_selection(0,5)
		
	def value_0_06(self, state):
		self.set_checked_for_page_0(6)
		self.setup_parameters_for_selection(0,5)
		
	def value_0_07(self, state):
		self.set_checked_for_page_0(7)
		self.setup_parameters_for_selection(0,7)
		
	def value_0_08(self, state):
		self.set_checked_for_page_0(8)
		self.setup_parameters_for_selection(0,8)
		
	def value_0_09(self, state):
		self.set_checked_for_page_0(9)
		self.setup_parameters_for_selection(0,9)
		
	def value_0_10(self, state):
		self.set_checked_for_page_0(10)
		self.setup_parameters_for_selection(0,10)
		
	def value_0_11(self, state):
		self.set_checked_for_page_0(11)
		self.setup_parameters_for_selection(0,11)
		
	def value_0_12(self, state):
		self.set_checked_for_page_0(12)
		self.setup_parameters_for_selection(0,12)
		
	def value_0_13(self, state):
		self.set_checked_for_page_0(13)
		self.setup_parameters_for_selection(0,13)
		
	def value_0_14(self, state):
		self.set_checked_for_page_0(14)
		self.setup_parameters_for_selection(0,14)
		
	def value_0_15(self, state):
		self.set_checked_for_page_0(15)
		self.setup_parameters_for_selection(0,15)
		
	def value_0_16(self, state):
		self.set_checked_for_page_0(16)
		self.setup_parameters_for_selection(0,16)
		
	def value_0_17(self, state):
		self.set_checked_for_page_0(17)
		self.setup_parameters_for_selection(0,17)
		
	def value_0_18(self, state):
		self.set_checked_for_page_0(18)
		self.setup_parameters_for_selection(0,18)
		
	def value_0_19(self, state):
		self.set_checked_for_page_0(19)
		self.setup_parameters_for_selection(0,19)
		
	def value_0_20(self, state):
		self.set_checked_for_page_0(20)
		self.setup_parameters_for_selection(0,20)
		
	def value_0_21(self, state):
		self.set_checked_for_page_0(21)
		self.setup_parameters_for_selection(0,21)
		
	def value_0_22(self, state):
		self.set_checked_for_page_0(22)
		self.setup_parameters_for_selection(0,22)
		
	def value_0_23(self, state):
		self.set_checked_for_page_0(23)
		self.setup_parameters_for_selection(0,23)
		
	def value_0_24(self, state):
		self.set_checked_for_page_0(24)
		self.setup_parameters_for_selection(0,24)

	def value_1_00(self, state):
		self.set_checked_for_page_1(0)
		self.setup_parameters_for_selection(1,0)
		
	def value_1_01(self, state):
		self.set_checked_for_page_1(1)
		self.setup_parameters_for_selection(1,1)
		
	def value_1_02(self, state):
		self.set_checked_for_page_1(2)
		self.setup_parameters_for_selection(1,2)
		
	def value_1_03(self, state):
		self.set_checked_for_page_1(3)
		self.setup_parameters_for_selection(1,3)
		
	def value_1_04(self, state):
		self.set_checked_for_page_1(4)
		self.setup_parameters_for_selection(1,4)
		
	def value_1_05(self, state):
		self.set_checked_for_page_1(5)
		self.setup_parameters_for_selection(1,5)
		
	def value_1_06(self, state):
		self.set_checked_for_page_1(6)
		self.setup_parameters_for_selection(1,6)
		
	def value_1_07(self, state):
		self.set_checked_for_page_1(7)
		self.setup_parameters_for_selection(1,7)
		
	def value_1_08(self, state):
		self.set_checked_for_page_1(8)
		self.setup_parameters_for_selection(1,8)
		
	def value_1_09(self, state):
		self.set_checked_for_page_1(9)
		self.setup_parameters_for_selection(1,9)
		
	def value_1_10(self, state):
		self.set_checked_for_page_1(10)
		self.setup_parameters_for_selection(1,10)
		
	def value_1_11(self, state):
		self.set_checked_for_page_1(11)
		self.setup_parameters_for_selection(1,11)
		
	def value_1_12(self, state):
		self.set_checked_for_page_1(12)
		self.setup_parameters_for_selection(1,12)
		
	def value_1_13(self, state):
		self.set_checked_for_page_1(13)
		self.setup_parameters_for_selection(1,13)
		
	def value_1_14(self, state):
		self.set_checked_for_page_1(14)
		self.setup_parameters_for_selection(1,14)
		
	def value_1_15(self, state):
		self.set_checked_for_page_1(15)
		self.setup_parameters_for_selection(1,15)
		
	def value_1_16(self, state):
		self.set_checked_for_page_1(16)
		self.setup_parameters_for_selection(1,16)
		
	def value_1_17(self, state):
		self.set_checked_for_page_1(17)
		self.setup_parameters_for_selection(1,17)
		
	def value_1_18(self, state):
		self.set_checked_for_page_1(18)
		self.setup_parameters_for_selection(1,18)
		
	def value_1_19(self, state):
		self.set_checked_for_page_1(19)
		self.setup_parameters_for_selection(1,19)
		
	def value_1_20(self, state):
		self.set_checked_for_page_1(20)
		self.setup_parameters_for_selection(1,20)
		
	def value_1_21(self, state):
		self.set_checked_for_page_1(21)
		self.setup_parameters_for_selection(1,21)
		
	def value_1_22(self, state):
		self.set_checked_for_page_1(22)
		self.setup_parameters_for_selection(1,22)
		
	def value_1_23(self, state):
		self.set_checked_for_page_1(23)
		self.setup_parameters_for_selection(1,23)
		
	def value_1_24(self, state):
		self.set_checked_for_page_1(24)
		self.setup_parameters_for_selection(1,24)
	
	def value_2_00(self, state):
		self.set_checked_for_page_2(0)
		self.setup_parameters_for_selection(2,0)
		
	def value_2_01(self, state):
		self.set_checked_for_page_2(1)
		self.setup_parameters_for_selection(2,1)
		
	def value_2_02(self, state):
		self.set_checked_for_page_2(2)
		self.setup_parameters_for_selection(2,2)
		
	def value_2_03(self, state):
		self.set_checked_for_page_2(3)
		self.setup_parameters_for_selection(2,3)
		
	def value_2_04(self, state):
		self.set_checked_for_page_2(4)
		self.setup_parameters_for_selection(2,4)
		
	def value_2_05(self, state):
		self.set_checked_for_page_2(5)
		self.setup_parameters_for_selection(2,5)
		
	def value_2_06(self, state):
		self.set_checked_for_page_2(6)
		self.setup_parameters_for_selection(2,6)
		
	def value_2_07(self, state):
		self.set_checked_for_page_2(7)
		self.setup_parameters_for_selection(2,7)
		
	def value_2_08(self, state):
		self.set_checked_for_page_2(8)
		self.setup_parameters_for_selection(2,8)
		
	def value_2_09(self, state):
		self.set_checked_for_page_2(9)
		self.setup_parameters_for_selection(2,9)
		
	def value_2_10(self, state):
		self.set_checked_for_page_2(10)
		self.setup_parameters_for_selection(2,10)
		
	def value_2_11(self, state):
		self.set_checked_for_page_2(11)
		self.setup_parameters_for_selection(2,11)
		
	def value_2_12(self, state):
		self.set_checked_for_page_2(12)
		self.setup_parameters_for_selection(2,12)
		
	def value_2_13(self, state):
		self.set_checked_for_page_2(13)
		self.setup_parameters_for_selection(2,13)
		
	def value_2_14(self, state):
		self.set_checked_for_page_2(14)
		self.setup_parameters_for_selection(2,14)
		
	def value_2_15(self, state):
		self.set_checked_for_page_2(15)
		self.setup_parameters_for_selection(2,15)
		
	def value_2_16(self, state):
		self.set_checked_for_page_2(16)
		self.setup_parameters_for_selection(2,16)
		
	def value_2_17(self, state):
		self.set_checked_for_page_2(17)
		self.setup_parameters_for_selection(2,17)
		
	def value_2_18(self, state):
		self.set_checked_for_page_2(18)
		self.setup_parameters_for_selection(2,18)
		
	def value_2_19(self, state):
		self.set_checked_for_page_2(19)
		self.setup_parameters_for_selection(2,19)
		
	def value_2_20(self, state):
		self.set_checked_for_page_2(20)
		self.setup_parameters_for_selection(2,20)
		
	def value_2_21(self, state):
		self.set_checked_for_page_2(21)
		self.setup_parameters_for_selection(2,21)
		
	def value_2_22(self, state):
		self.set_checked_for_page_2(22)
		self.setup_parameters_for_selection(2,22)
		
	def value_2_23(self, state):
		self.set_checked_for_page_2(23)
		self.setup_parameters_for_selection(2,23)
		
	def value_2_24(self, state):
		self.set_checked_for_page_2(24)
		self.setup_parameters_for_selection(2,24)

	#####################
	# GENERAL FUNCTIONS #
	#####################

	#####################
	# KEY BINDING CALLS #
	#####################

	###########################
	# **** closing event **** #
	###########################

	##############################
	# required class boiler code #
	##############################

	def __getitem__(self, item):
		return getattr(self, item)
	def __setitem__(self, item, value):
		return setattr(self, item, value)

################################
# required handler boiler code #
################################

def get_handlers(halcomp,widgets,paths):
	 return [HandlerClass(halcomp,widgets,paths)]
