import os
import requests 
import pandas as pd
import tarfile
from sklearn import datasets
from craft_ai_sdk import CraftAiSdk, StepDependency, Input, Output

# Connect to the environment on craft AI platform 
sdk = CraftAiSdk(
    environment_url=os.environ.get("CRAFT_AI_ENVIRONMENT_URL"),
    sdk_token=os.environ.get("CRAFT_AI_ACCESS_TOKEN")
)

# Input and Output to step
dataset_input = Input(
    name="dataXFilePath",
		data_type="file",
    description="iris dataset",
		is_required=True
)

prediction_output = Output(
    name="prediction",
		data_type="file",
    description="result iris use case"
)


# Create a step with the iris ML code (with the code in the folder in the GitHub repository).
sdk.create_step(function_path="src/2_first_step_pipeline/iris_ml_platform.py",
	function_name="entryStepIris", 
	step_name="irisclassifier",
    input=[dataset_input],
	output=[prediction_output],
	description="This function creates a classifier model for iris and makes prediction on test data set",
	container_config = { 
	  "language": "python"
	}
)

# Create a pipeline with the previous step 
pipeline = sdk.create_pipeline(
    name="irisclassifier-pipeline",
		steps=[StepDependency(step_name="irisclassifier")],
    description="my first pipeline",
)


# Create a endpoint base on the existing pipeline
endpoint = sdk.create_endpoint(
	pipeline_name="irisClassifier-pipeline",
	endpoint_name="irisClassifier-endpoint"
)


# Download dataset
iris_X, iris_y = datasets.load_iris(return_X_y=True)

# Conversion to csv format
iris_X_df = pd.DataFrame(iris_X)
iris_X_df.to_csv("irisX.csv")

iris_y_df = pd.DataFrame(iris_y)
iris_y_df.to_csv("irisY.csv")

# Compress file 
tar = tarfile.open("irisDataSet.tar.gz", "w:gz")
for name in ["irisX.csv", "irisY.csv"]:
    tar.add(name)
tar.close()


# Trigger the endpoint with a post request 
endpointURL = "CRAFT_AI_ENVIRONMENT_URL/endpoints/" + endpoint["name"]
headers = {"Authorization": "EndpointToken " + endpoint["endpoint_token"]}
files = {'upload_file': open('irisDataSet.tar.gz','rb')}
requests.post(endpointURL, headers=headers, files=files)






# ---------------------------------------------------------------



# # Trigger the pipeline 
# exec_id = sdk.execute_pipeline(pipeline_name="irisClassifier-pipeline")["execution_id"]

# # Get information about the execution of pipeline (state and log)
# print (sdk.get_pipeline_execution(pipeline_name="irisClassifier-pipeline", execution_id=exec_id))
# print(sdk.get_pipeline_execution_logs(pipeline_name="irisClassifier-pipeline", execution_id=exec_id))





# ---------------------------------------------------------------

# files = {'upload_file': open('file.txt','rb')}
# values = {'DB': 'photcat', 'OUT': 'csv', 'SHORT': 'short'}

# r = requests.post(url, files=files, data=values)