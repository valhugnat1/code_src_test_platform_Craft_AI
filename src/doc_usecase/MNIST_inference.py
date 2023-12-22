import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from craft_ai_sdk import CraftAiSdk

def inference(image, model_path, ground_truth):

    sdk = CraftAiSdk()

    # Save model in local context and load it
    sdk.download_data_store_object(model_path, "model.keras")
    model = load_model("model.keras")


    # Preprocess the input image
    input_image = tf.keras.preprocessing.image.load_img(image["path"], target_size=(28, 28), color_mode='grayscale')
    input_image = tf.keras.preprocessing.image.img_to_array(input_image)
    input_image = np.expand_dims(input_image, axis=0)
    input_image = input_image.astype('float32') / 255.0

    # Make predictions
    predictions = model.predict(input_image)

    # The predictions are probabilities, convert them to class labels
    predicted_class = int(np.argmax(predictions[0]))

    if ground_truth : 
        if ground_truth == predicted_class:
            sdk.record_metric_value("score", 1)
        else :
            sdk.record_metric_value("score", 0)

    return predicted_class
