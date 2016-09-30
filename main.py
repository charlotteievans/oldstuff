import sys, argparse, jsonutil, image_spectrum_reader, fileutil
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

def parse_args(argv):
	parser = argparse.ArgumentParser()
	parser.add_argument('filepath')
	return parser.parse_args(argv)

def integrate_spectra(spectra, a, b):
	return sum(spectra[i] for i in range(a, b))
	
def create_spectra_figure(spectrum, figure_index):	
	a = 550
	b = 600
	
	header = spectrum['header']
	
	print(jsonutil.write(header))
	x, y = np.meshgrid(range(header['ScanPixelsX']), range(header['ScanPixelsY']))
	z = np.array([integrate_spectra(s, a, b) for s in spectrum['spectra']]).reshape((header['ScanPixelsX'], header['ScanPixelsY']))
	
	fig = plt.figure(figure_index)
	ax = fig.add_subplot(121, projection='3d')
	ax.plot_wireframe(x, y, z)
	ax2 = fig.add_subplot(122)
	ax2.imshow(z, interpolation='none', cmap=cm.hot)
	
def main(argv):
	args = parse_args(argv)
	
	items = [image_spectrum.read(filepath) for filepath in fileutil.listdir('z')]
	for figure_index, item in enumerate(items):
		create_spectra_figure(item, figure_index)

	plt.show()
	
		
if __name__ == '__main__':
	main(sys.argv[1:])
