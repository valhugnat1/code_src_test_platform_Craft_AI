

def entryStepFileIo (entryFile) :
    print (entryFile)

    with open(entryFile["path"]) as f:
        contents = f.readlines()
        print (contents)


    text_file = open('file_output.txt', 'wb')  # Open the file in binary mode
    text_file.write("Result of step send in file output :) ".encode('utf-8'))  # Encode the string to bytes
    text_file.close()

    
    fileOjb = {"resultFile" : {"path": "file_output.txt"}}

    return fileOjb
