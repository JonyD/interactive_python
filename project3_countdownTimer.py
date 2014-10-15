# template for "Stopwatch: The Game"
# Import modules
import simplegui
import random

# define global variables
tenths_of_sec = 0
nr_success_stops = 0
nr_total_stops = 0
str_stops = ""
status = "init"

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    min = t // 600
    sec = (t-(600*min)) // 10
    cent_sec = (t-(600*min)) % 10
    if sec<10 :
        sec_str= "0"+str(sec)
        final_str = str(min)+":"+sec_str+"."+str(cent_sec)
    else:
        final_str = str(min)+":"+str(sec)+"."+str(cent_sec)
    return str(final_str)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global status
    status = "started"
    timer.start()

def stop():
    global status
    if status == "started":
        status = "stopped"
        timer.stop()
        increment_nr_total_stops()
        if is_stop_in_full_second():
            increment_nr_success_stops()
        format_str_stops()
   
def reset():
    global status
    status = "resetted"
    timer.stop()
    reset_times()
    format_str_stops()
##################################################
# helper functions

def reset_times():
    global tenths_of_sec
    global nr_total_stops
    global nr_success_stops
    tenths_of_sec = 0
    nr_total_stops = 0
    nr_success_stops = 0

##    
def increment_nr_total_stops():
    global nr_total_stops
    nr_total_stops = nr_total_stops + 1
##
def increment_nr_success_stops():
    global nr_success_stops
    nr_success_stops = nr_success_stops + 1
##    
def format_str_stops():
    global str_stops
    str_stops = str(nr_success_stops) +"/"+ str(nr_total_stops)
##
def is_stop_in_full_second():
    if tenths_of_sec % 10 == 0:
        return True
    else:
        return False
    
###################################################  

    
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global tenths_of_sec
    tenths_of_sec = tenths_of_sec + 1


# define draw handler time
def draw(canvas):
    canvas.draw_text(format(tenths_of_sec), [150,100], 30, "White")
    #global str_stops
    format_str_stops()
    canvas.draw_text(str_stops, [200,40], 30, "Green")

    
# create frame
frame = simplegui.create_frame("Home", 300, 200)
#buttons
frame.add_button("Start", start)
frame.add_button("Stop", stop)
frame.add_button("Reset", reset)

# register event handlers
frame.set_draw_handler(draw)


# start frame
frame.start()

#define timer
timer = simplegui.create_timer(100, timer_handler)


# Please remember to review the grading rubric

