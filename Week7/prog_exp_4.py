a_string = "To be or not to be! Being famous is not important!"
lowercase = a_string.lower()
vowel_counts = {}
for vowel in "aeiou":
    count = lowercase.count(vowel)
    vowel_counts[vowel] = count
print(vowel_counts)

counts = vowel_counts.values()
total_vowels = sum(counts)
print(total_vowels)
