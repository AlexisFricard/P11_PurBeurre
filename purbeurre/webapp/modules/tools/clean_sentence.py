""" TO CLEAN A GIVEN SENTENCE """


def clean_query(query):

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
                msg = msg.replace(char, "")
            elif params == "add_space":
                if char in ",-\"'":
                    msg = msg.replace(char, " ")
                else:
                    msg = msg.replace(char, "")
    return msg


def clean_accents(query):

    a_acc = ["à", "â", "ä"]
    e_acc = ["é", "è", "ê", "ë"]
    i_acc = ["î", "ï"]
    o_acc = ["ô", "ö"]
    u_acc = ["ù", "û", "ü"]

    for char in query:
        rep = False
        if char in a_acc:
            rep = "a"
        elif char in e_acc:
            rep = "e"
        elif char in i_acc:
            rep = "i"
        elif char in o_acc:
            rep = "o"
        elif char in u_acc:
            rep = "u"

        if rep:
            query = query.replace(char, rep)

    return query


def clean_space(query, replacer):
    # CHECK THE FIRST CHAR:
    if query[0] == " ":
        query = query[1:]
    for char in query:
        if char == " ":
            query = query.replace(char, replacer)

    return query
