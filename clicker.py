import sys
from PyQt5.QtWidgets import *

# application variables
width, height = 600, 600 # main window width, height

app = QApplication(sys.argv) # declare app

# User screen dimensions
screen_resolution = app.desktop().screenGeometry()
s_width, s_height = screen_resolution.width(), screen_resolution.height()

window = QWidget() # declare main window

# Start application in middle of the users screen:
window.setGeometry((s_width/2)-(width/2), (s_height/2)-(height/2), width, height) #x, y, w, h

window.setWindowTitle("Click Counter") # main window title

window.setFixedSize(window.size()) #set fixed window size
window.show() # display main window

loops = 0
def change_button_text():
    global loops
    global btn
    loops += 1
    btn.setText("Clicked: " + str(loops) + " time(s)!")

# button - start #
btn = QPushButton("Click me!", window) # create and attach button to main window
btn.clicked.connect(change_button_text) # link click event to function
btn_width, btn_height = 150, 150 # button width and height
btn.resize(btn_width,btn_height) # set button size
btn.move((width/2)-(btn_width/2),(height/2)-(btn_height/2)) # position button to center of main window
btn.show() # display button
# button - end #

app.exec_() # keep application open
