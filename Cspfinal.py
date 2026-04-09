import itertools

word1 = input("Enter first word: ").upper()
word2 = input("Enter second word: ").upper()
result = input("Enter result word: ").upper()

letters = list(set(word1 + word2 + result))

if len(letters) > 10:
    print("Too many unique letters (max 10 allowed).")
    exit()

digits = range(10)

for perm in itertools.permutations(digits, len(letters)):
    letter_map = dict(zip(letters, perm))

    if (letter_map[word1[0]] == 0 or 
        letter_map[word2[0]] == 0 or 
        letter_map[result[0]] == 0):
        continue

    num1 = int("".join(str(letter_map[ch]) for ch in word1))
    num2 = int("".join(str(letter_map[ch]) for ch in word2))
    num3 = int("".join(str(letter_map[ch]) for ch in result))

    if num1 + num2 == num3:
        print("\nSolution Found!")
        
        for letter in sorted(letter_map):
            print(f"{letter} = {letter_map[letter]}")
        
        print(f"\n{word1} = {num1}")
        print(f"{word2} = {num2}")
        print(f"{result} = {num3}")
        break
else:
    print("No solution found.")