import numpy as np
import pandas as pd
import tensorflow
import keras
from keras.layers import Dense
from keras.models import Sequential
import pickle
def load_data(filepath):
    try:
        data = pd.read_csv(filepath)
        return data
    except Exception as e:
        print("Could not  open file")


def four_layer_architecture(data: pd.DataFrame):
    try:
        X = data.drop(columns=['Path_is_optimal'])
        y = data['Path_is_optimal']
        model = Sequential()
        model.add(Dense(8, activation='relu', input_dim=4))
        model.add(Dense(8, activation='relu'))
        model.add(Dense(4, activation='relu'))
        model.add(Dense(1, activation='sigmoid'))
        model.compile(loss='binary_crossentropy', optimizer='Adam', metrics=['accuracy'])
        model.fit(X, y, epochs=100, validation_split=0.2, batch_size=5000)

        pickle.dump(model,open('model.pkl','wb'))
        print("pickle Updated Sucessfull")
    except Exception as e:
        print("Model and Pickle not created")


def six_layer_architecture(data: pd.DataFrame):
    try:
        X = data.drop(columns=['Path_is_optimal'])
        y = data['Path_is_optimal']
        model = Sequential()
        model.add(Dense(8, activation='relu', input_dim=4))
        model.add(Dense(8, activation='relu'))
        model.add(Dense(8, activation='relu'))
        model.add(Dense(8, activation='relu'))
        model.add(Dense(4, activation='relu'))
        model.add(Dense(1, activation='sigmoid'))
        model.compile(loss='binary_crossentropy', optimizer='Adam', metrics=['accuracy'])
        model.fit(X, y, epochs=100, validation_split=0.2, batch_size=5000)

        pickle.dump(model, open('model.pkl', 'wb'))
        print("pickle Updated Sucessfull")
    except Exception as e:
        print("Model and Pickle not created")


def eight_layer_architecture(data: pd.DataFrame):
    try:
        X = data.drop(columns=['Path_is_optimal'])
        y = data['Path_is_optimal']
        model = Sequential()
        model.add(Dense(8, activation='relu', input_dim=4))
        model.add(Dense(8, activation='relu'))
        model.add(Dense(8, activation='relu'))
        model.add(Dense(8, activation='relu'))
        model.add(Dense(4, activation='relu'))
        model.add(Dense(4, activation='relu'))
        model.add(Dense(4, activation='relu'))
        model.add(Dense(1, activation='sigmoid'))
        model.compile(loss='binary_crossentropy', optimizer='Adam', metrics=['accuracy'])
        model.fit(X, y, epochs=100, validation_split=0.2, batch_size=5000)

        pickle.dump(model, open('model.pkl', 'wb'))
        print("pickle Updated Sucessfull")
    except Exception as e:
        print("Model and Pickle not created")

