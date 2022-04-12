
i = 0

while i < 10:
    print(i)
    i += 1
    print("jsme uvnitř cyklu")

print("konec cyklu")  

while True:
    slovo = input("Chceš skončit??")
    if slovo == "ano":
        break