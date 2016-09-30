from itertools import islice

def _read_spectra(inputfile, pixel_count):
	inputfile.readline()
	return [int(line.strip()) for line in islice(inputfile, pixel_count)]

def read(filepath):
	with open(filepath) as inputfile:
		header = {}
		for line in inputfile:
			if 'XValues' in line:
				break
			key, value = line.split(maxsplit=1)
			header[key] = value.strip()
			
		header.update({
			'PixelCount': int(header['PixelCount']),
			'TotalSpectra': int(header['TotalSpectra']),
			'ScanPixelsX': int(header['ScanPixelsX']),
			'ScanPixelsY': int(header['ScanPixelsY'])
		})
		
		xvalues = [float(line.strip()) for line in islice(inputfile, header['PixelCount'])]
		spectra = [_read_spectra(inputfile, header['PixelCount']) for _ in range(header['TotalSpectra'])]
		
		return {'header': header, 'xvalues': xvalues, 'spectra': spectra}
