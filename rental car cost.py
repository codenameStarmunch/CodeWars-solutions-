# Lol

def rental_car_cost(d):
    return (d * 40) if d < 3 else (d * 40) - 20 if d > 3 and d < 7 else (d * 40) - 50


print(rental_car_cost(7))