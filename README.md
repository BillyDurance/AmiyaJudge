# AmiyaJudge
AmiyaJudge

## modol shape
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to
==================================================================================================
input_1 (InputLayer)            (None, 100, 100, 3)  0
__________________________________________________________________________________________________
conv2d_5 (Conv2D)               (None, 100, 100, 32) 2432        input_1[0][0]
__________________________________________________________________________________________________
batch_normalization_5 (BatchNor (None, 100, 100, 32) 128         conv2d_5[0][0]
__________________________________________________________________________________________________
conv2d_6 (Conv2D)               (None, 100, 100, 32) 25632       batch_normalization_5[0][0]
__________________________________________________________________________________________________
batch_normalization_6 (BatchNor (None, 100, 100, 32) 128         conv2d_6[0][0]
__________________________________________________________________________________________________
conv2d_2 (Conv2D)               (None, 100, 100, 32) 2432        input_1[0][0]
__________________________________________________________________________________________________
conv2d_7 (Conv2D)               (None, 100, 100, 32) 9248        batch_normalization_6[0][0]
__________________________________________________________________________________________________
batch_normalization_2 (BatchNor (None, 100, 100, 32) 128         conv2d_2[0][0]
__________________________________________________________________________________________________
batch_normalization_7 (BatchNor (None, 100, 100, 32) 128         conv2d_7[0][0]
__________________________________________________________________________________________________
conv2d_3 (Conv2D)               (None, 100, 100, 32) 9248        batch_normalization_2[0][0]
__________________________________________________________________________________________________
conv2d_8 (Conv2D)               (None, 100, 100, 32) 9248        batch_normalization_7[0][0]
__________________________________________________________________________________________________
batch_normalization_3 (BatchNor (None, 100, 100, 32) 128         conv2d_3[0][0]
__________________________________________________________________________________________________
batch_normalization_8 (BatchNor (None, 100, 100, 32) 128         conv2d_8[0][0]
__________________________________________________________________________________________________
conv2d_1 (Conv2D)               (None, 100, 100, 32) 896         input_1[0][0]
__________________________________________________________________________________________________
conv2d_4 (Conv2D)               (None, 100, 100, 32) 25632       batch_normalization_3[0][0]
__________________________________________________________________________________________________
conv2d_9 (Conv2D)               (None, 100, 100, 32) 1056        batch_normalization_8[0][0]
__________________________________________________________________________________________________
batch_normalization_1 (BatchNor (None, 100, 100, 32) 128         conv2d_1[0][0]
__________________________________________________________________________________________________
batch_normalization_4 (BatchNor (None, 100, 100, 32) 128         conv2d_4[0][0]
__________________________________________________________________________________________________
batch_normalization_9 (BatchNor (None, 100, 100, 32) 128         conv2d_9[0][0]
__________________________________________________________________________________________________
average_pooling2d_1 (AveragePoo (None, 99, 99, 32)   0           batch_normalization_1[0][0]
__________________________________________________________________________________________________
average_pooling2d_2 (AveragePoo (None, 99, 99, 32)   0           batch_normalization_4[0][0]
__________________________________________________________________________________________________
average_pooling2d_3 (AveragePoo (None, 99, 99, 32)   0           batch_normalization_9[0][0]
__________________________________________________________________________________________________
flatten_1 (Flatten)             (None, 313632)       0           average_pooling2d_1[0][0]
__________________________________________________________________________________________________
flatten_2 (Flatten)             (None, 313632)       0           average_pooling2d_2[0][0]
__________________________________________________________________________________________________
flatten_3 (Flatten)             (None, 313632)       0           average_pooling2d_3[0][0]
__________________________________________________________________________________________________
concatenate_1 (Concatenate)     (None, 940896)       0           flatten_1[0][0]
                                                                 flatten_2[0][0]
                                                                 flatten_3[0][0]
__________________________________________________________________________________________________
dense_1 (Dense)                 (None, 64)           60217408    concatenate_1[0][0]
__________________________________________________________________________________________________
dense_2 (Dense)                 (None, 3)            195         dense_1[0][0]
==================================================================================================
Total params: 60,304,579
Trainable params: 60,304,003
Non-trainable params: 576
__________________________________________________________________________________________________



