
with open("ovoce.txt", "r", encoding="utf-8") as infile, \
     open("novy.txt", "w", encoding="utf-8") as outfile:
    for line in infile:
        if line.strip("\n") != "pikachu":
            outfile.write(line)
        else:
            outfile.write("rajče")

