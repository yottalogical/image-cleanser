#!/usr/bin/env python3

import numpy as np
from PIL import Image
from sys import argv


def median(arrays):
	dtype = arrays[0].dtype
	for array in arrays:
		assert array.dtype == dtype
	
	return np.median(arrays, axis=0).astype(dtype)


def main():
	input_image_arrays = [np.asarray(Image.open(str(i) + '.jpeg')) for i in range(int(argv[1]))]
	
	Image.fromarray(median(input_image_arrays)).save('output.jpeg')


if __name__ == '__main__':
	main()
