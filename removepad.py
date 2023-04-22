import os
import glob
import tqdm
import argparse
from PIL import Image, ImageChops, UnidentifiedImageError

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--folder', type=str)
    return parser.parse_args()

def main():
    args = get_args()

    images = glob.glob(f'{args.folder}/*')

    for image in tqdm(images):
        im = Image.open(image)
        
        bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
        diff = ImageChops.difference(im, bg)
        diff = ImageChops.add(diff, diff, 2.0, -100)
        bbox = diff.getbbox()
        if bbox:
            im = im.crop(bbox)  
            im.save(image)

if __name__ == '__main__':
    main()