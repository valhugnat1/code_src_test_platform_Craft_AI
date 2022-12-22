import os
import requests 
from craft_ai_sdk import CraftAiSdk
from craft_ai_sdk import StepDependency
from craft_ai_sdk import Input, Output

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

# Trigger the endpoint with a post request 
endpointURL = "CRAFT_AI_ENVIRONMENT_URL/endpoints/" + endpoint["name"]
headers = {"Authorization": "EndpointToken " + endpoint["endpoint_token"]}
requests.post(endpointURL, headers=headers)






# ---------------------------------------------------------------



# # Trigger the pipeline 
# exec_id = sdk.execute_pipeline(pipeline_name="irisClassifier-pipeline")["execution_id"]

# # Get information about the execution of pipeline (state and log)
# print (sdk.get_pipeline_execution(pipeline_name="irisClassifier-pipeline", execution_id=exec_id))
# print(sdk.get_pipeline_execution_logs(pipeline_name="irisClassifier-pipeline", execution_id=exec_id))

