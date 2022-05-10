
def pig_latin_lowercase(word):
    if word[0] in "aeiouy":
        #první je smaohláska
        return word + "way"
    else:
        #první je souhláska
        return word[1:] + word[0] + "ay"
    
def pig_latin_anycase(word):
    first_letter = word[0]
    if first_letter.upper() == first_letter:
        was_capital = True
    else:
        was_capital = False   

    #KOMPLET TO PREVEĎ NA MALÁ PÍSMENA
    word = word.lower()

    #ZAVOLEJ pig_latin_lowercase(word) A ULOŽ SI VÝSLEDEK
    result = pig_latin_lowercase(word)

    #POKUD BYLO PRVNÍ PÍSMENO VELKÉ, UDĚLĚJ HO VE VÝSLEDKU ZASE VELKÉ
    if was_capital:
        result = result.capitalize()
    #VRAŤ VÝSLEDEK
    return result

def pig_latin_anycase_shorter_version(word):
    first_letter = word[0]
    result = pig_latin_lowercase(word.lower())
    if first_letter.upper() == first_letter:
        result = result.capitalize()
    return result

# tohle jsou testy na ověření, jeslti funkce pracuje správně 
# (zatím nepracuje ... ale to zlepšíme)
print(pig_latin_lowercase("elephant"))
print(pig_latin_lowercase("cat"))
print(pig_latin_lowercase("octopus"))
print(pig_latin_lowercase("telephone"))

print(pig_latin_anycase("telephone"))
print(pig_latin_anycase("Telephone"))
print(pig_latin_anycase("octopus"))
print(pig_latin_anycase("Octopus"))

