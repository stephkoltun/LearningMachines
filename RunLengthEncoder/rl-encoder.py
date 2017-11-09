# encode a string
def encode (string):
	code=[]
	count=0			#track sequential instances of the same letter
	letterIt=1 		#letter iterator - only way I could figure out how to deal with the last character in the string
	prevletter=''	#letter for comparing through the loop

	for letter in string:
		#if it's the first letter, assign it as the previous
		if letterIt == 1:
			prevletter=letter

		#check if this letter is the same or different than the pevious
		if letter == prevletter:
			#keep counting
			count+=1
		else:
			# it's different
			# deal with the previous letter: add count and previous to list
			pair = (count,prevletter)
			code.append(pair)
			# reset count and assign new previous letter
			count = 1

		##if it's the last letter, make sure it gets added
		if letterIt == len(string):
			pair = (count,letter)
			code.append(pair)

		prevletter=letter
		letterIt+=1

	return code

# generate random string
def generateString ():
	characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','q','r','s','t','u','v','w','x','y','z']
	genstr = ''

	import random

	for i in range(12):
		thischar = random.choice(characters)
		amount = random.randint(1,6)
		for num in range(amount):
			genstr += thischar
	return genstr


inputstr = generateString()
print "original string: " + inputstr 
print "encoded: "
print encode(inputstr)