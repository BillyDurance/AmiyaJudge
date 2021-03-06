from keras.optimizers import Adam
from keras import Model, Input
from keras.layers import *
import tensorflow as tf
import time
import os
#from getData import *
from datasetreader import *
#os.environ["CUDA_VISIBLE_DEVICES"] = "3"
#hyper things
train_epochs = 10
batch_size = 10
learning_rate = 0.01
test_ratio = 0.1
config = tf.ConfigProto()
# 指定可见显卡
config.gpu_options.visible_device_list="1"
#不满显存, 自适应分配
config.gpu_options.allow_growth=True
#the picture size
imginput = Input(shape=(100, 100, 1))

#imgtube1
imgtube1 = Conv2D(filters=32, kernel_size=3, padding='same',
                  activation='relu')(imginput)
imgtube1 = BatchNormalization()(imgtube1)
imgtube1 = AveragePooling2D(padding="valid",
                            pool_size=2,
                            data_format="channels_last",
                            strides=1)(imgtube1)
imgtube1 = Flatten()(imgtube1)

#imgtube2
imgtube2 = Conv2D(filters=32, kernel_size=5, padding='same',
                  activation='relu')(imginput)
imgtube2 = BatchNormalization()(imgtube2)
imgtube2 = Conv2D(filters=32, kernel_size=3, padding='same',
                  activation='relu')(imgtube2)
imgtube2 = BatchNormalization()(imgtube2)
imgtube2 = Conv2D(filters=32, kernel_size=5, padding='same',
                  activation='relu')(imgtube2)
imgtube2 = BatchNormalization()(imgtube2)
imgtube2 = AveragePooling2D(padding="valid",
                            pool_size=2,
                            data_format="channels_last",
                            strides=1)(imgtube2)
imgtube2=Dropout(0.2)(imgtube2)
imgtube2 = Flatten()(imgtube2)

#imgtube3
imgtube3 = Conv2D(filters=32, kernel_size=5, padding='same',
                  activation='relu')(imginput)
imgtube3 = BatchNormalization()(imgtube3)
imgtube3 = Conv2D(filters=32, kernel_size=5, padding='same',
                  activation='relu')(imgtube3)
imgtube3 = BatchNormalization()(imgtube3)
imgtube3 = Conv2D(filters=32, kernel_size=3, padding='same',
                  activation='relu')(imgtube3)
imgtube3 = BatchNormalization()(imgtube3)
imgtube3 = Conv2D(filters=32, kernel_size=3, padding='same',
                  activation='relu')(imgtube3)
imgtube3 = BatchNormalization()(imgtube3)
imgtube3 = Conv2D(filters=32, kernel_size=1, padding='same',
                  activation='relu')(imgtube3)
imgtube3 = BatchNormalization()(imgtube3)
imgtube3 = AveragePooling2D(padding="valid",
                            pool_size=2,
                            data_format="channels_last",
                            strides=1)(imgtube3)
imgtube3 = BatchNormalization()(imgtube3)
imgtube3 = Conv2D(filters=32, kernel_size=3, padding='same',
                  activation='relu')(imgtube3)
imgtube3 = BatchNormalization()(imgtube3)
imgtube3 = Conv2D(filters=32, kernel_size=3, padding='same',
                  activation='relu')(imgtube3)
imgtube3 = BatchNormalization()(imgtube3)
imgtube3 = Conv2D(filters=32, kernel_size=1, padding='same',
                  activation='relu')(imgtube3)
imgtube3 = BatchNormalization()(imgtube3)
imgtube3 = AveragePooling2D(padding="valid",
                            pool_size=2,
                            data_format="channels_last",
                            strides=1)(imgtube3)
imgtube3 = BatchNormalization()(imgtube3)
imgtube3 = Conv2D(filters=32, kernel_size=3, padding='same',
                  activation='relu')(imgtube3)
imgtube3 = BatchNormalization()(imgtube3)
imgtube3 = Conv2D(filters=32, kernel_size=3, padding='same',
                  activation='relu')(imgtube3)
imgtube3 = BatchNormalization()(imgtube3)
imgtube3 = Conv2D(filters=32, kernel_size=1, padding='same',
                  activation='relu')(imgtube3)
imgtube3 = BatchNormalization()(imgtube3)
imgtube3 = AveragePooling2D(padding="valid",
                            pool_size=2,
                            data_format="channels_last",
                            strides=1)(imgtube3)
imgtube3 = Dropout(0.2)(imgtube3)                    
imgtube3 = Flatten()(imgtube3)

#combine network
comnet = concatenate([imgtube1, imgtube2, imgtube3])
comnet = Dense(256, activation='relu')(comnet)
comnet = Dense(128, activation='relu')(comnet)
comnet = Dense(64, activation='relu')(comnet)
output = Dense(3, activation='softmax')(comnet)

#difine the modol
model = Model(inputs=[imginput], outputs=[output])
model.summary()

model.compile(optimizer=Adam(learning_rate),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

#TODO get the data , train the modol


x_data,y_data=getdate("tfrecord_train.tfrecords")
# print(x_data.shape)
# print(y_data.shape)
# print(x_data,y_data)
model.fit(np.array(x_data),np.array(y_data),validation_split=0.3, epochs=30, batch_size=100,shuffle=True)