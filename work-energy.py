import matplotlib.pyplot as plot

class Object:
    def __init__(self,mass,pos,vel,acc,force):
        self.mass = mass
        self.pos = pos
        self.vel = vel
        self.acc = acc
        self.force = force

o1 = Object(5,0,-6,-12/5,-12)
xPos = []
time = []

timer = 0.0
while timer <= 1 and o1.pos < 5:
    timer += 0.00000001
    o1.force = -12 + 0.3*o1.pos*o1.pos
    o1.acc = o1.force/o1.mass
    o1.vel += o1.acc*timer
    o1.pos += o1.vel*timer + (1/2)*o1.acc*timer*timer
    xPos.append(o1.pos)
    time.append(timer)
    print(o1.pos,o1.vel,o1.acc)

filteredxList = xPos[::1000]
filteredtList = time[::1000]

plot.plot(filteredtList,filteredxList)
plot.show()

