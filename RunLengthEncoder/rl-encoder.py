import sys
import random

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

# generate random string with the argument being number of potentially different characters
def generateString (num):
	characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','q','r','s','t','u','v','w','x','y','z']
	genstr = ''

	for i in range(num):
		# pick a random character from the character list
		thischar = random.choice(characters)
		# pick a random number between 1 and 6
		amount = random.randint(1,6)
		genstr += thischar*amount

	return genstr

# decode
def decode (code):
	string = ''

	# use each pair in the code
	for count, letter in code:
		# add the number of letter instances to the string
		string += letter * count

	return string



inputstr = generateString(int(sys.argv[1])) # use 1st argument from command to determine length
print "original string: "
print inputstr 
print "encoded: "
encoded = encode(inputstr)
print encoded
print "decoded: "
decoded = decode(encoded)
print decoded