#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    text = dir(hidden_4)

    for word in text:
        if word[0:2] != "__":
            print("{:s}".format(word))
