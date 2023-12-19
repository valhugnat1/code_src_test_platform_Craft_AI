import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist
from craft_ai_sdk import CraftAiSdk

def trainer(learning_rate=0.001, nb_epoch=5, batch_size=64) : 

    sdk = CraftAiSdk()

    # Load and preprocess the MNIST dataset
    (train_images, train_labels), (test_images, test_labels) = mnist.load_data()
    train_images = train_images.reshape((60000, 28, 28, 1)).astype('float32') / 255
    test_images = test_images.reshape((10000, 28, 28, 1)).astype('float32') / 255
    train_labels = tf.keras.utils.to_categorical(train_labels)
    test_labels = tf.keras.utils.to_categorical(test_labels)

    # Build the neural network model
    model = models.Sequential()
    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.Flatten())
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(10, activation='softmax'))

    # Compile the model
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
                loss='categorical_crossentropy',
                metrics=['accuracy'])

    # Train the model
    for epoch in range(nb_epoch):  # Set the number of epochs
        model.fit(train_images, train_labels, epochs=1, batch_size=batch_size, validation_split=0.2)
        
        # Evaluate the model on the test set and log test metrics
        test_loss, test_acc = model.evaluate(test_images, test_labels)
        print({'epoch': epoch + 1, 'test_loss': test_loss, 'test_accuracy': test_acc})
        sdk.record_list_metric_values("test-loss",  test_loss)
        sdk.record_list_metric_values("test-accuracy", test_acc)


    # Evaluate the model on the test set
    test_loss, test_acc = model.evaluate(test_images, test_labels)
    print(f'Test accuracy: {test_acc}')
    sdk.record_metric_value("accuracy", test_acc)
    sdk.record_metric_value("loss", test_loss)

    # Save the model
    model.save('mnist-model.h5')
    sdk.upload_data_store_object('mnist_model.h5', 'product-doc/mnist_model.h5')