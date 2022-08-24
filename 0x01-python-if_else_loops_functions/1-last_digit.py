#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = int(repr(number)[-1])
    last_digit = last_digit*(-1)
else:
    last_digit = int(repr(number)[-1])
# comparing
<<<<<<< HEAD
if last_digit < 6:
    text = " less than 6 and not 0"
elif last_digit > 5:
    text = " greather than 5"
else:
    text = " 0"
=======
if last_digit == 0:
    text = " 0"
elif last_digit > 5:
    text = " greater than 5"
else:
    text = " less than 6 and not 0"
>>>>>>> 6f2b21ff6cab5af28771d14081faf1e096f7c4ec
print("Last digit of {} is {} and is{}".format(number, last_digit, text))
