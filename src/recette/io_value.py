def io_value (num_i, text_i, json_i): 
    
    json_i.update({"last": True})

    text_o = text_i*num_i

    return {"text_o": text_o, "json_o": json_i, "bool_o": True}
