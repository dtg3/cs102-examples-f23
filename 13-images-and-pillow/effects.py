from PIL import Image
from pathlib import Path
import math


# A function for approximating how similar two colors are
def color_difference(color1, color2):
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    
    # This is a euclidean distance over all three values
    #	of the color (r, g, b).
    return math.sqrt((r2-r1)**2 + (g2-g1)**2 + (b2-b1)**2)


# A function to determine how bright or intense a color is
def average_luminance(color):
    r, g, b = color
    return (r + g + b) / 3


def detect_edge(picture_path):
    source = Image.open(Path(picture_path))
    px = source.load()
    width, height = source.size
    for x in range(width):
        for y in range(height):
            
            # This is a boundary check to make sure we do not try to get a
            #   bottom-right pixel (botrt) adjacent to our pixel (px)
            if y < height - 1 and x < width - 1:
                # Access the bottom right pixel in the image based on the x,y of our
                #   current pixel (px)
                botrt = px[x + 1, y + 1]
                
                # Calculate the color distance between the two pixels and compare
                #    that distance to a threshold value where a 
                #    higher threshold values means more white pixels
                if color_difference(px[x, y], botrt) > 25:
                    px[x, y] = (0,0,0)
                else:
                    px[x, y] = (255,255,255)

    return source

def chroma_key(fg, bg, ccolor):
    foreground = Image.open(fg)
    background = Image.open(bg)
    
    fg_pixels = foreground.load()
    bg_pixels = background.load()
    
    # foreground needs to be the <= size of the background image
    width, height = foreground.size
    for x in range(width):
        for y in range(height):
            # Look for the color used for the background chromakey
            if color_difference(fg_pixels[x, y], ccolor) < 100:
                fg_pixels[x, y] = bg_pixels[x, y]
    
    return foreground


def greyscale(picture_path):
    source = Image.open(Path(picture_path))
    px = source.load()
    width, height = source.size
    
    for x in range(width):
        for y in range(height):
            # If we know how "bright" the color is, we can set that
            #	brightness to all the channels (r, g, b) to create
            #	a grey of the appropriate intensity
            avg_lum = int(average_luminance(px[x, y]))
            px[x,y] = (avg_lum, avg_lum, avg_lum)
    
    return source


# Blend two images together
#	This assumes the images are the same dimensions
def blend_images(pic1_path, pic2_path):
    image1 = Image.open(pic1_path)
    img1_px = image1.load()
    
    image2 = Image.open(pic2_path)
    img2_px = image2.load()
    
    width, height = image1.size
    
    new_image = Image.new('RGB', (width, height))
    new_pixels = new_image.load()
    
    for x in range(new_image.size[0]):
        for y in range(new_image.size[1]):
            r1, g1, b1 = img1_px[x, y]
            r2, g2, b2 = img2_px[x, y]
            
            # The secret sauce...
            #	Take a portion of each color and combine the values
            #	70% of image1's pixel value, and 30% from image2
            #	This 'blends' the pixel values to create the effect.
            r = int(r1*.7 + r2*.3)
            g = int(g1*.7 + g2*.3)
            b = int(b1*.7 + b2*.3)
            
            new_pixels[x, y] = (r, g, b)
    
    return new_image    
            
            
detect_edge(Path('images/car.jpg')).show()

chroma_color = (1, 255, 19)
chroma_key(Path('images/chromakey/minion.png'), Path('images/chromakey/background.png'), chroma_color).show()

greyscale(Path('images/apples.jpg')).show()

pic1_path = Path('images/dog.jpg')
pic2_path = Path('images/leaf.jpg')
blend_images(pic1_path, pic2_path).show()