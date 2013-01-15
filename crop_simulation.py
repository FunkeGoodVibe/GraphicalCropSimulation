from PyQt4.QtCore import *
from PyQt4.QtGui import *

from radio_button_widget import * #provides the radio button widget

import sys

class CropWindow(QMainWindow):
	"""this class creates a main window to observe the growth of a simulated crop"""

	#constructor
	def __init__(self):
		super().__init__() #call super class constructor
		self.setWindowTitle("Crop Simulator") #set window title

	def create_select_crop_layout(self):
		#this is the initial layout of the window - to select the crop type

		self.crop_radio_buttons = RadioButtonWidget("Crop Simulation","Please select a crop",("Wheat","Potato")) #create crop selector 
		self.instantiate_button = QPushButton('Create Crop')

		#create layout to hold the widgets
		self.initial_layout = QVBoxLayout()
		self.initial_layout.addWidget(self.crop_radio_buttons)
		self.initial_layout.addWidget(self.instantiate_button)

		#create a widget to display the layout
		self.select_crop_widget = QWidget()
		self.select_crop_widget.setLayout(self.initial_layout)

		#connections
		self.instantiate_button.clicked.connect(self.instantiate_crop)

def main():
	crop_simulation = QApplication(sys.argv) #create new application
	crop_window = CropWindow() #create new instance of main window
	crop_window.show() #make instance visible
	crop_window.raise_() #raise instance to top of window stack
	crop_simulation.exec_() #monitor application for events


if __name__ == "__main__":
	main()