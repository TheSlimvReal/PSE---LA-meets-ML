import h5py
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import optimizers
from keras.models import load_model
from keras.callbacks import ModelCheckpoint
import keras
from modules.view.output_service import OutputService


##  This class handles the training of the neural network
class TrainingModule:

    __output_service: OutputService = OutputService()

    ##  trains the neural network labeled matrices
    #
    #   @param matrices_path path where the labeled matrices are located
    #   @param neural_network_path path where are existing neural network is located if you want to improve one
    #   @param name under which the trained network will be saved
    #   @param saving_path path to where the trained network will be saved
    @staticmethod
    def train(matrices_path: str, neural_network_path: str, name: str, saving_path: str) -> None:

        # model is defined by the config file or loaded from a path
        model = TrainingModule.__define_model(neural_network_path)

        datagen = ImageDataGenerator()

        # loads matrices and labels from hdf5 file
        dataset = h5py.File(matrices_path, 'r')

        # converts matrices and labels in keras conform shape (samples, height, width, channels)
        matrices = np.expand_dims(np.array(dataset['dense_matrices']), axis=3)
        labels = np.array(dataset['label_vectors'])

        # saves model after every training epoch in format "saving_path+name+epochnr+loss"
        checkpointer = ModelCheckpoint(filepath=saving_path + name + "{epoch:02d}-{loss:.2f}.hdf5", monitor='loss',
                                       verbose=0, save_best_only=False, save_weights_only=False, mode='auto', period=1)

        # trains model
        model.fit_generator(datagen.flow(matrices, labels, batch_size=25),
                            steps_per_epoch=len(matrices) / 25, epochs=5, callbacks=[checkpointer])

    @staticmethod
    def __define_model(neural_network_path: str) -> keras.models.Sequential:
        if neural_network_path == "":
            # later config file definitions should happen here
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
                          optimizer=optimizer, metrics=['accuracy'])
        else:
            # loads a compiled model from the specified path
            model = load_model(neural_network_path)

        return model

    @staticmethod
    def set_output_service(service: OutputService):
        TrainingModule.__output_service = service
