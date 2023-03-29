import json
import sys
import os
from sklearn import datasets


def my_function (number, file) :
    print (number, file)

    with open(file["path"]) as f:
        contents = f.readlines()
        print (contents)

    _, iris_y = datasets.load_iris(return_X_y=True)
    

    # return iris_y
    return ["Return step array", "output elem", "other elem"]



if __name__ == "__main__":

    # Pre-processing: Inputs
    parameters_inputs = json.loads(sys.argv[1])
    files_inputs = json.loads(sys.argv[2])

    result = my_function(**parameters_inputs, **files_inputs)

    # Post-processing: Outputs
    output_dir = '/app'
    with open(os.path.join(output_dir, 'output_var'), 'w') as f:
        json.dump(result, f)
        
    with open(os.path.join(output_dir, 'output_file'), 'w') as f:
        f.write('\n'.join(f'* {item}' for item in result))