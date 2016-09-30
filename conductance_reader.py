def read(filepath):
	data = ''
	with open(filepath) as inputfile:
		inputfile.readline()
		lines = []
		for line in inputfile:
			line = line.strip()
			if not line:
				break
			if ':' in line:
				lines.append(line)
			else:
				lines[-1] += ' ' + line
		header = dict([token.strip() for token in line.split(':', maxsplit=1)] for line in lines)
		return header
