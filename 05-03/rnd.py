import random

anglictina = {
    "dveře": "door",
    "stůl": "table",
    "židle": "chair",
    "dům": "house",
    "pes": "dog"
}

for i in range(5):
    klic = random.choice(list(anglictina.keys()))
    print(f"Česky: {klic} - anglicky: {anglictina[klic]}")