

def entryStepMultipli (pathEntry) :
    print (pathEntry)

    with open(pathEntry["path"]) as f:
        contents = f.readlines()
        print (contents)


    with open("file_output.txt", "w") as text_file:
        text_file.write("Result of step send in file output :) ")
    
    fileOjb = {"resultFile" : {"path": "file_output.txt"}}

    return fileOjb