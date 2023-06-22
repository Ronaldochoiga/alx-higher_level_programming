#!/usr/bin/python3

if __name__ == "__main__":

    import hidden_4

    nmes = dir(hidden_4)
    for name in nmes:
        if name[:2] != "__":
            print(name)
