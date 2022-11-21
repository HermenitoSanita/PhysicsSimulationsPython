import matplotlib.pyplot as plot

xPos = 0
vel = 0
acc = 0
k = 23
force =   k * (5.6-xPos)
timer = 0

posArray = []
velArray = []
accArray = []
timeArray = []

while timer < 1 and len(posArray) < 300000:
    xPos += vel*timer + (acc/2)*timer*timer
    vel += acc*timer
    acc = force/50
    force = k * (5.6 - xPos)
    timer += 0.000000001

    posArray.append(xPos)
    velArray.append(vel)
    accArray.append(acc)
    timeArray.append(timer)
    print(xPos,vel,acc,timer)

filteredX = posArray[::10]
filteredV = velArray[::10]
filteredA = accArray[::10]
filteredT = timeArray[::10]

plot.plot(filteredT,filteredX)
plot.plot(filteredT,filteredV)
plot.plot(filteredT,filteredA)
plot.legend(["POS","VEL","ACC"])
plot.show()

