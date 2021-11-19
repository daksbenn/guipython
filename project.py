"""
* Libraries to install:
    sudo pip3 install guizero
* you need a pic named hacker.png in the folder assets/ in the same folder where the code is located.

"""

from guizero import App, Text, Picture      #Import the guizero library with App, Text and Picture.
from guizero.PushButton import PushButton   #Import the pushbutton for creating a button in the gui.
import subprocess                           #Import subprocess for executing system cammands.
import os                                   #Import os library for os cammands 
from random import choice                   #Import Ramdom library for selecting from lists.

app = App("Wanted!")    #App title
msg = Text(app, text="The Anonymous Hacker is...\n") #The text in the field.

#*****Text Styling Part******#
app.bg = "black"          #The background colour.
app.text_size = 20          #Text size.
app.text_color = "white"     #Text colour.
app.font = "Liberation Serif"    #Font Style.
#*****Styling End************#

#*****Button Area************#
#def name():
#    name = subprocess.check_output("notify-send 'it works'", shell=True)
#    print('\tThe Super Secret Name is elliot!!')

def choose_name():
    #print("Button was pressed")    
    first_names = ["Barbara", "Woody", "Tiberius", "Smokey", "Jennifer", "Ruby", "Elliot"]
    last_names = ["Spindleshanks", "Mysterioso", "Dungeon", "Catseye", "Darkmeyer", "Flamingobreath"]
    spy_name = choice(first_names) +" "+choice(last_names)
    print(spy_name)
    name.value = spy_name

button =PushButton(app, choose_name, text="Tell me!")
name =Text(app, text="")
#*****Button End*************#
#*****Picture Area***********#
pic = Picture(app, image='hacker.png')
#*****Picture End************#

app.display()               #This starts the display with the above code in it.
