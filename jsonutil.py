import json

def read(s):
	return json.loads(s)

def write(value):
	return json.dumps(value, indent=4)

def readfile(filepath):
	with open(filepath) as inputfile:
		return json.load(inputfile)
		
def writefile(filepath, value):
	with open(filepath, 'w') as outputfile:
		json.dump(value, outputfile, indent=4)
