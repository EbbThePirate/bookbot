def word_count(s):
    return len(s.split())

def char_count(s):
    s = s.lower() 
    char_dict = {}
    for char in s:
        if char.isalpha():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    total_words = word_count(file_contents)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{total_words} words found in the document")
    ## Prints word count
    
    print()
    print()
    ## For space between word count and character count

    sorted_chars = sorted(char_count(file_contents).items(), key=lambda x: x[1], reverse=True)
    for char, count in sorted_chars:
        print(f"The '{char}' character was found {count} times")
    ## Prints character counts

    print("--- End report ---")

if __name__ == "__main__": 
    main()
