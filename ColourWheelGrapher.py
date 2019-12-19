from PIL import Image
from math import *
import cmath
import colorsys

# Function that returns the real value of f(z)
def f(z):
    try:
        return (z**2 - 1)*(z - 2 - 1j)**2/(z**2 + 2 + 2j)
    except:
        return 0

# Maps points in image to complex number z
def MAP(x, y, scale, origin):
    Cx, Cy = origin
    a = (x - Cx)/scale
    b = -(y - Cy)/scale
    return a + b*1j

# Main function
def main(function, width, height, scale, origin):
    # Creates RGB image
    img = Image.new("RGB",(width,height))
    
    # Loops through all pixels in image
    for x in range(width):
        for y in range(height):    
            # Convert image coordinates to complex number
            z = MAP(x,y,scale,origin)
            # Determine colouring of pixel (in HLS)
            H = cmath.phase(function(z))  
            L = 1 - 1.05**(-abs(function(z)))
            S = 1

            # Converts HLS to RGB
            R, G, B = colorsys.hls_to_rgb(H/(2*pi), L, S)
            # Writes colour to pixel
            img.putpixel((x,y), (round(R*255),round(G*255),round(B*255)))
            
    # Returns image
    return img

if __name__ == "__main__":
    cwgraph = main(f,1000,1000,100,(500,500))
    cwgraph.save("cwgraph.jpg", "JPEG")
    cwgraph.show()
