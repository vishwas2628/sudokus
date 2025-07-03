import os
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential,load_model
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

# Path to your assets folder (should have subfolders 0,1,...,9)
# Use relative paths for portability
base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_dir, 'assets') 
'''
import kagglehub

# Download latest version
path = kagglehub.dataset_download("kshitijdhama/printed-digits-dataset")

print("Path to dataset files:", path)
'''
checkpoint_path = os.path.join(base_dir, 'my_new_Model.h5')

# Data generator for loading images
datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2,
    rotation_range=10,
    width_shift_range=0.1,
    height_shift_range=0.1,
    zoom_range=0.1
)

train_gen = datagen.flow_from_directory(
    data_dir,
    target_size=(28, 28),
    color_mode='grayscale',
    batch_size=32,
    class_mode='categorical',
    subset='training',
    shuffle=True
)

val_gen = datagen.flow_from_directory(
    data_dir,
    target_size=(28, 28),
    color_mode='grayscale',
    batch_size=32,
    class_mode='categorical',
    subset='validation',
    shuffle=True
)

# Load the previous model if it exists, else create a new one
#checkpoint_path = r'C:\Users\HP\OneDrive\Desktop\sudokus\sudoku\sudokusolver\Resources\myModel.h5'
if os.path.exists(checkpoint_path):
    model = load_model(checkpoint_path)
    print("Loaded existing model for further training.")
else:
    model = Sequential([
        Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
        BatchNormalization(),
        Conv2D(64, (3,3), activation='relu'),
        BatchNormalization(),
        MaxPooling2D(2,2),
        Dropout(0.25),
        Conv2D(128, (3,3), activation='relu'),
        BatchNormalization(),
        MaxPooling2D(2,2),
        Dropout(0.25),
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(10, activation='softmax')
    ])
    model.compile(optimizer=Adam(learning_rate=0.001), loss='categorical_crossentropy', metrics=['accuracy'])

# Callbacks for best weights and early stopping
# checkpoint_path = r'C:\Users\HP\OneDrive\Desktop\sudokus\sudoku\sudokusolver\Resources\myModel_new.h5'
callbacks = [
    ModelCheckpoint(checkpoint_path, monitor='val_accuracy', save_best_only=True, verbose=1),
    #EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True, verbose=1)
]

# Training
model.fit(
    train_gen,
    epochs=60,  # longer training
    validation_data=val_gen,
    callbacks=callbacks
)

# Save the final model (optional, as best is already saved)
model.save(checkpoint_path)