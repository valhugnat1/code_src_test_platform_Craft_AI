from craft_ai_sdk import CraftAiSdk
import time
import random

def metricsStep () :

    sdk = CraftAiSdk()

    sdk.record_metric_value("metric", random.randint(0,10))

    sdk.record_metric_value("accuracy", random.random())
    
    sdk.record_metric_value("loss", time.time()-1693225620)


    print ("Metrics are send")


