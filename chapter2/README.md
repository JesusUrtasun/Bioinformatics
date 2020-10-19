# Chapter 2

## Basics of Python

*Jesús Urtasun Elizari - University of Milan - 2019/20.*

## Exercise 1 - Install Python

If you have succesfully followed the tutorial in `chapter0` you already have the basic notions of Linux that will be needed for this course.
Then, as in most of Linux devices, Python is already installed in your machine. If for whatever reason that is not the case, download it from 
the official website [https://www.python.org/downloads/](https://www.python.org/downloads/).

You can also download it from the terminal following the instructions in 
[https://linuxize.com/post/how-to-install-python-3-7-on-ubuntu-18-04/#installing-python-37-on-ubuntu-with-apt]
(https://linuxize.com/post/how-to-install-python-3-7-on-ubuntu-18-04/#installing-python-37-on-ubuntu-with-apt)


## Exercise 2 - Install basic libraries

For the first steps we will use `numpy`, the basic Python library used for numerical computations.
[https://numpy.org/](https://numpy.org/)
During the course we will also use `TensorFlow` and `Keras`, extermely powerful for Machine Learning applications.
[https://www.tensorflow.org/](https://www.tensorflow.org/)
[https://keras.io/][https://keras.io/]
Both will be extensively used and discussed durnig the course.

## Exercise 3 - Get used to Python

Before starting we suggest to create a folder for chapter 1 where you can save all files that will be created for the exercise
```bash
cd ~/           # go the home directory
mkdir chapter1  # create the directory chapter1 in home
cd chapter1     # go inside chapter1
```

1. Import `numpy ` as `np`, `tensorflow` as `tf` and `keras`.

2. Generate two matrices `a` and `b` filled with random numbers, by calling the random method of `numpy`.
Create a matrix `c` equivalent to the product of `a` and `b`, computed with `np.dot()`, and print it on screen.

3. Check that `tensorflow` is correctly installed by printing the version on screen.
```python
print("\nTensorflow version: {}".format(tf.__version__))
```

3. Check that `keras` is correctly installed by generating a sequential model.
```python
model = keras.Sequential()
print(model)
```