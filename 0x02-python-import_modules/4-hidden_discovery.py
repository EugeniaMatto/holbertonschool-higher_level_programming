#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    lista = dir(hidden_4)
    for i in lista:
        if i[:2] != "__":
            print(f"{i}")
