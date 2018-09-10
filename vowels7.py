vowels = {'a', 'e', 'i', 'o', 'u'}
word = input("Provide a word to search for vowels: ")
found =  []
set_inter = vowels.intersection(set(word))
found = list(set_inter)
for vowel in found:
    print(vowel)
