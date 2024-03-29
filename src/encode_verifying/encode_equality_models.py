import tensorflow as tf
from larq.quantizers import SteSign
from pathlib import Path

from src.encode_model.encode_model import Encode, print_clauses


def encode_equality_models(path1, path2, input_shape=tuple([28, 28, 1])):
    model1 = tf.keras.models.load_model(path1, custom_objects={"custom_activation": SteSign})
    model2 = tf.keras.models.load_model(path2, custom_objects={"custom_activation": SteSign})
    encode1 = Encode(model1, input_shape=input_shape)
    encode2 = Encode(model2, id_start=encode1.all_vars[-1].id-encode1.output_vars_layers[0][1]+1, input_shape=input_shape)
    encode2.change_input_vars(1)

    assert encode1.output_layers_shape[-1] == encode2.output_layers_shape[-1]
    assert encode1.output_vars_layers[-1][1] == encode2.output_vars_layers[-1][1]

    clauses = []
    res_clause = []
    for i in range(encode1.output_vars_layers[-1][1]):
        var = encode2.create_var('equal').id
        res_clause.append(var)
        clauses.append([encode1.output_vars_layers[-1][0] + i, encode2.output_vars_layers[-1][0] + i, -var])
        clauses.append([encode1.output_vars_layers[-1][0] + i, -(encode2.output_vars_layers[-1][0] + i), var])
        clauses.append([-(encode1.output_vars_layers[-1][0] + i), encode2.output_vars_layers[-1][0] + i, var])
        clauses.append([-(encode1.output_vars_layers[-1][0] + i), -(encode2.output_vars_layers[-1][0] + i), -var])
    clauses.append(res_clause)

    path = "../../data/CNFs/" + Path(path1).parents[0].stem + "/equality_" + Path(path1).stem + "_and_" + Path(path2).stem + ".cnfcc"
    file = open(path, 'w')
    file.write('p cnf ' + str(len(encode1.all_vars) + len(encode2.all_vars) - encode1.output_vars_layers[0][1]) + ' ' + str(len(encode1.clauses) + len(encode1.constraints) + len(encode2.clauses) + len(encode2.constraints) + len(clauses)) + '\n')
    print_clauses(clauses, file)
    file.close()

    encode1.save(path, mode='a')
    encode2.save(path, mode='a')


# encode_equality_models("../../data/models/mnist/model0.h5", "../../data/models/mnist/model0.h5")
# encode_equality_models("../../data/models/mnist/model0.h5", "../../data/models/mnist/model4.h5")
# encode_equality_models("../../data/models/mnist/model4.h5", "../../data/models/mnist/model0.h5")
# encode_equality_models("../../data/models/mnist/model4.h5", "../../data/models/mnist/model4.h5")
#
# encode_equality_models("../../data/models/mnist/model0.h5", "../../data/models/mnist/model5.h5")
# encode_equality_models("../../data/models/mnist/model5.h5", "../../data/models/mnist/model0.h5")
# encode_equality_models("../../data/models/mnist/model5.h5", "../../data/models/mnist/model5.h5")
#
# encode_equality_models("../../data/models/mnist/model5.h5", "../../data/models/mnist/model4.h5")
# encode_equality_models("../../data/models/mnist/model4.h5", "../../data/models/mnist/model5.h5")

# encode_equality_models("../../data/models/mnist/model0.h5", "../../data/models/mnist/model6.h5")
# encode_equality_models("../../data/models/mnist/model5.h5", "../../data/models/mnist/model6.h5")

# encode_equality_models("../../data/models/mnist/model0.h5", "../../data/models/mnist/model7.h5")
# encode_equality_models("../../data/models/mnist/model0.h5", "../../data/models/mnist/model8.h5")
# encode_equality_models("../../data/models/mnist/model0.h5", "../../data/models/mnist/model9.h5")

# encode_equality_models("../../data/models/mnist/model6.h5", "../../data/models/mnist/model7.h5")
# encode_equality_models("../../data/models/mnist/model9.h5", "../../data/models/mnist/model7.h5")
# encode_equality_models("../../data/models/mnist/model8.h5", "../../data/models/mnist/model7.h5")
# encode_equality_models("../../data/models/mnist/model10.h5", "../../data/models/mnist/model7.h5")

# encode_equality_models("../../data/models/cifar10/model5.h5", "../../data/models/cifar10/model6.h5", input_shape=tuple([32, 32, 3]))
# encode_equality_models("../../data/models/cifar10l/model5.h5", "../../data/models/cifar10l/model6.h5", input_shape=tuple([32, 32, 3, 8]))
#
# encode_equality_models("../../data/models/cifar10l/model0.h5", "../../data/models/cifar10l/model4.h5", input_shape=tuple([32, 32, 3, 8]))
# encode_equality_models("../../data/models/cifar10/model0.h5", "../../data/models/cifar10/model4.h5", input_shape=tuple([32, 32, 3]))
#
# encode_equality_models("../../data/models/my/model11.h5", "../../data/models/my/model12.h5", input_shape=tuple([4]))

encode_equality_models("../../data/models/mnistl/model0.h5", "../../data/models/mnistl/model4.h5", input_shape=(28, 28, 8))
