```
32/32 [==============================] - 0s 5ms/step - loss: 2.0624 - accuracy: 0.8380
Test accuracy 83.80 %
+sequential_1 stats------------------------------------------------------------------------------------+
| Layer                            Input prec.          Outputs  # 1-bit  # 32-bit  Memory  1-bit MACs |
|                                        (bit)                       x 1       x 1    (kB)             |
+------------------------------------------------------------------------------------------------------+
| 0/Init/Activation                          -  (-1, 28, 28, 8)        0         0       0           ? |
| 1/Flatten/Flatten                          -       (-1, 6272)        0         0       0           0 |
| 2/QuantDense/QuantDense                    1        (-1, 128)   802816       128   98.50      802816 |
| 2/QuantDense/BatchNormalization            -        (-1, 128)        0       256    1.00           0 |
| 2/QuantDense/Activation                    -        (-1, 128)        0         0       0           ? |
| 3/Output/QuantDense                        1         (-1, 10)     1280         0    0.16        1280 |
| 3/Output/Activation                        -         (-1, 10)        0         0       0           ? |
+------------------------------------------------------------------------------------------------------+
| Total                                                           804096       384   99.66      804096 |
+------------------------------------------------------------------------------------------------------+
```