import os
from craft_ai_sdk import CraftAiSdk
from craft_ai_sdk import StepDependency

# Connect to the environment on craft AI platform 
sdk = CraftAiSdk(
    environment_url=os.environ.get("CRAFT_AI_ENVIRONMENT_URL"),
    sdk_token=os.environ.get("CRAFT_AI_ACCESS_TOKEN")
)

# Create a step with the iris ML code (with the code in the folder in the GitHub repository).
sdk.create_step(function_path="src/2_first_step_pipeline/iris_ml_platform.py",
	function_name="entryStepIris", 
	step_name="irisclassifier",
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

# Trigger the pipeline 
exec_id = sdk.execute_pipeline(pipeline_name="irisClassifier-pipeline")["execution_id"]

# Get information about the execution of pipeline (state and log)
print (sdk.get_pipeline_execution(pipeline_name="irisClassifier-pipeline", execution_id=exec_id))
print(sdk.get_pipeline_execution_logs(pipeline_name="irisClassifier-pipeline", execution_id=exec_id))

