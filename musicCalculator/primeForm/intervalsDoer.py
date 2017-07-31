from primeFormDoer import primeFormLaunch

def singPlur(n):
	if n == 1:
		return "instance"
	else:
		return "instances"

def intervalsLaunch(notes):
	baseForThis = intervalsFinder(notes)
	finalResult = []
	for x in range(len(baseForThis)):
		if baseForThis[x] != 0:
			finalResult.append("%d %s of Interval Class %d" %(baseForThis[x], singPlur(baseForThis[x]), x))
	return finalResult

def intervalClassConverter(digit):
	if digit <= 6:
		return digit
	else:
		return (12 - digit)

def intervalsFinder(chord):
	intervals = [0] * 7
	launchPad = primeFormLaunch(chord)
	for x in range(len(launchPad) - 1):
		for y in launchPad[x + 1::]:
			intervals[intervalClassConverter(y - launchPad[x])] += 1
	return intervals
