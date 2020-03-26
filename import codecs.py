import codecs

f = codecs.open("1.txt", "w", "utf-8")
f.write("written word")





f = codecs.open("1.txt", "r", "utf-8")
x = f.read()
print (x) # print in the sublime



f = codecs.open("1.txt", "a", "utf-8")
f.write("\nRuby")


f = codecs.open("1.txt", "r", "utf-8")
x = f.read()
print (x)

f.close()