def io_file(file_endpoint_i, file_datastore_i):
    res = ""

    with open(file_endpoint_i["path"], 'r') as f:
        contents = f.read()
        print(contents)
        res += contents

    with open(file_datastore_i["path"], 'r') as f:
        contents = f.read()
        print(contents)
        res += contents


    text_file = open('file_output.txt', 'wb')  # Open the file in binary mode
    text_file.write(res.encode('utf-8'))  # Encode the string to bytes
    text_file.close()


    file_endpoint_o = {"file_endpoint_o": {"path": "file_output.txt"}}

    return file_endpoint_o
