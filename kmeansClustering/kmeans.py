# Learning Machines, Assignment 2
# kmeans Clustering
# Fall 2017, ITP NYU
# Stephanie Koltun

# Instructions
# cmd line: python kmeans.py [x-extent] [y-extent] [number of clusters] [number of datapoints]
# the first two arguments are used to create a set of random points

import sys
import random
import matplotlib.pyplot as plt
import math

# assign user inputs
xextent = int(sys.argv[1])		# user input to define X extent
yextent = int(sys.argv[2])		# user input to define Y extent
k = int(sys.argv[3])			# number of clusters - max 7 because of colors
numpoints = int(sys.argv[4])	# number of points to split into clusters

# these are the points - make empty lists for keeping track
pointslist = [[],[],[]]
xcoords = pointslist[0]
ycoords = pointslist[1]
ptclust = pointslist[2]

# these are the cluster centers
# centroids[i] = [x,y]
centroids = []

# these are the points for each cluster
clusters = []
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']	


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
		clusters.append([])

	for point in range(numpoints):
		# get random point
		thispoint = generateCoord(xextent, yextent)
		# add this point to the list
		xcoords.append(thispoint[0])
		ycoords.append(thispoint[1])

		# assign random centroid to the point
		randcluster = random.randint(0,(k-1))
		ptclust.append(randcluster)
		
	


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
			print "reassigned point " + str(p)

	# should this keep going?
	if changedAnyPoint == True:
		print "keep checking"
		averageCentroid()	# adjust centroid
		assign()			# run assignment function again
	else:
		print "clusters are done!"
		groupPoints()		# should do another version where there are subplots
							# for each assignment, and points are grouped at every round
		

def averageCentroid():
	for cluster in range(k):
		pointsincluster = 0
		sumvector = [0,0]

		# add up all the vectors that are part of this cluster
		for p in range(numpoints):
			# is this point part of that cluster?
			if (ptclust[p] == cluster):
				# add this vector
				sumvector[0] += xcoords[p]
				sumvector[1] += ycoords[p]
				pointsincluster += 1

		# divide vector by number of points in this cluster
		newx = sumvector[0]/pointsincluster
		newy = sumvector[1]/pointsincluster
		print "new center for " + str(cluster)
		print newx,newy
		# replace old centroid in list
		centroids[cluster][0] = newx
		centroids[cluster][1] = newy

def groupPoints():
	# should make another version that groups the points each time
	# and uses subplots to show each assignment iteration
	for cluster in range(k):
		# find matching points
		for p in range(numpoints):
			# is this point part of that cluster?
			if (ptclust[p] == cluster):
				point = [xcoords[p], ycoords[p]]
				# finally assign the point to the appropriate cluster
				clusters[cluster].append(point)
		print "cluster " + str(cluster) + ", centroid: " + str(centroids[cluster][0]) + "," + str(centroids[cluster][1])
		print clusters[cluster]

def plotIt():
	# plot the individual points
	for p in range(numpoints):
		plt.scatter(xcoords[p], ycoords[p], s=15, c=colors[ptclust[p]])
	# plot the centeroids
	for center in centroids:
		plt.scatter(center[0], center[1], s=50, c=center[2])
	plt.show()


# ----- HELPER FUNCTIONS BELOW

# generate random coord
def generateCoord(xext, yext):
	# generate a random position between 0 and extent
	# rather than use random, I could weight this to make sure the clusters
	# are pretty distinct
	x = random.randint(0,xext)
	y = random.randint(0,yext)
	coord = [x,y]

	return coord

# calculate distance between two points
def calcDist(point1,point2):
	x1 = point1[0]
	y1 = point1[1]
	x2 = point2[0]
	y2 = point2[1]

	dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
	return dist


# run it!
initializePointsAndClusters()
print "points: "
print pointslist
print "centers: "
print centroids
assign()
plotIt()


