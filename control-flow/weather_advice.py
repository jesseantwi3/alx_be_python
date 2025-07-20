
weather = (input("Whats the weather like today?(sunny/rainy/cold): ")).lower()


if weather == "sunny":
    print("Wear a t-shirt And sunglasses")
elif weather == "rainy":
    print("Dont forget your umbrella And raincoat")
elif weather == "cold":
    print("Make sure to wear warm coat And scarf")
else:
    print("sorry, i dont have recommendations For this weather")
