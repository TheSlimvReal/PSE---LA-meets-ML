import h5py
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import optimizers



##  This class handles the training of the neural network
class TrainingModule:

    ##  trains the neural network labeled matrices
    #
    #   @param matrices_path path where the labeled matrices are located
    #   @param neural_network_path path where are existing neural network is located if you want to improve one
    #   @param name under which the trained network will be saved
    #   @param saving_path path to where the trained network will be saved
    @staticmethod
    def train(matrices_path: str, neural_network_path: str, name: str, saving_path: str):
        NUM_CLASSES = 5
        model = Sequential()

        model.add(Conv2D(32, (3, 3), input_shape=(128, 128, 1)))
        model.add(Activation('relu'))

        model.add(Flatten())

        model.add(Dense(64))
        model.add(Activation('relu'))

        model.add(Dense(NUM_CLASSES))
        model.add(Activation('sigmoid'))

        optimizer = optimizers.SGD(lr=0.001)
        model.compile(loss='categorical_crossentropy',
                     optimizer=optimizer,
                     metrics=['accuracy'])


        ################################
        datagen = ImageDataGenerator()
        dataset = h5py.File(matrices_path, 'r')


        matrices = np.expand_dims(np.array(dataset['dense_matrices']), axis=3)
        labels = np.array(dataset['label_vectors'])

        model.fit_generator(datagen.flow(matrices, labels, batch_size=25),
                            steps_per_epoch=len(matrices) / 25, epochs=1)




