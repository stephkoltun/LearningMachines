# Learning Machines, Assignment 2
# kmeans Clustering
# Fall 2017, ITP NYU
# Stephanie Koltun

# Instructions
# cmd line: 

import sys
import random
import matplotlib.pyplot as plt

xextent = int(sys.argv[1])		# user input to define X extent
yextent = int(sys.argv[2])		# user input to define Y extent
k = int(sys.argv[3])	# number of clusters
numpoints = int(sys.argv[4])	# number of points to split into clusters

# these are the points
pointslist = [[],[]]
xcoords = pointslist[0]
ycoords = pointslist[1]


# these are the cluster centers
# centroids[i] = [x,y]
centroids = []

# these are the points for each cluster
clusters = []	


# generate list of points and randomly place centers
def initializePointsAndClusters():
	for point in range(numpoints):
		thispoint = generateCoord(xextent, yextent)
		# add this point to the list
		xcoords.append(thispoint[0])
		ycoords.append(thispoint[1])

	for cluster in range(k):
		# get a random coord for each cluster's center
		center = generateCoord(xextent, yextent)
		centroids.append(center)

		# append empty list for each cluster
		clusters.append([[],[]])	
	
# generate random coord
def generateCoord(xext, yext):
	# generate a random x position between 0 and extent
	# rather than use random, I could weight this to make sure the clusters
	# are pretty distinct
	x = random.randint(0,xext)
	y = random.randint(0,yext)
	coord = [x,y]

	return coord

def assignFirstCluster():
	# for each point
	for point in pointslist:
		# initialize shortest distance as the furthest place
		shortestDist = sqrt((yextent)**2 + (yextent)**2)
		nearestClust = 0
		# find the distance to every cluster-center
		for center in prevcenters:
			dist = calcDist(point,center)
			if dist < shortestDist:
				# reassign 
				shortestDist = dist
				point[2] = prevcenters.index(center)	# add cluster val to point
				nearestClust = prevcenters.index(center)
				prevclusters[prevcenters.index(center)].append(point)

def plotIt():
	# plot the individual points
	plt.scatter(xcoords, ycoords, c="g")
	# plot the centeroids
	for center in centroids:

	plt.show()

# def calcDist(point,center):
# 	x1 = point[0]
# 	y1 = point[1]
# 	x2 = center[0]
# 	y2 = center[1]

# 	dist = sqrt((x2-x1)**2 + (y2-y1)**2)
# 	return dist


# run it!
initializePointsAndClusters()
print "points: "
print pointslist
print "centers: "
print prevcenters
plotIt()


