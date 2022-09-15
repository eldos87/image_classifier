import tensorflow as tf
from tensorflow.keras.preprocessing import image

print("starts")
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3), kernel_initializer='he_uniform'),
    tf.keras.layers.MaxPool2D((2,2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu', kernel_initializer='he_uniform'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics= ['accuracy'])

train_datagen = image.ImageDataGenerator(shear_range=0.2, zoom_range=0.2, horizontal_flip=True, rescale=1./255)
val_datagen = image.ImageDataGenerator(rescale=1./255)

train_data = train_datagen.flow_from_directory(directory='cats_and_dogs_filtered/train',
                                               target_size=(64,64),
                                               batch_size=64,
                                               class_mode='binary')

val_data = val_datagen.flow_from_directory(directory='cats_and_dogs_filtered/validation',
                                           target_size=(64, 64),
                                           batch_size=64,
                                           class_mode='binary')

model.fit(train_data, epochs=2, validation_data=val_data)  #  steps_per_epoch, validation_steps give warning
                                                           # verbose other than 1(default) give error
model.save('eldos.h5')
print('model saved')


