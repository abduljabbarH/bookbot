count = 0
char_count_dic = {}
with open("./books/frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.split()
    count += len(words)
    for word in words:
        for char in word.lower():

            if char in char_count_dic:
                char_count_dic[char] +=1
            elif char.isalpha():
                char_count_dic[char] = 1
print("--- Begin report of books/frankenstein.txt ---")
print(f"{count} words found in the document\n")

for word_dict in sorted(char_count_dic.items()):
    print(f"The '{word_dict[0]}' character was found {word_dict[1]} times")

print("--- End report ---")
