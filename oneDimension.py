# This Python file uses the following encoding: utf-8
### 这段代码模拟了一维随机游走过程，完整运行这段代码后会绘制三个统计图，对应报告的图1 2 3
import random
import matplotlib.pyplot as plt

def randomWalk(nsteps):# 输入随机游走总步数，返回最终坐标
	x = 0
	for i in range(nsteps):
		x += (random.randint(1,2) - 1.5) * 2
	return x

sumX = 0 
sumXabs = 0
averageX = []
averageDist = []
for i in range(100000):
	x = randomWalk(100)
	sumX += x
	sumXabs += abs(x)
	averageX.append(sumX * 1.0 / (i + 1))
	averageDist.append(sumXabs * 1.0 / (i + 1))

plt.xlabel('Times')
plt.ylabel('average X')
plt.plot(averageX)
plt.show()

plt.xlabel('Times')
plt.ylabel('average Distance')
plt.plot(averageDist)
plt.show()

distlList = []
sumDist = 0
for i in range(100):
	sumDist = 0
	for j in range(40000):
		x = randomWalk(i)
		sumDist += abs(x)
		if j == 39999:
			distlList.append(sumDist * 1.0 / (j+1))

plt.xlabel('total steps')
plt.ylabel('average Distance')
plt.plot(distlList)
plt.show()