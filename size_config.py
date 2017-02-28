from utility import *
screen_width, screen_height = get_resolution()

main_window_width = screen_width/2
main_window_height = screen_height/2
position_x = screen_width/2 - main_window_width/2
position_y = screen_height/2 - main_window_height/2
main_window_geometry = str(main_window_width) + "x" + str(main_window_height) + "+" + str(position_x) + "+" + str(position_y)

control_frame_width = main_window_width/2
control_frame_height = main_window_height

listbox1_width = control_frame_width/3
listbox1_height = control_frame_width/2
listbox1_x = control_frame_width/9
listbox1_y = 50
listbox2_x = listbox1_width + listbox1_x*2

radiobutton1_x = 0
radiobutton1_y = listbox1_y + listbox1_height + 30
radiobutton1_width = control_frame_width
radiobutton2_y = listbox1_y + listbox1_height + 60

button_width = 100
button_x = control_frame_width/2 - button_width/2
button_y = control_frame_height - 50
