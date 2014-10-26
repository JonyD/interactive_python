# implementation of card game - Memory

import simplegui
import random



# define lists
turns = 0
list_a = range(1,9)
list_b = range(1,9)
list_c = list_a + list_b
list_cx = random.shuffle(list_c)



card_already_guessed = [False]*16
clicked_card_index_A = -1
clicked_card_index_B = -1
clicks = 0


# helper function to initialize globals

def reset():

    global reset_activated,clicked_card_index_A,clicked_card_index_B,clicks,card_already_guessed
    card_already_guessed = [False]*16
    clicked_card_index_A = -1
    clicked_card_index_B = -1
    clicks = 0
    list_cx = random.shuffle(list_c)
    new_game()
    frame.start()
    print str(list_c)


def new_game():
    update_turns_label( True )


def update_turns_label(new_game):
    global turns
    if new_game:
        turns = 0
    else:
        turns+=1
    label.set_text("Turns = "+ str(turns))
#-----------------------------------------

def validate_pairs( A, B):
    global clicked_card_index_B
    if A != -1:
        print "Clicked_A:"+ str(list_c[A])
        if B != -1:
            print "Clicked_B:"+ str(list_c[B])
            if B != A:                     #ignore same cards
                update_turns_label(False)  #increment turns

                if (list_c[B] == list_c[A]):
                    print "MATCH!!!!"
                    card_already_guessed[A] = True
                    card_already_guessed[B] = True
                    clicked_card_index_B = -1
        print "----"
    pass
#-----------------------------------------     
# define event handlers
def mouseclick(pos):
    global clicked_card_index, clicked_card_index_A, clicked_card_index_B
    global clicks,list_c
    
    clicked_card_index = pos[0]//50
    print "clicked:tuple_c[" + str(clicked_card_index)+"]"

    if not card_already_guessed[clicked_card_index]: #ignore already guessed ones
        if clicks == 0: #1st card
            clicked_card_index_A = clicked_card_index

            
        elif clicks == 1: #2nd card
            clicked_card_index_B = clicked_card_index
            validate_pairs(clicked_card_index_A,clicked_card_index_B)
            
        clicks+=1
        if clicks == 2: #3rd click -> reset clicks
            clicks = 0
        

        #print "A:"+str(clicked_card_index_A)
        #print "B:"+str(clicked_card_index_B)
        #clicked_card_index_B = -1

#-----------------------------------------       
# cards are logically 50x100 pixels in size    
def draw(canvas):
        global list_cx
        x_coordinate = 0
        exposed_index=0
        for item in list_c:
            pos = [x_coordinate, 80]
            if card_already_guessed[exposed_index] or clicked_card_index_A == exposed_index or clicked_card_index_B == exposed_index:
                canvas.draw_text( str(item), pos, 100, 'White' )
            else:
                canvas.draw_polygon([(x_coordinate,0), (x_coordinate, 100), (x_coordinate+50, 100),(x_coordinate+50, 0)], 1, 'Red', 'Green')
            x_coordinate+=50
            exposed_index+=1
        

#-----------------------------------------
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", reset)
label = frame.add_label("Turns = "+ str(turns))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
print str(list_c)
# Always remember to review the grading rubric