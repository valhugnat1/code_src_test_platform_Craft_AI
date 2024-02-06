import numpy as np
import matplotlib.pyplot as plt
from craft_ai_sdk import CraftAiSdk


def generate_next_value(last_last_value, last_value, volatility=0.1):

    if last_value == 1 : 
        mean_value=0.9
    
    elif last_value == 0 : 
        mean_value=0.1
    else : 
        mean_value = last_value

    if last_value > last_last_value : 
        mean_value = mean_value + 0.05
    
    if last_value < last_last_value : 
        mean_value = mean_value - 0.05
    

    # Generate the next value from a normal distribution
    next_value = np.random.normal(loc=mean_value, scale=volatility)

    # Clip the result to be within [0, 1]
    next_value = max(0, min(1, next_value))

    sdk = CraftAiSdk()

    sdk.record_metric_value("recette_metric", next_value)
    sdk.record_metric_value("recette_metric_square", next_value**2)

    sdk.create_or_update_environment_variable("LAST_LAST_METRIC_VALUE", last_value)
    sdk.create_or_update_environment_variable("LAST_METRIC_VALUE", next_value)
    
    

""" 
if __name__ == "__main__":


    volatility_factor = 0.05  # Adjust as needed for more volatility
    num_iterations = 100
    last_last_value, last_value = 0.15, 0.25

    res_values = []

    res_values_2 = []

    for _ in range(num_iterations):
        last_last_value, last_value = generate_next_value(last_last_value, last_value, volatility_factor)
        res_values.append(last_value)
        res_values_2.append(last_value**2)


    # Plotting the values
    plt.plot(res_values, marker='o', linestyle='-', color='b')
    plt.plot(res_values_2, marker='o', linestyle='-', color='r')
    plt.title('Generated Values Over Time with Increased Volatility')
    plt.xlabel('Iterations')
    plt.ylabel('Generated Values')
    plt.show()
 """