import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
from craft_ai_sdk import CraftAiSdk
import tensorflow as tf
from tensorflow.keras.datasets import fashion_mnist

def inference(image_num, model_path):

    sdk = CraftAiSdk()
    ima_path = './image_from_fashion_mnist.jpg'

    # Load the Fashion MNIST dataset
    (train_images, train_labels), (vali_images, vali_labels) = fashion_mnist.load_data()

    # save 1 image of validation dataset 
    image_to_save = Image.fromarray(vali_images[image_num]) 
    image_to_save.save(ima_path)    
    

    # Save model in local context and load it
    sdk.download_data_store_object(model_path, "model.keras")
    model = load_model("model.keras")


    # Preprocess the input image
    input_image = tf.keras.preprocessing.image.load_img(ima_path, target_size=(28, 28), color_mode='grayscale')
    input_image = tf.keras.preprocessing.image.img_to_array(input_image)
    input_image = np.expand_dims(input_image, axis=0)
    input_image = input_image.astype('float32') / 255.0

    # Make predictions
    predictions = model.predict(input_image)

    # The predictions are probabilities, convert them to class labels
    predicted_class = int(np.argmax(predictions[0]))

    if vali_labels[image_num] : 
        if vali_labels[image_num] == predicted_class:
            sdk.record_metric_value("score", 1)
        else :
            sdk.record_metric_value("score", 0)

    return {"predicted_class": predicted_class}
