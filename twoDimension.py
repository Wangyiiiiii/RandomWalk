# This Python file uses the following encoding: utf-8
### 这段代码模拟了二维随机游走过程，完整运行这段代码后会绘制四个统计图，对应报告的图1 2 3
import random
import matplotlib.pyplot as plt
import numpy as np

def randomWalk(nsteps):#输入模拟步数，返回(x,y)
	(x,y) = (0,0)
	for i in range(nsteps):
		randomDecision = random.randint(1,4)
		if randomDecision == 1:
			x += 1
		elif randomDecision == 2:
			x -= 1
		elif randomDecision == 3:
			y += 1
		else:
			y -= 1
	return (x,y)

(sumX,sumY) = (0,0)
averageXY = []
sumDist = 0
averageDist = []

for i in range(100000):
	(x,y) = randomWalk(100)
	sumX += x
	sumY += y
	sumDist += x*x + y*y
	averageXY.append((sumX*1.0/(i+1),sumY*1.0/(i+1))) 
	averageDist.append(sumDist*1.0/(i+1))

averageXY = np.array(averageXY) #转换成numpy数组方便处理

plt.xlabel('Times')
plt.ylabel('average X')
plt.plot(averageXY[:,0])
plt.show()

plt.xlabel('Times')
plt.ylabel('average Y')
plt.plot(averageXY[:,1])
plt.show()

plt.xlabel('Times')
plt.ylabel('average x^2+y^2')
plt.plot(averageDist)
plt.show()

distlList = []
sumDist = 0
for i in range(100):
	sumDist = 0
	for j in range(40000):
		(x,y) = randomWalk(i)
		sumDist += x*x + y*y
		if j == 39999:
			distlList.append(sumDist * 1.0 / (j+1))

plt.xlabel('total steps')
plt.ylabel('average x^2+y^2')
plt.plot(distlList)
plt.show()