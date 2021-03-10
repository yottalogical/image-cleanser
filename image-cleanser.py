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


def print_help():
	print(f'Usage: {argv[0]} INPUT_FILES [-o, --output] OUTPUT_FILE')


def process_argv():
	options, input_filenames = gnu_getopt(argv[1:], 'o:h', ['output=', 'help'])
	
	if len(input_filenames) == 0:
		print_help()
		exit(1)
	
	output_filename = None
	for option, parameter in options:
		if option in ('-o', '--output'):
			output_filename = parameter
		elif option in ('-h', '--help'):
			print_help()
			exit()
	
	return input_filenames, output_filename


def main():
	try:
		input_filenames, output_filename = process_argv()
		
		print('Loading images...')
		input_images = [Image.open(filename) for filename in input_filenames]
		
		print('Processing images...')
		output_image = median_image(input_images)
		
		if output_filename is not None:
			print('Saving image...')
			output_image.save(output_filename)
		else:
			print('Displaying image...')
			output_image.show()
	except (GetoptError, OSError) as err:
		print(err, file=stderr)
		exit(1)
	except ValueError:
		print('Input images must all have the exact same width, height, and color mode', file=stderr)
		exit(1)


if __name__ == '__main__':
	main()
