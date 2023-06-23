from craft_ai_sdk import CraftAiSdk
import time
import math


def metricsList () :

    sdk = CraftAiSdk()
    sdk.record_metric_value("metricsimple", 12)
    sdk.record_metric_value("metricsimple2", 100)

    sdk.record_list_metric_values("metric", [0.172, 0.198, 0.112])


    time.sleep(5)
    sdk.record_list_metric_values("metric", 0.1409)
    sdk.record_list_metric_values("metric", 0.19)
    

    time.sleep(5)
    sdk.record_list_metric_values("autre", [12,2,-9,8,-4,-9,-4,2,0])

    for i in range (1, 500) : 

        sdk.record_list_metric_values("logx", math.log(i))


    print ("Metrics are send")


