import os
from craft_ai_sdk import CraftAiSdk
import requests 

# Connect to the environment on craft AI platform 
sdk = CraftAiSdk(
    environment_url=os.environ.get("CRAFT_AI_ENVIRONMENT_URL"),
    sdk_token=os.environ.get("CRAFT_AI_ACCESS_TOKEN")
)

# Create a endpoint base on the existing pipeline
endpoint = sdk.create_endpoint(
	pipeline_name="irisClassifier-pipeline",
	endpoint_name="irisClassifier-endpoint"
)

# Trigger the endpoint with a post request 
endpoint = "CRAFT_AI_ENVIRONMENT_URL/endpoints/" + endpoint["name"]
headers = {"Authorization": "EndpointToken " + endpoint["endpoint_token"]}
requests.post(endpoint, headers=headers)