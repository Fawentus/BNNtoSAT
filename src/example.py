import random

import numpy as np
import tensorflow as tf
import larq as lq
import matplotlib.pyplot as plt

from src.encode_model.encode_model import Encode

# (train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.cifar10.load_data()
#
# print(len(test_images))
# print(len(test_images[0]))
# print(len(test_images[0][0]))
# print(len(test_images[0][0][0]))
# # print(len(test_images[0][0][0][0]))
# # print(len(test_images[0][0][0][0][0]))
# # print(test_images[0])
# # print(max(test_labels))
# print(min(test_images.flatten()), max(test_images.flatten()))
# id_image = random.randint(0, 100-1)
# # plt.imshow(test_images[id_image])
# print(test_images[id_image])
#
# # test_images = test_images[:100]
#
# new_test_images = np.empty(test_images.shape + (8,))
# for i in range(len(test_images)):
#     for j in range(len(test_images[0])):
#         for k in range(len(test_images[0][0])):
#             for l in range(len(test_images[0][0][0])):
#                 num = '{0:08b}'.format(test_images[i][j][k][l])
#                 for n in range(len(num)):
#                     if num[n] == '1':
#                         new_test_images[i][j][k][l][n] = 1
#                     else:
#                         new_test_images[i][j][k][l][n] = -1
#
#
# # _, (test_images, test_labels) = tf.keras.datasets.cifar10.load_data()
# print(len(new_test_images))
# print(len(new_test_images[0]))
# print(len(new_test_images[0][0]))
# print(len(new_test_images[0][0][0]))
# print(len(new_test_images[0][0][0][0]))
# # print(len(new_test_images[0][0][0][0][0]))
# # print(len(new_test_images[0][0][0][0][0][0]))
# # print(test_images[0])
# # print(max(test_labels))
# # print(min(new_test_images.flatten()), max(new_test_images.flatten()))
# # test_images = test_images / 127.5 - 1
# # print(min(test_images.flatten()), max(test_images.flatten()))
# id_image = random.randint(0, 100-1)
# # plt.imshow(test_images[id_image])
# print(new_test_images[id_image])
# # print(id_image)


# Load MNIST
# _, (test_images, test_labels) = tf.keras.datasets.mnist.load_data()
# test_images = test_images.reshape((10000, 28, 28, 1))
# test_images = test_images / 127.5 - 1  # Normalize pixel values to be between -1 and 1

# Print image
# id_image = random.randint(0, 10000-1)
# plt.imshow(test_images[id_image])
# print(id_image)
# plt.show()

# Get stat
# model = tf.keras.models.load_model("../data/models/mnist/model103.h5")
# test_loss, test_acc = model.evaluate(test_images, test_labels)
# print(f"Test accuracy {test_acc * 100:.2f} %")
# lq.models.summary(model)
#
# # Get intermediate values
# layer_outputs = [layer.output for layer in model.layers]
# activation_model = tf.keras.models.Model(inputs=model.input, outputs=layer_outputs)
# acts = activation_model.predict(test_images[id_image:id_image+1])
#
# print('\n- - - - - -', 'start', '- - - - - -')
# for i in test_images[id_image]:
#     for j in i:
#         print(j, end='')
#     print()
#
# for i in range(len(model.layers)):
#     layer = model.layers[i]
#     print('\n-----------', layer.name, '-----------')
#     print(layer.weights)
#     print('\n- - - - - -', layer.name, '- - - - - -')
#     print(acts[i].shape)
#     print(acts[i])
#
# print('\n-----------', 'ANSWER', '-----------')
# max_value = max(acts[-1][0])
# print([str(index) + ' ' + str(val) for index, val in enumerate(acts[-1][0])])
# print([index for index, val in enumerate(acts[-1][0]) if val == max_value])
#
# encode = Encode(model)
# encode.print_vars()
# encode.print_constraints()


(train_images_, train_labels), (test_images_, test_labels) = tf.keras.datasets.mnist.load_data()
test_images_ = test_images_[:1000]  # TODO
test_labels = test_labels[:1000]  # TODO

test_images = np.empty((len(test_images_), 28, 28, 8))
for k in range(len(test_images_)):
    for i in range(len(test_images_[0])):
        for j in range(len(test_images_[0][0])):
            num = '{0:08b}'.format(test_images_[k][i][j])
            for n in range(len(num)):
                if num[n] == '1':
                    test_images[k][i][j][n] = 1
                else:
                    test_images[k][i][j][n] = -1
    if k % 100 == 0:
        print(str(k) + "/" + str(len(train_images_)))

model = tf.keras.models.load_model("../data/models/mnistl/model_from_pytorch2.h5")
test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f"Test accuracy {test_acc * 100:.2f} %")
lq.models.summary(model)


























# model = tf.keras.models.load_model("../data/models/my/model11.h5")
# for i in range(len(model.layers)):
#     layer = model.layers[i]
#     print('\n-----------', layer.name, '-----------')
#     # print(layer.weights)
#     if len(layer.weights) > 0:
#         print(layer.weights[0].read_value().numpy().transpose())


# print("../data/models/mnist/model4.h5")
# model = tf.keras.models.load_model("../data/models/mnist/model4.h5")
# for i in range(len(model.layers)):
#     layer = model.layers[i]
#     print('\n-----------', layer.name, '-----------')
#     print(len(layer.weights))
#     for i in range(len(layer.weights)):
#         print(layer.weights[i].read_value().numpy().shape)
#         print(layer.weights[i].read_value().numpy())
#
# print("../data/models/mnist/model100.h5")
# model = tf.keras.models.load_model("../data/models/mnist/model100.h5")
# for i in range(len(model.layers)):
#     layer = model.layers[i]
#     print('\n-----------', layer.name, '-----------')
#     print(len(layer.weights))
#     for i in range(len(layer.weights)):
#         print(layer.weights[i].read_value().numpy().shape)
#         print(layer.weights[i].read_value().numpy())

# path = "../../data/mnist/model.cpp"
# k = 0
# for i in range(len(path)):
#     if path[i] == '.':
#         k = i
#
# new_path = path[:k] + "_input." + path[k+1:]
# print(new_path)

# print("../data/models/mnist/model102.h5")
# model = tf.keras.models.load_model("../data/models/mnist/model102.h5")
# for i in range(len(model.layers)):
#     layer = model.layers[i]
#     print('\n-----------', layer.name, '-----------')
#     print(len(layer.weights))
#     for i in range(len(layer.weights)):
#         print(layer.weights[i].read_value().numpy().shape)
#         print(layer.weights[i].read_value().numpy())

# for layer in model.layers:
#     print("layer name: ",layer.name)
#     print(model.get_layer(name = layer.name).get_config())
    # print("strides: ",model.get_layer(name = layer.name).get_config()['strides'])
    # print("padding: ",model.get_layer(name = layer.name).get_config()['padding'])
