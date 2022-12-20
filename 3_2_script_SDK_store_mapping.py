import os
from craft_ai_sdk import CraftAiSdk
from craft_ai_sdk import StepDependency
from sklearn import datasets
import pandas as pd

# Connect to the environment on craft AI platform 
sdk = CraftAiSdk(
    environment_url=os.environ.get("CRAFT_AI_ENVIRONMENT_URL"),
    sdk_token=os.environ.get("CRAFT_AI_ACCESS_TOKEN")
)


# Download dataset
iris_X, iris_y = datasets.load_iris(return_X_y=True)

# Conversion to csv format
iris_X_df = pd.DataFrame(iris_X)
iris_X_df.to_csv("irisX.csv")

iris_y_df = pd.DataFrame(iris_y)
iris_y_df.to_csv("irisY.csv")

# Upload to the data store
sdk.upload_data_store_object(
	filepath_or_buffer="./irisX.csv", 
	object_path_in_datastore="get_started/irisX.csv"
)

sdk.upload_data_store_object(
	filepath_or_buffer="./irisY.csv", 
	object_path_in_datastore="get_started/irisY.csv"
)

# Create Input and Output for a new step 

# Create a new step 
sdk.create_step(function_path="src/3_endpoint_sources_destination/iris_ml_platform_file_input.py",
	function_name="entryStepIris", 
	step_name="irisclassifier-file",
	description="This function create a classifier model for iris with data give in inside",
	container_config = { 
	  "language": "python"
	}
)

# Create a new pipeline with the step 
pipeline = sdk.create_pipeline(
    name="irisclassifier-file-pipeline",
		steps=[StepDependency(step_name="irisclassifier-file")],
    description="Pipeline with input file",
)

# Create mapping object 

# Deployment using new pipeline and mapping object 
