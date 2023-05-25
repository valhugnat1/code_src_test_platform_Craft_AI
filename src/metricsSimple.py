from craft_ai_sdk import *
import time




def metricsStep () :

    CraftAiSdk.record_metric_value("label", 12)

    time.sleep(10)
    CraftAiSdk.record_metric_value("label", 0.1409)
    
    time.sleep(10)
    CraftAiSdk.record_metric_value("label", 1/3)


    print ("Metrics are send")


