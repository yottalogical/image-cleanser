# image-cleanser
Automatically remove moving objects from images

## Usage

Start by taking multiple pictures of your subject.
It is important that your subject stays perfectly still and that all the pictures are taken from the exact same angle.
Try to keep the lighting as consistent as possible, but it's okay if it changes by a little.

For the script to work, all the images must all have the exact same width, height, and color mode.
Unedited pictures all taken from the same camera (with the same settings) should work.

The script can be run with the following command:

```console
python3 image-cleanser.py [INPUT IMAGES FILENAMES] --output [OUTPUT IMAGE FILENAME]
```

Note: The input images filenames can be specified using [shell pattern matching](https://www.gnu.org/software/findutils/manual/html_node/find_html/Shell-Pattern-Matching.html).

If the `--output` option is not specified, the output image will be saved as a temporary PNG file, then opened using their system's default image viewer.

## Requirements

This script was written for Python 3.9.2, but should also work with later versions of Python 3.

It uses the following packages from PyPI:
* `numpy` 1.20.1
* `Pillow` 8.1.2

Later versions of these packages should also work. 
They can be quickly installed by running the following command in the base directory of this repository:

```console
pip install -r requirements.txt
```