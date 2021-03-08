#!/usr/bin/env python3

import numpy as np
from PIL import Image
from sys import argv, stderr
from getopt import gnu_getopt, GetoptError


def median_image(images):
	mode = images[0].mode
	arrays = []
	for image in images:
		if image.mode != mode:
			raise ValueError
		
		arrays.append(np.asarray(image))
	
	dtype = arrays[0].dtype
	size = arrays[0].size
	for array in arrays:
		assert array.dtype == dtype
		
		if array.size != size:
			raise ValueError
	
	median_array = np.median(arrays, axis=0, overwrite_input=True).astype(dtype)
	return Image.fromarray(median_array, mode=mode)


def process_argv():
	try:
		options, arguments = gnu_getopt(argv[1:], 'o:h', ['output =', 'help'])
		options = dict(options)
		
		if ('-h' in options) or ('--help' in options) or (len(arguments) == 0):
			print('Usage: ' + argv[0] + ' INPUT_FILES [-o, --output] OUTPUT_FILE')
			exit()
		else:
			return arguments, options.get('-o', options.get('--options'))
	except GetoptError as err:
		print(err, file=stderr)
		exit(1)


def main():
	input_filenames, output_filename = process_argv()
	
	try:
		input_images = [Image.open(filename) for filename in input_filenames]
		output_image = median_image(input_images)
		
		if output_filename is not None:
			output_image.save(output_filename)
		else:
			output_image.show()
	except OSError as err:
		print(err, file=stderr)
		exit(1)
	except ValueError as err:
		print('Input images must all have the exact same width, height, and color mode', file=stderr)
		exit(1)


if __name__ == '__main__':
	main()
