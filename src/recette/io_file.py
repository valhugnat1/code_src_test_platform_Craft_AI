def entryStepFileIo(file_endpoint_i, file_datastore_i):
    res = ""

    with open(file_endpoint_i["path"], 'r') as f:
        contents = f.read()
        print(contents)
        res += contents

    with open(file_datastore_i["path"], 'r') as f:
        contents = f.read()
        print(contents)
        res += contents

    with open('file_output.txt', 'w', encoding='utf-8') as text_file:
        text_file.write(res)

    file_endpoint_o = {"resultFile": {"path": "file_output.txt"}}

    return file_endpoint_o
