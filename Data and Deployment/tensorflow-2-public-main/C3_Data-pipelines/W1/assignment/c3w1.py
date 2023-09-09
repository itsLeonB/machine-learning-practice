from os import getcwd
import tensorflow as tf
import tensorflow_datasets as tfds


# EXERCISE: encoding the labels using your own function for one-hot encoding

def my_one_hot(feature, label):
    # Encode the labels to one-hot using tf.one_hot with depth equal to total number of classes here which are rock, paper and scissors

    one_hot = tf.one_hot(label, depth=3, on_value=1.0, off_value=0.0)
    return feature, one_hot


# TESTING THE FUNCTION
_, one_hot = my_one_hot(["a", "b", "c", "a"], [1, 2, 3, 1])
print(one_hot)

# EXERCISE: Loading the rock, paper and scissors train and test dataset using tfds.load.

# Use data_dir=filepath as the dataset is already downloaded for you

# use 'filePath' if you are running on Coursera, ignore 'filePath' if you are running on Colab or your local machine
filePath = f"{getcwd()}/data"

train_data = tfds.load("rock_paper_scissors:3.*.*", data_dir=filePath, split = "train")
val_data = tfds.load("rock_paper_scissors:3.*.*", data_dir=filePath, split = "test")

# Testing train_data and val_data if loaded correctly

train_data_len=len(list(train_data))
val_data_len = len(list(val_data))

print(train_data_len)
print(val_data_len)

# EXERCISE: one-hot encode the train and validation labels using the function you defined earlier

# HINT - use map function https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map

train_data =

print(type(train_data))

# EXERCISE: Check the information about the dataset to see the dataset image shape

# HINT: Use with_info=True and data_dir (use 'data_dir' if running on Coursera, otherwise skip that parameter)
_,info = tfds.load(# YOUR CODE HERE)

# DO NOT EDIT THIS
print(info.features['image'].shape)

# EXERCISE: Train a simple CNN model on the dataset

train_batches = train_data.shuffle(100).batch(10)
validation_batches = val_data.batch(32)

model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(16, (3, 3), activation='relu', input_shape=# YOUR CODE HERE),
    # YOUR CODE HERE - Add a maxpool2d layer with kernel (2,2)
    # YOUR CODE HERE - Add a flatten layer
    tf.keras.layers.Dense(# YOUR CODE HERE)  # Remember there are 3 classes to classify and to use proper activation
])

model.summary()