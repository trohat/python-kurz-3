
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

def pig_latin_punctuation(word):
    #ZJISTI, JESTLI MÁ TEČKU NEBO ČÁRKU
    last_letter = word[-1]
    #TEČKU NEBO ČÁRKU DEJ PRYČ
    if last_letter in ".,!?":
        word = word[:-1]
    else:
        last_letter = ""
    #PŘEVEĎ DO PIG LATIN POMOCÍ UŽ HOTOVÝCH FUNKCÍ
    word = pig_latin_anycase_shorter_version(word)
    #POKUD BYLA TEČKA NEBO ČÁRKA, VRAŤ JI TAM
    word = word + last_letter
    return word

def pig_latin_sentence(sentence):
    sentence_list = sentence.split()
    #print(sentence_list)
    new_sentence_list = []
    for word in sentence_list:
        transformed_word = pig_latin_punctuation(word)
        new_sentence_list.append(transformed_word)
    result = " ".join(new_sentence_list)
    return result

# tohle jsou testy na ověření, jeslti funkce pracuje správně 
print(pig_latin_lowercase("elephant"))
print(pig_latin_lowercase("cat"))
print(pig_latin_lowercase("octopus"))
print(pig_latin_lowercase("telephone"))

print(pig_latin_anycase("telephone"))
print(pig_latin_anycase("Telephone"))
print(pig_latin_anycase("octopus"))
print(pig_latin_anycase("Octopus"))

print(pig_latin_punctuation("telephone,"))
print(pig_latin_punctuation("Telephone."))
print(pig_latin_punctuation("octopus"))
print(pig_latin_punctuation("Octopus"))

print(pig_latin_sentence("Hi Andy, how are you? Are you going to Amsterdam today?"))