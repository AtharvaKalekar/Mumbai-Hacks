# import tensorflow as tf
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense, LeakyReLU

# def build_generator():
#     model = Sequential()
#     model.add(Dense(64, input_dim=100))
#     model.add(LeakyReLU(0.2))
#     model.add(Dense(32))
#     model.add(Dense(1))
#     return model

# def build_discriminator():
#     model = Sequential()
#     model.add(Dense(32, input_dim=1))
#     model.add(LeakyReLU(0.2))
#     model.add(Dense(1, activation='sigmoid'))
#     return model
