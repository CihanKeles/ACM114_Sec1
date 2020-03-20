# Simplest Answer:

inputString = str(input("Please type a sentence: "))

vowel_count = 0

inputString =inputString.lower()

vowel_count+=inputString.count("a")
vowel_count+=inputString.count("e")
vowel_count+=inputString.count("i")
vowel_count+=inputString.count("o")
vowel_count+=inputString.count("u")

print(vowel_count)
