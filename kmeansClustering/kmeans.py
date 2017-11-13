# Learning Machines, Assignment 2
# kmeans Clustering
# Fall 2017, ITP NYU
# Stephanie Koltun

# Instructions
# cmd line: 

import sys
import random
import matplotlib.pyplot as plt
import math

xextent = int(sys.argv[1])		# user input to define X extent
yextent = int(sys.argv[2])		# user input to define Y extent
k = int(sys.argv[3])	# number of clusters
numpoints = int(sys.argv[4])	# number of points to split into clusters

# these are the points
pointslist = [[],[],[]]
xcoords = pointslist[0]
ycoords = pointslist[1]
ptclust = pointslist[2]


# these are the cluster centers
# centroids[i] = [x,y]
centroids = []

# these are the points for each cluster
clusters = []
colors = ["r","g","b"]	


# generate list of points and randomly place centers
def initializePointsAndClusters():
	iterate = 0

	for cluster in range(k):
		# get a random coord for each cluster's center
		center = generateCoord(xextent, yextent)
		center.append(colors[iterate])
		centroids.append(center)
		iterate += 1

		# append empty list for each cluster
		clusters.append([[],[]])

	for point in range(numpoints):
		thispoint = generateCoord(xextent, yextent)
		# add this point to the list
		xcoords.append(thispoint[0])
		ycoords.append(thispoint[1])

		# assign random centroid
		randcenter = random.randint(0,(k-1))
		ptclust.append(randcenter)

	
# generate random coord
def generateCoord(xext, yext):
	# generate a random x position between 0 and extent
	# rather than use random, I could weight this to make sure the clusters
	# are pretty distinct
	x = random.randint(0,xext)
	y = random.randint(0,yext)
	coord = [x,y]

	return coord

def assign():
	changedAnyPoint = False

	for p in range(numpoints):
		changedPoint = False
		point = [xcoords[p],ycoords[p]]
		# initialize shortest distance as the furthest place
		curClust = int(ptclust[p])
		nearestCenter = centroids[curClust]
		curDist = calcDist(point,nearestCenter)
		
		# find the distance to every centroid
		for center in centroids:
			dist = calcDist(point,center)
			#print "d: " + str(dist) + " prev: " + str(curDist)
			if dist < curDist:
				# reassign 
				curDist = dist
				ptclust[p] = centroids.index(center) # change current clust num
				changedPoint = True
				
				
		if changedPoint == True:
			changedAnyPoint = True
			print "reassigned point"
		else:
			print "point " + str(p) + " okay"

	# should this keep going?
	if changedAnyPoint == True:
		# move centroid
		print "keep checking"
		averageCentroid()	# adjust centroid
		assign()			# run function again
	else:
		print "clusters are done!"
		return True

def averageCentroid():


def plotIt():
	# plot the individual points
	for p in range(numpoints):
		plt.scatter(xcoords[p], ycoords[p], s=15, c=colors[ptclust[p]])
	# plot the centeroids
	for center in centroids:
		plt.scatter(center[0], center[1], s= 50, c=center[2])
	plt.show()

def calcDist(point,center):
	x1 = point[0]
	y1 = point[1]
	x2 = center[0]
	y2 = center[1]

	dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
	return dist


# run it!
initializePointsAndClusters()
print "points: "
print pointslist
print "centers: "
print centroids
done = assign()
print done
plotIt()


