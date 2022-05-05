pocasi = {
    "pondělí": {
        "teplota": [ {
            "a": 1,
            "b": 2,
            "c": 3
        }, {
            "a": 4,
            "b": 5,
            "c": 6
        }, {
            "a": 11,
            "b": 12,
            "c": 13
        }],
        "srážky": 1.5,
        "bio": 2
    },
    "úterý": {
        "teplota": [17, 19, 21],
        "srážky": 1.2,
        "bio": 1
    },
    "středa": {
        "teplota": [15, 23, 14],
        "srážky": 0,
        "bio": 2
    }
}

print(pocasi["úterý"]["bio"])
print(pocasi["pondělí"]["teplota"][0])
print(pocasi["středa"]["teplota"][1])

print(pocasi["pondělí"]["teplota"][1]["a"])
print(pocasi["pondělí"]["teplota"][2]["c"])
