import numpy as np
import pandas as pd

def two_o_file_datastore () :

    # Define file into local step contenaire 
    path_text = "file_text_output.txt"
    path_matrix = "confusion_matrix.csv"


    # Create a fake confusion matrix into .csv file
    confusion_matrix = np.array([[100, 20, 5],
                                [30, 150, 10],
                                [10, 5, 200]])
    class_labels = ['Class A', 'Class B', 'Class C'] # Define the class labels
    df = pd.DataFrame(confusion_matrix, index=class_labels, columns=class_labels) # Create a DataFrame from the confusion matrix
    df.to_csv(path_matrix, index=True, header=True) # Save the DataFrame as a CSV file


    # Create .txt file
    text_file = open(path_text, 'wb')  # Open the file in binary mode
    text_file.write("Result of step send in file output :) ".encode('utf-8'))  # Encode the string to bytes
    text_file.close()


    # Return the path of the file in the container of the current step execution.
    fileOjb = {"txtFile" : {"path": path_text}, "csvFile" : {"path": path_matrix}}
    return fileOjb
