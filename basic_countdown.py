import digit_handling_functions as dh


x = 0
while x < 80:
    dh.iterate_digit_down(0)
    dh.output()
    x = x + 1
    dh.time.sleep(1)
