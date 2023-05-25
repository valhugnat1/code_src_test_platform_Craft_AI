from craft_ai_sdk import *


def metricsStep () :

    CraftAiSdk.record_metric_value("label", 12)


    print ("Metrics are send")
