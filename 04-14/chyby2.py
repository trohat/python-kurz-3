
muj_string = "a"

try:
    while True:
        muj_string = muj_string + muj_string
        print(len(muj_string))
except MemoryError:
    print("Hmmm, došla ti paměť... :(")