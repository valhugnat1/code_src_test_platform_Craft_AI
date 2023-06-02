

def entryStepFileIo (entryFile) :
    print (entryFile)

    with open(entryFile["path"]) as f:
        contents = f.readlines()
        print (contents)


    # with open("file_output.txt", "wb") as text_file:
    #     text_file.write("Result of step send in file output :) ")
    #     # Assuming 'text_file' is the file object you're working with
    text_file = open('file_output.txt', 'wb')  # Open the file in binary mode
    text_file.write("Result of step send in file output :) ".encode('utf-8'))  # Encode the string to bytes
    text_file.close()

    
    fileOjb = {"resultFile" : {"path": "file_output.txt"}}

    return fileOjb
