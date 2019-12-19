# Colour Wheel Grapher

## About and Dependencies

Graphs can be tremendously important in understanding mathematical functions, but issues arise when graphing complex functions. This is because complex functions have 2 dimensional inputs and 2 dimensional outputs, resulting in the need of 4 total dimensions.

To get around this, we can use **colour wheel graphs** (or **domain colouring**). This is a trick that uses *colour* to fill in the extra dimensions. The 2 dimensions required by the inputs are represented in the space of a picture. The 2 dimensions of our outputs are represented in colour. The argument of the output value gives us a pixel's hue, and its magnitude gives us its lightness. The saturation of all points is 100%. More information can be found in the references.

This program uses the [Python Imaging Library](https://python-pillow.org/), as well as a few libraries available in standard Python:

* `math` to make certain constants and functions easily available.
* `cmath` for dealing with complex numbers.
* `colorsys` for converting between different colour models.



## Some Results

![z^5 - 1](https://latex.codecogs.com/png.latex?%5Cdpi%7B300%7D%20z%5E5%20-%201)

![z^5 - 1](https://i.imgur.com/wQtlpKf.jpg)



![Log(z)](https://latex.codecogs.com/png.latex?%5Cdpi%7B300%7D%20%5Ctext%7BLog%7D%28z%29)

![Log(z)](https://i.imgur.com/ptKfEvj.jpg)



![Function 2](https://latex.codecogs.com/png.latex?%5Cdpi%7B300%7D%20%5Cfrac%7B%28z%5E2%20-%201%29%28z%20-%202%20-%20i%29%5E2%7D%7B%28z%5E2%20&plus;%202%20&plus;%202i%29%7D)

![Function 2](https://i.imgur.com/fo5o0PR.jpg)

This example was inspired by Wikipedia.



## Future Development

Converting the magnitude of the output vector to a saturation requires an extra parameter. Currently, this values needs to be determined through trial and error for each function. In future, it would hopefully be calculated somehow - likely in a way to create as much contrast as possible in the output image.



## References/Further Reading

[Domain Colouring (Wikipedia)](https://en.wikipedia.org/wiki/Domain_coloring)