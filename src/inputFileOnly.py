

def inputFileOnly (entryFile) :
    print (entryFile)

    with open(entryFile["path"]) as f:
        contents = f.readlines()
        print (contents)

    print("Done !")