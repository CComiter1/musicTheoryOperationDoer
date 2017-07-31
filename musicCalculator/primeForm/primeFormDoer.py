notes = [['c', 'C', 'b#', 'B#', 'h#', 'H#'], ['db', 'Db', 'c#', 'C#'], 
['d', 'D'], ['eb', 'Eb', 'd#', 'D#'], ['fb', 'Fb', 'E', 'e'],
 ['f', 'F', 'e#', 'E#'], ['gb', 'Gb', 'f#', 'F#'], ['g', 'G'], 
 ['g#', 'G#', 'ab', 'Ab'], ['a', 'A'], ['bb', 'Bb', 'a#', 'A#', 'hb', 'Hb'], 
 ['cb', 'Cb', 'b', 'B', 'h', 'H']]

def translate(letterNote):
	for x in notes:
		if letterNote in x:
			return notes.index(x)

def revTranslate(numNote):
	return notes[numNote][1]

def noteConverter(letterChord):
	numChord = []
	for x in letterChord:
		numChord.append(translate(x))
	return numChord

def revNoteConverter(numChord):
	letterChord = []
	for x in numChord:
		letterChord.append(revTranslate(x))
	return letterChord

def subLister(bigList, smallList):
	affectedList = []
	for x in bigList:
		if x in smallList:
			smallList.remove(x)
		else:
			affectedList.append(x)
	return affectedList

def modConverter(n):
	while n < 0:
		n += 12
	while n > 11:
		n -= 12
	if n in range(12):
		return n

def boundFinder(correctChord):
	if (len(correctChord) == 2) or (len(correctChord) == 1):
		return correctChord
	else:
		possibles, theTrueMinimum = [], []
		for y in correctChord:
			for z in correctChord:
				valid = []
				emptyPillow = (range(modConverter(z - y + 1)))
				for x in range(len(emptyPillow)):
					emptyPillow[x] = modConverter(emptyPillow[x] + y)
				for q in correctChord:
					if q in emptyPillow:
						valid.append(1)
					else:
						valid.append(-1)
				sum = 0
				for r in valid:
					sum += r
				if (len(correctChord)) == sum:
					possibles.append([y, z])
		for x in possibles:
			if (len(theTrueMinimum)) == 0:
				theTrueMinimum = x
			else:
				if modConverter(x[1] - x[0]) < modConverter(theTrueMinimum[1] - theTrueMinimum[0]):
					theTrueMinimum = x
		return theTrueMinimum

def primeFormFinder(theChord):
	thatWhichIsReturned = [0] * len(theChord)
	theBounds = boundFinder(theChord)
	theOtherBounds = theBounds
	theMax, theMin = theBounds[1], theBounds[0]
	thatWhichIsReturned[0], thatWhichIsReturned[len(theChord) - 1] = theBounds[0], theBounds[1]
	counter, possibleMagicNumber = 0, 0
	newChord = subLister(theChord, theOtherBounds)
	while counter < len(theChord)/2:
		if counter != 0: 
			newChord = subLister(newChord, newBounds)
		newBounds = boundFinder(newChord)
		if len(newBounds) != 0:
			if len(newBounds) == 1:
				possibleMagicNumber = newChord[0]
			else:
				if modConverter(theMax - newBounds[1]) > modConverter(theMax - newBounds[0]):
					newBounds.reverse()
				thatWhichIsReturned[counter + 1] = newBounds[0]
				thatWhichIsReturned[len(theChord) - counter - 2] = newBounds[1]
		counter += 1
	if (len(theChord) % 2) == 1:
		thatWhichIsReturned[len(theChord)/2] = possibleMagicNumber
	if modConverter(thatWhichIsReturned[1] - theMin) <= modConverter(thatWhichIsReturned[len(theChord) - 1] - thatWhichIsReturned[len(theChord) - 2]):
		for x in range(len(theChord)):
			thatWhichIsReturned[x] = modConverter(thatWhichIsReturned[x] - theMin)
	else:
		thatWhichIsReturned.reverse()
		for x in range(len(theChord)):
			thatWhichIsReturned[x] = modConverter(theMax - thatWhichIsReturned[x])
	return thatWhichIsReturned


def primeFormLaunch(notes):
	return primeFormFinder(noteConverter(notes.split(" ")))


#tester Code
#for x in notes:
#	for y in notes:
#		for z in notes:
#			for t in notes:
#				print("%s %s" %([x[0], y[0], z[0], t[0]], primeFormFinder(noteConverter([x[0], y[0], z[0], t[0]]))))

