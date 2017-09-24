#Created by : Sidney Kang
#Created on : 5 Oct. 2017
#Created for : ICS3UR
# Daily Assignment - Unit3-01
# This program shows how to use an if statement

import ui

max_number_of_students = 25

def check_number_of_students_touch_up_inside(sender):
    #This checks the number of students entered versus the constant (25 stuents)
    
    #input
    number_entered = int(view['input_of_number_of_students_textbox'].text)
    
    #process
    if number_entered > max_number_of_students:
    	 #output
    	 view['too_many_students_label'].text = "There are too many students."
    
view = ui.load_view()
view.present('sheet')
