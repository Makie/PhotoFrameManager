#!/usr/bin/env 

import os
import sys

from fractions import Fraction
from PIL import Image

source_folder = r"C:\Users\Makie\GitHub\PhotoFrameManager\IN"
output_folder = r"C:\Users\Makie\GitHub\PhotoFrameManager\OUT"
skipped_files = []

print("Looking in:", source_folder)
print("Saving to:", output_folder)

for root, folders, files in os.walk(source_folder):
    for number, filepath in enumerate(os.path.join(root, file) for file in files):
        try:
            im = Image.open(filepath)
            im.verify()
        except:
            skipped_files.append((number, filepath, "VERIFY FAIL",sys.exc_info()[1]))
            continue
        else:
            im = Image.open(filepath)

        width, height = im.size
        print(number, filepath)

        # If image is portrait, roatate before scaling.
        portrait = height > width
        if portrait:
            im = im.rotate(90)

        try:
            # Scale image
            im = im.resize((1024, 768))    
        except:
            skipped_files.append((number, filepath, "VERIFY FAIL",sys.exc_info()[1]))
            continue
        
        # Rotate back if needed
        if portrait:
            im = im.rotate(-90)
        # Save image
        outpath = os.path.join(output_folder, "{:0>4}.jpg".format(number))
        print(outpath)
        im.save(outpath, format="JPEG", quality=95, optimize=True)
        print("Done.")

print("COMPLETE")

if len(skipped_files) > 0:
    print(len(skipped_files), "files were skipped, details follow:")
    for entry in skipped_files:
        print(entry)
