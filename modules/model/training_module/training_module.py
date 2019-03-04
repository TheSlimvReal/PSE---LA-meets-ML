import h5py
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import optimizers
from keras.models import load_model
from keras.callbacks import ModelCheckpoint
import keras

from modules.controller.commands.module import Module
from modules.view.output_service import OutputService
from modules.shared.configurations import Configurations


##  This class handles the training of the neural network
class TrainingModule:

    __output_service: OutputService = OutputService()

    # Network Structure:
    __num_conv_layers: int = Configurations.get_config(Module.TRAIN, "num_conv_layers")
    __num_dense_layers: int = Configurations.get_config(Module.TRAIN, "num_dense_layers")
    __layer_activation: str = Configurations.get_config(Module.TRAIN, "layer_activation")
    __final_activation: str = Configurations.get_config(Module.TRAIN, "final_activation")
    __dropout: int = Configurations.get_config(Module.TRAIN, "dropout")
    __num_classes: int = 4

    # Hyper parameters:
    __batch_size: int = Configurations.get_config(Module.TRAIN, "batch_size")
    __learning_rate: float = Configurations.get_config(Module.TRAIN, "learning_rate")
    __loss: str = Configurations.get_config(Module.TRAIN, "loss")
    __epochs: int = Configurations.get_config(Module.TRAIN, "epochs")

    ##  trains the neural network labeled matrices
    #
    #   @param matrices_path path where the labeled matrices are located
    #   @param neural_network_path path where are existing neural network is located if you want to improve one
    #   @param name under which the trained network will be saved
    #   @param saving_path path to where the trained network will be saved
    #   @param training_test_split float no how much of the data should be for training purposes, the
    #           rest will be used for testing
    @staticmethod
    def train(matrices_path: str, neural_network_path: str, name: str, saving_path: str, training_test_split: float) -> None:

        # model is defined by the config file or loaded from a path
        model = TrainingModule.__get_model(neural_network_path)

        train_datagen = ImageDataGenerator()
        validation_datagen = ImageDataGenerator()

        # loads matrices and labels from hdf5 file
        dataset = h5py.File(matrices_path, 'r')

        # converts matrices and labels in keras conform shape (samples, height, width, channels)
        matrices = np.array(dataset['dense_matrices'])
        labels = np.array(dataset['label_vectors'])

        index = int(training_test_split * len(matrices))

        train_matrices = np.expand_dims(matrices[:index], axis=3)
        train_labels = labels[:index]

        validation_matrices = np.expand_dims(matrices[index + 1:], axis=3)
        validation_labels = labels[index + 1:]

        # saves model after every training epoch in format "saving_path+name+epochnr+loss"
        checkpointer = ModelCheckpoint(filepath=saving_path + name + "{epoch:02d}-{val_loss:.2f}.hdf5", monitor='val_loss',
                                       verbose=1, save_best_only=True, save_weights_only=False, mode='auto', period=1)

        # trains model
        validation_steps = len(validation_matrices) / TrainingModule.__batch_size
        model.fit_generator(train_datagen.flow(train_matrices, train_labels, batch_size=TrainingModule.__batch_size),
                            steps_per_epoch=len(matrices) / TrainingModule.__batch_size,
                            epochs=TrainingModule.__epochs, callbacks=[checkpointer], verbose=1,
                            validation_data=validation_datagen.flow(validation_matrices, validation_labels),
                            validation_steps=validation_steps)

    @staticmethod
    def __get_model(neural_network_path: str) -> keras.models.Sequential:
        if not neural_network_path:
            # path not set, create new model
            model = TrainingModule.__define_new_model()
        else:
            # loads a compiled model from the specified path
            model = load_model(neural_network_path)
        return model

    ##  sets the static output service
    #
    #   use this to register your own output service at the start of the program
    #   this output service will be for called logs and results
    #   @param service OutputService that should be registered
    @staticmethod
    def set_output_service(service: OutputService):
        TrainingModule.__output_service = service

    @staticmethod
    def __define_new_model():
        model = Sequential()
        output_size = 32
        kernel_size = 3
        new_output_size = 0

        if TrainingModule.__num_conv_layers != 0:
            model.add(Conv2D(output_size, (kernel_size, kernel_size), input_shape=(128, 128, 1)))
            model.add(Activation(TrainingModule.__layer_activation))
            new_output_size = output_size

        for i in range(1, TrainingModule.__num_conv_layers):
            model.add(Conv2D(output_size * (i + 1), (kernel_size, kernel_size)))
            model.add(Activation(TrainingModule.__layer_activation))
            new_output_size = output_size * (i + 1)

        model.add(Flatten())

        if TrainingModule.__num_dense_layers > 1:
            model.add(Dense(new_output_size * 4))
            model.add(Activation(TrainingModule.__layer_activation))
            for i in range(1, TrainingModule.__num_dense_layers - 1):
                model.add(Dense(int((new_output_size * 4) / i)))
                model.add(Activation(TrainingModule.__layer_activation))

        model.add(Dropout(TrainingModule.__dropout))

        model.add(Dense(TrainingModule.__num_classes))
        model.add(Activation(TrainingModule.__final_activation))

        optimizer = optimizers.SGD(lr=TrainingModule.__learning_rate)
        model.compile(loss=TrainingModule.__loss,
                      optimizer=optimizer, metrics=['accuracy'])
        return model
