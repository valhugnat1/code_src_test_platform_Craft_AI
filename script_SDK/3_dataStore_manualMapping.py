import os
import requests 
from craft_ai_sdk import CraftAiSdk
from craft_ai_sdk import DeploymentInputMapping, DeploymentOutputMapping


# Connect to the environment on craft AI platform 
sdk = CraftAiSdk(
    environment_url=os.environ.get("CRAFT_AI_ENVIRONMENT_URL"),
    sdk_token=os.environ.get("CRAFT_AI_ACCESS_TOKEN")
)


# Upload to data store
sdk.upload_data_store_object(
	filepath_or_buffer="./irisDataSet.tar.gz", 
	object_path_in_datastore="get_started/irisDataSet.tar.gz"
)


# Mapping
iris_mapping_input = DeploymentInputMapping(
	step_name="irisclassifier",
	step_input_name="dataSetPath",
	datastore_path="get_started/irisDataSet.tar.gz",
	required=True,
)

iris_mapping_output = DeploymentOutputMapping(
	step_name="irisclassifier",
	step_output_name="irisResult",
	datastore_path="get_started/irisResult.tar.gz",
)


# Endpoint manual mapping deployment 
endpoint = sdk.create_endpoint(
    pipeline_name="irisClassifier-pipeline",
    endpoint_name="irisClassifier-mapping-endpoint"
    input_mappings=[iris_mapping_input],
    output_mappings=[iris_mapping_output],
)


# Trigger new deployment
endpoint_URL = "CRAFT_AI_ENVIRONMENT_URL/endpoints/" + endpoint["name"]
headers = {"Authorization": "EndpointToken " + endpoint["endpoint_token"]}
files = {'upload_file': open('./irisDataSet.tar.gz','rb')}
requests.post(endpoint_URL, headers=headers, files=files)


# Download result 
CraftAiSdk.download_data_store_object(
	object_path_in_datastore="get_started/irisResult.tar.gz",
	filepath_or_buffer="./irisResult.tar.gz"
)




# ---------------------------------------------------------------


# Create Input and Output for a new step 

# # Create a new step 
# sdk.create_step(function_path="src/3_endpoint_sources_destination/iris_ml_platform_file_input.py",
# 	function_name="entryStepIris", 
# 	step_name="irisclassifier-file",
# 	description="This function create a classifier model for iris with data give in inside",
# 	container_config = { 
# 	  "language": "python"
# 	}
# )

# # Create a new pipeline with the step 
# pipeline = sdk.create_pipeline(
#     name="irisclassifier-file-pipeline",
# 		steps=[StepDependency(step_name="irisclassifier-file")],
#     description="Pipeline with input file",
# )

# # Create mapping object 

# # Deployment using new pipeline and mapping object 
