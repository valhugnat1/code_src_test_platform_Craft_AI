

def entryStepFileIo (entryFile) :
    print (entryFile)

    with open(entryFile["path"]) as f:
        contents = f.readlines()
        print (contents)


    with open("file_output.txt", "wb") as text_file:
        text_file.write("Result of step send in file output :) ")
    
    fileOjb = {"resultFile" : {"path": "file_output.txt"}}

    return fileOjb 