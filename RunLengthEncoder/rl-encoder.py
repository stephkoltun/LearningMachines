def encode (string):
	print("input string: " + string)
	code=[]
	count=1
	curletter=''
	prevletter=''
	for letter in string:
		#check if this letter is the same or different than the pevious
		if letter == prevletter:
			count++
		else:
			# it's different
			# deal with the previous letter: add count and previous to list
			pair = (count,prevletter)
			code.append(pair)
			# reset count and assign new previous letter
			count = 1
			prevletter=letter
	return code

print encode("aaaaahhhhhhmmmmmmmuiiiiiiiaaaaaa")
