import time
import tm1637

time_file_path = "time_file.txt"

digits = [0, 4, 9, 0]       #this is the time digits in reverse order.
                            #Thus, the time is actually digits[3]digits[2]:digits[1]digits[0]

max_digits = [9, 5, 9, 9]   #The maximum that each digit can get to is usually 9.  Except for the
                            #tens of minutes, which maxes out at 60 sec

#function to iterate a digit up.  It is actually recursive, and takes care of carrying to the next place
def iterate_digit_up(i):
    if digits[i] < max_digits[i]:
        digits[i] = digits[i]+1
    else:
       digits[i] = 0
       iterate_digit_up(i+1)

#function to iterate the digit down
def iterate_digit_down(i):
    if digits[i] > 0:
        digits[i] = digits[i]-1
    else:
       digits[i] = max_digits[i]
       iterate_digit_down(i+1)

#function to refresh the time on the display
def output():
    # /// Uncomment the following line out for terminal testing without 7-segment display
    time_file = open(time_file_path, "w")
    new_time_str = str(digits[3]) + str(digits[2]) + ':' + str(digits[1]) + str(digits[0])
    time_file.write(new_time_str)
    time_file.close()
    print(new_time_str)
    display = tm1637.TM1637(CLK=5, DIO=6, brightness=1.0)
    display.ShowDoublepoint(True)
    display.Show([digits[3], digits[2], digits[1], digits[0]])
