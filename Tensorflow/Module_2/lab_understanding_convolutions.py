"""Convolution: 1D operation with Python (Numpy/Scipy)"""

import numpy as np

h = [2, 1, 0]
x = [3, 4, 5]

y = np.convolve(x, h)
y

print("Compare with the following values from Python: y[0] = {0} ; y[1] = {1}; y[2] = {2}; y[3] = {3}; y[4] = {4}".format(y[0], y[1], y[2], y[3], y[4]))


x = [6, 2]
h = [1, 2, 5, 4]

y = np.convolve(x, h, "full")  # now, because of the zero padding, the final dimension of the array is bigger


x = [6, 2]
h = [1, 2, 5, 4]

y = np.convolve(x, h, "same")  # it is same as zero padding, but with returns an ouput with the same length as max of x or h


x = [6, 2]
h = [1, 2, 5, 4]

y = np.convolve(x, h, "valid")  # valid returns output of length max(x, h) - min(x, h) + 1, this is to ensure that values outside of the boundary of
                                # h will not be used in the calculation of the convolution
                                # in the next example we will understand why we used the argument valid


"""Convolution: 2D operation with Python (Numpy/Scipy)"""
from scipy import signal as sg

I= [[255,   7,  3],
    [212, 240,  4],
    [218, 216, 230],]

g= [[-1, 1]]

print('Without zero padding \n')
print('{0} \n'.format(sg.convolve(I, g, 'valid')))
# The 'valid' argument states that the output consists only of those elements
# that do not rely on the zero-padding.

print('With zero padding \n')
print(sg.convolve(I, g))

print('With zero(left) padding \n')
print(sg.convolve(I, g, 'same'))

# For a more difficult case where h= [ [-1 1] , [2 3] ]
I = [[255,   7,  3],
    [212, 240,  4],
    [218, 216, 230],]

g = [[-1,  1],
     [2,  3]]

print('With zero padding \n')
print('{0} \n'.format(sg.convolve(I, g, 'full')))
# The output is the full discrete linear convolution of the inputs.
# It will use zero to complete the input matrix

print('With zero padding_same_ \n')
print('{0} \n'.format(sg.convolve(I, g, 'same')))
# The output is the full discrete linear convolution of the inputs.
# It will use zero to complete the input matrix


print('Without zero padding \n')
print(sg.convolve( I, g, 'valid'))
# The 'valid' argument states that the output consists only of those elements
# that do not rely on the zero-padding.


"""Coding with TensorFlow"""
import tensorflow as tf
print("using version " + tf.__version__)

input = tf.Variable(tf.random.normal([1, 10, 10, 1]))
filter = tf.Variable(tf.random.normal([3, 3, 1, 1]))
op = tf.nn.conv2d(input, filter, strides=[1, 1, 1, 1], padding='VALID')
op2 = tf.nn.conv2d(input, filter, strides=[1, 1, 1, 1], padding='SAME')

print("Input \n")
print('{0} \n'.format(input.numpy()))
print("Filter/Kernel \n")
print('{0} \n'.format(filter.numpy()))
print("Result/Feature Map with valid positions \n")
print(op.numpy())
print('\n')
print("Result/Feature Map with padding \n")
print(op2.numpy())


"""Convolution applied on images"""
#Importing
from scipy import signal
from scipy import misc
import matplotlib.pyplot as plt
from PIL import Image

im = Image.open('/Users/harold/PycharmProjects/DeepLearning_IBM/Tensorflow/Module_2/Rhea.jpg')  # type here your image's name

image_gr = im.convert("L")    # convert("L") translate color images into black and white
                              # uses the ITU-R 601-2 Luma transform (there are several
                              # ways to convert an image to grey scale)
print("\n Original type: %r \n\n" % image_gr)

# convert image to a matrix with values from 0 to 255 (uint8)
arr = np.asarray(image_gr)
print("After conversion to numerical representation: \n\n %r" % arr)
# Activating matplotlib for Ipython

# Plot image
imgplot = plt.imshow(arr)
imgplot.set_cmap('gray')  # you can experiment different colormaps (Greys,winter,autumn)
print("\n Input image converted to gray scale: \n")
plt.show(imgplot)


# Now, we will experiment using an edge detector kernel.

kernel = np.array([[0, 1, 0],
                   [1, -4, 1],
                   [0, 1, 0]])

grad = signal.convolve2d(arr, kernel, mode='same', boundary='symm')

print('GRADIENT MAGNITUDE - Feature map')

fig, aux = plt.subplots(figsize=(10, 10))
aux.imshow(np.absolute(grad), cmap='gray')

type(grad)

grad_biases = np.absolute(grad) + 100

grad_biases[grad_biases > 255] = 255

print('GRADIENT MAGNITUDE - Feature map')

fig, aux = plt.subplots(figsize=(10, 10))
aux.imshow(np.absolute(grad_biases), cmap='gray')

# Lets see how it works for a digit:
im = Image.open('/Users/harold/PycharmProjects/DeepLearning_IBM/Tensorflow/Module_2/destructed3.jpg')  # type here your image's name

image_gr = im.convert("L")    # convert("L") translate color images into black and white
                              # uses the ITU-R 601-2 Luma transform (there are several
                              # ways to convert an image to grey scale)
print("\n Original type: %r \n\n" % image_gr)

# convert image to a matrix with values from 0 to 255 (uint8)
arr = np.asarray(image_gr)
print("After conversion to numerical representation: \n\n %r" % arr)
# Activating matplotlib for Ipython

# Plot image
fig, aux = plt.subplots(figsize=(10, 10))
imgplot = plt.imshow(arr)
imgplot.set_cmap('gray')  #you can experiment different colormaps (Greys,winter,autumn)
print("\n Input image converted to gray scale: \n")
plt.show(imgplot)


kernel = np.array([
                        [ 0, 1, 0],
                        [ 1,-4, 1],
                        [ 0, 1, 0],
                                     ])

grad = signal.convolve2d(arr, kernel, mode='same', boundary='symm')

print('GRADIENT MAGNITUDE - Feature map')

fig, aux = plt.subplots(figsize=(10, 10))
aux.imshow(np.absolute(grad), cmap='gray')






