def automobili(marka, modelis, gads, nobraukums):
    return {
        "marka": marka,
        "modelis": modelis,
        "gads": gads,
        "nobraukums": nobraukums
    }
    
autins = automobili("Toyota", "Corolla", 2020, 15000)
print(autins)