from craft_ai_sdk import CraftAiSdk
import time


def metricsStep () :

    sdk = CraftAiSdk()

    sdk.record_metric_value("metric", 12)

    time.sleep(10)
    sdk.record_metric_value("accuracy", 0.1409)
    
    time.sleep(10)
    sdk.record_metric_value("loss", 1/3)


    print ("Metrics are send")


