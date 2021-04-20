# Image Filtering
Filters can be defined as "Operations on an image to modify/transform them so that they are **usable**."
> Usable is the key here, based on the applications an image can be filtered for smoothening or for enhancing an edge.

Typically these operations are performed to enhance an image by eliminating or reducing undesired properties (a.k.a noise) and increasing the desired properties of an image.

---

## Classification of **spatial** filtering techniques

### Linear type
- Low-pass filtering
- High-pass filtering
- Bandpass filtering
- Band Stop filtering

### Statistical Type
- Minimum
- Maximum
- Median

### Derivative Type
- Laplacian
- Prewitt
- Sobel


### Low-pass filtering (a.k.a) Image smoothing or blurring
In this technique, we attenuate (or eliminate) high frequency components such as characterized by edges and sharp details in an image # Image Filtering
Filters can be defined as "Operations on an image to modify/transform them so that they are **usable**."
> Usable is the key here, based on the applications an image can be filtered for smoothening or for enhancing an edge.
> Net effect is image blurring

### High-pass filtering (a.k.a) Image sharpening
In this technique, we attenuate (or eliminate) low frequency components such as slowly varying characteristics
> Net effect is a sharpening of edges and other details


### Key Terms
- **Image patch** is a small square matrix (3x3, 5x5, etc) region of the image centered around a pixel
- **Kernel** is a small square matrix (3x3, 5x5, etc) also called a filter used for convolution.  This is also called as **convolution matrix** or a **mask**.
- **Convolution** Its the basis of all linear filters, it requires two parameters/matrix **patch** and **kernel** matrix.  ***NOTE*: size of both matrices must be same.**
> For color images, convolution is performed on the all the channels separately.

> **Refer to Spatial filtering notes for details EE4323 Chapter - 07, Chapter - 08**
---
## The following spatial filters are demonstrated:
---
#### Brightness and Contrast
- [Contrast]
- [Brightness]
- [Comparison Between Brightness and Contrast]

#### Low Pass Filters
- [Convolution]
- [Low Pass]
- [Gaussian]
- [Bilateral]
- [Median]
- [Comparison of Filters]

#### First Order Filter
- [Prewitt]
- [Sobel]

#### Second Order Filter
- [Laplacian]
- [Laplacian Of Gaussian]

#### High Pass Filter
- [High Pass]

### Applications:
- [Blur Detection]
