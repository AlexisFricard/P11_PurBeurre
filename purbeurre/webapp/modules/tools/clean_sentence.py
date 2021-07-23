""" TO CLEAN A GIVEN SENTENCE """

def clean_query(query):
    print(type(query))
    if query == "" or query == " ":
        return None
    else:
        try:
            code = int(query)
            return code
        except ValueError:
            query = remove_special_char(query, "add_space")
            return query

def remove_special_char(msg, params):
    msg = msg.lower()
    for char in msg:
        if char in "[\"/\\:?!-}><(){,]&":
            if params == "all":
                msg = msg.replace(i, "")
            # To keep separate {it's -> it s etc..}
            elif params == "add_space":
                if char in ",-\"":
                    msg = msg.replace(char, " ")
                else:
                    msg = msg.replace(char, "")
    return msg
