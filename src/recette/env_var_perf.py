
from craft_ai_sdk import CraftAiSdk

def env_var_perf(value_i) :

    sdk = CraftAiSdk()

    value = int(value_i)

    print(sdk.list_environment_variables())

    sdk.create_or_update_environment_variable("PROD_PERF_TESTING", value**2)

    return {"value_o": value+10}

