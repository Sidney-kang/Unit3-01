#Created by : Sidney Kang
#Created on : 5 Oct. 2017
#Created for : ICS3UR
# Daily Assignment - Unit3-01
# This program shows how to use an if statement

import ui

NUMBER_COMPUTER_IS_THINKING_ABOUT = 5

def check_number_touch_up_inside(sender):
    #This checks the number of students entered versus the constant (25 stuents)
    
    #input
    number_entered = int(view['input_of_number_textbox'].text)
    
    #process
    if number_entered == NUMBER_COMPUTER_IS_THINKING_ABOUT:
    	 #output
    	 view['check_answer_label'].text = "Correct!!!"
    
view = ui.load_view()
view.present('sheet')
