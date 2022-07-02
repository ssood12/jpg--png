import sys
import os
from PIL import Image

from_folder = sys.argv[1]
to_folder = sys.argv[2]

if not os.path.isdir(to_folder):
	os.mkdir(to_folder)

for filename in os.listdir(from_folder):
	img = Image.open(f'./{from_folder}/{filename}')
	clean_name = os.path.splitext(filename)[0]
	img.save(f"./{to_folder}/{clean_name}.png", 'png')