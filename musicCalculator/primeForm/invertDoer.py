from primeFormDoer import noteConverter, revNoteConverter, modConverter 

def invertFinder(theChord, num):
	clToFinArr = noteConverter(theChord)
	for x in range(len(theChord)):
		clToFinArr[x] = modConverter(int(num) - clToFinArr[x])
	return revNoteConverter(clToFinArr)

def theInverter(notes, num):
	return invertFinder(notes.split(" "), int(num))
