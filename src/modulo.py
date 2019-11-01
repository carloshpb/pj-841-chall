def func(pedras="", joia=""):
    # Escreva seu codigo aqui
    quantity = 0
    for stone in pedras:
        quantity += joia.count(stone)
    return quantity