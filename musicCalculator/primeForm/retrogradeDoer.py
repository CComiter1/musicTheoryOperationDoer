def retrogradeLaunch(notes):
	notes = notes.split(" ")[::-1]

	notes = [str(x) for x in notes]

	return notes