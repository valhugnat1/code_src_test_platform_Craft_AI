

def cypress_deploy_test (number, text, entryFile) :
    print (entryFile)
    """ 
    with open(entryFile["path"]) as f:
        contents = f.readlines()
        print (contents)
     """

    text_file = open('file_output.txt', 'wb')  # Open the file in binary mode
    text_file.write((text*number).encode('utf-8'))  # Encode the string to bytes
    text_file.close()

    
    fileOjb = {"resultFile" : {"path": "file_output.txt"}}

    return fileOjb


if __name__ == "__main__":
    cypress_deploy_test(2, "", "dff")