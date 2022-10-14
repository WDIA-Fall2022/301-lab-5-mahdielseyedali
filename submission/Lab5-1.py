
from sense_hat import SenseHat
import random

s = SenseHat()
c = (233,150,122)
n = (0, 0, 0)

def rollAdice(y):
    x = random.randint(1, y)
    return x

    while True:
        try:
            dice = int(input("how many faces for this dice? (1 to 64)"))
            if 0 < dice < 65:
                numOfdice = rollAdice(dice)
                test = []
                for i in range(64):
                    if i < numOfdice:
                        test.append(c)
                    else:
                        test.append(n)
                s.set_pixels(test)
            else:
                print("Number must be in between 1 and 64. Please try again!")
        except ValueError:
            print("Number must be in between 1 and 64. Please try again!")
