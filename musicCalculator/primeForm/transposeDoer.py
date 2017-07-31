from primeFormDoer import noteConverter, revNoteConverter, modConverter 

def transposeFinder(theChord, num):
	clToFinArr = noteConverter(theChord)
	for x in range(len(theChord)):
		clToFinArr[x] = modConverter(int(num) + clToFinArr[x])
	return revNoteConverter(clToFinArr)

def theTransposer(notes, num):
	return transposeFinder(notes.split(" "), int(num))