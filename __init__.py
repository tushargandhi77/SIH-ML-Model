from Utils import  load_data
from Utils import four_layer_architecture
from Utils import six_layer_architecture
from Utils import eight_layer_architecture

if __name__ == "__main__":
    path = 'dataset.csv'
    data = load_data(path)
    six_layer_architecture(data)
