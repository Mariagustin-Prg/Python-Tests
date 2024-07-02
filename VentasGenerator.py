import pandas as pd
import numpy as np
from datetime import date
import random

while True:
    cantidad_de_ordenes = input("Ingrese la cantidad de registros que desea generar: ")

    try:
        int_cantidad_de_ordenes = int(cantidad_de_ordenes)
        break

    except Exception:
        continue





products_category = {
    "Frutas": ("Manzanas", "Naranjas", "Bananas", "Peras", "Frutillas", "Mandarinas", "Kiwis"),
    "Vegetales": ("Tomates", "Papas", "Zanahorias", "Cebollas", "Morrón", "Zapallitos", "Lechugas"),
    "Utensilios": ("Cuchillo", "Tabla", "Ollas", "Sartén", "Cucharas", "Tenedores"),
    "Otros": ("Botellas", "Guantes", "Delantal", "Tuppers")
}

data = {
    "OrderID": [0],
    "Product": ["Papas"],
    "Category": ["Vegetales"],
    "Quantify": [14],
    "Price Each": [3],
    "Total Price": [42],
    "Order Date": [date(2022, 4, 21)]
}



def Generator() -> None:
    
    data["OrderID"].append(data["OrderID"][-1] + 1)

    categoryID = random.randint(0, len(products_category) - 1)
    category = list(products_category.keys())[categoryID]


    list_products = products_category[category]

    product = list_products[random.randint(0, len(list_products) - 1)]

    
    data["Product"].append(product)
    data["Category"].append(category)

    quantify = random.randint(1,100)

    data["Quantify"].append(quantify)

    prices = np.arange(0.1, 40.01, 0.01)

    price = round(prices[random.randint(0, len(prices) - 1)], 2)

    data["Price Each"].append(price)

    data["Total Price"].append(quantify * price)

    years = (2022, 2023, 2021)
    months = tuple(range(1, 13))
    days = tuple(range(1, 32))

    while True:
        try:
            year = years[random.randint(0, len(years) - 1)]
            month = months[random.randint(0, len(months) - 1)]
            day = days[random.randint(0, len(days) - 1)]

            order_date = date(year, month, day)

            break

        except Exception:
            continue

    data["Order Date"].append(order_date)



for i in range(int_cantidad_de_ordenes):
    Generator()

    try:
        if i % (int_cantidad_de_ordenes // 10) <= 0.4:
            print(round(i * 100 / int_cantidad_de_ordenes, 2), "% Completado.",
                f"{i} registros creadas.")
    except ZeroDivisionError:
        print(f"{i} registros realizados.")


df = pd.DataFrame(data)

df.to_csv("RandomDataGenerated.csv", index= False)
print(f"Tabla exportada. {int_cantidad_de_ordenes} incluidos.")