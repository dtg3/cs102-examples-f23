from PIL import Image
from pathlib import Path


def crop(image, tlx, tly, brx, bry):
    cropped_picture = Image.new('RGB', (brx-tlx, bry-tly), (255, 255, 255))
    dest_pixels = cropped_picture.load()
    source_pixels = image.load()
    
    dest_x = 0
    for source_x in range(tlx, brx):
        dest_y = 0
        
        for source_y in range(tly, bry):
            color = source_pixels[source_x, source_y]
            dest_pixels[dest_x, dest_y] = color
            dest_y += 1
        
        dest_x += 1
    
    return cropped_picture
            

pic = Image.open(Path('images/alphabet.jpg'))
cropped_image = crop(pic, 67, 116, 206, 251)
cropped_image.show()


