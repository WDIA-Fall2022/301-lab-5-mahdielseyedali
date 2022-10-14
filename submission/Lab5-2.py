from sense_hat import SenseHat
s = SenseHat()
r = (250,128,114)
G = (0, 100, 0)
R = (255, 0, 0)
b = (0, 0, 255)
DB = (0, 0, 255)
LB = (50, 250, 50)
LG = (0, 255, 0)
n = (0, 0, 0)



def displayColorOfTemperature():
    temp = float(s.get_temperature())
    return temp

for i in range(64):
    if -10 >= displayColorOfTemperature() >= -40:
        s.clear(DB)
    if 0 >= displayColorOfTemperature() > -10:
        s.clear(LB)
    if 15 >= displayColorOfTemperature() > 0:
        s.clear(LG)
    if 22 >= displayColorOfTemperature() > 15:
        s.clear(G)
    if displayColorOfTemperature() > 22:
        s.clear(R)
print("Temperature %s C" % displayColorOfTemperature())

#input version
def displayColorOfTemperature(y):
    t = float(y)
    return t

while True:
    try:
        turnOn = float(input("What is the temperature: "))
        if -10 >= displayColorOfTemperature(turnOn) >= -40:
            s.clear(DB)
        if 0 >= displayColorOfTemperature(turnOn) > -10:
            s.clear(LB)
        if 15 >= displayColorOfTemperature(turnOn) > 0:
            s.clear(LG)
        if 22 >= displayColorOfTemperature(turnOn) > 15:
            s.clear(G)
        if displayColorOfTemperature(turnOn) > 22:
            s.clear(R)
    except ValueError:
        print("Error")











########################################

def LedsOnForHumidity():
    h = int(s.get_humidity())
    return h

v = 64 * LedsOnForHumidity() / 100
pixels = [range if i < v else n for i in range(64)]

s.set_pixels(pixels)
print("Humidity %s %" % LedsOnForHumidity())

# input version
def LedsOnForHumidity(y):
  x = int(64 * y/100)
  return x

while True:
    try:
        h = int(input("Number of Humidity is "))
        if 0 < h <= 100:
            lightsOn = LedsOnForHumidity(h)
            pixels = []
            for i in range(64):
                if i < lightsOn:
                    pixels.append(r)
                else:
                    pixels.append(n)
            s.set_pixels(pixels)
        else:
            print("Number must be between 0 and 100. Please try again")
    except ValueError:
        print("Please try again")
