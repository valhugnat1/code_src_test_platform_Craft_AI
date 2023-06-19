from craft_ai_sdk import CraftAiSdk
import time


def metricsList () :

    sdk = CraftAiSdk()

    sdk.record_list_metric_values("metric", [12])


    time.sleep(5)
    sdk.record_list_metric_values("metric", 0.1409)
    sdk.record_list_metric_values("metric", 0.19)
    
    time.sleep(5)
    sdk.record_list_metric_values("loss", [12,2,9,8,4,9,4,2,0])

    time.sleep(5)
    sdk.record_list_metric_values("autre", [12,2,-9,8,-4,-9,-4,2,0])

    print ("Metrics are send")


