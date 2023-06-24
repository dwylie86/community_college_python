# David Wylie
# PA 2
# Takes three words, slices them to combines into a new word.

slice_1 = input("Enter a word that contains at least 4 letters: ")[:3]
slice_2 = input("Enter a word that contains at least 4 letters: ")[-2:]
slice_3 = input("Enter a word that contains at least 4 letters: ")[0]

print(f"The combined word is: {slice_1}{slice_2}{slice_3}")
