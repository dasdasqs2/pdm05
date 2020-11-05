import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np

import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)

from keras.datasets import cifar10

# Load MNIST dataset using tensorflow.keras
# Dividing data into training and test set
(x_train, y_train), (x_test, y_test) = cifar10.load_data()
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

# Sidebar
st.sidebar.header('cifar10')

# Show a random number
if st.sidebar.checkbox('Show a random image from cifar10'):
    num = np.random.randint(0, x_train.shape[0])
    image = x_train[num]
    st.sidebar.image(image, caption=class_names[y_train[num]], width=192)

# Main 
st.title('DL using CNN2D')
st.header('Dataset: cifar10')
#spending a few lines to describe our dataset
st.text("""Dataset of 50000 32x32 color training images, 
        consist of 'vehicle' and 'animal'
        and 10,000 test images.""")

# Information of mnist dataset
# (x_train, y_train), (x_test, y_test) = mnist.load_data()
if st.checkbox('Show images sizes'):
    st.write(f'##### X Train Shape: {x_train.shape}') 
    st.write(f'##### X Test Shape: {x_test.shape}')
    st.write(f'##### Y Train Shape: {y_train.shape}')
    st.write(f'##### Y Test Shape: {y_test.shape}')

# display one random image from our training set:
# st.subheader('Inspecting dataset')
# if st.checkbox('Show random image from the train set'):
#     num = np.random.randint(0, x_train.shape[0])
#     image = x_train[num]
#     st.image(image, caption=class_names[y_train[num]], width=96) 
st.write('***')
if st.checkbox('Show 10 different image from the train set'):
    num_10 = np.unique(y_train, return_index=True)[1]
#     st.write(num_10)
    images = x_train[num_10]
    for i in range(len(images)):
        # define subplot
        plt.subplot(2,5,1 + i) #, sharey=False)
        # plot raw pixel data
        plt.imshow(images[i])
        plt.title(class_names[i])
        plt.xticks([])
        plt.yticks([])
    plt.suptitle("10 different images", fontsize=18)
    st.pyplot()  # Warning