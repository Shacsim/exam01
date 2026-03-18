matn = input("Matn kiriting: ")
matn.lower()

son = 0

for h in "aeiou":
    son += matn.count(h)

print(son)