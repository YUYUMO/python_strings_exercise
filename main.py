#Please write a program which prints out a line of hash characters, the width of which is chosen by the user.
def main():
    width = int(input("Enter the width of the line of hashes: "))
    a_line_of_hashes(width)

def a_line_of_hashes(width):
    hashes = "#" * width
    return hashes

print(a_line_of_hashes(10))

#Please write a function named hash_square(length), which takes an integer argument. The function prints out a square of hash characters, and the argument specifies the length of the side of the square.
def hash_square(length):
    for _ in range(length): 
        print("#" * length)

hash_square(3)


#Please write a function named same_chars, which takes one string and two integers as arguments. The integers refer to indexes within the string. The function should return True if the two characters at the indexes specified are the same. Otherwise, and especially if either of the indexes falls outside the scope of the string, the function returns False.
def same_chars(string, integer1, integer2):
    if len(string) < integer1 or len(string) < integer2:
        return False
    elif string[integer1] == string[integer2]:
        return True
    else:
        return False

# same characters m and m
print(same_chars("programmer", 6, 7)) # True

# different characters p and r
print(same_chars("programmer", 0, 4)) # False

# the second index is not within the string
print(same_chars("programmer", 0, 12)) # False

#Please write a function named longest(strings: list), which takes a list of strings as its argument. The function finds and returns the longest string in the list. You may assume there is always a single longest string in the list.
def longest(strings: list):
    longest_string = strings[0]
    for string in strings:
        if len(string) > len(longest_string):
            longest_string = string
    return longest_string

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))

#Please write three functions: first_word, second_word and last_word. Each function takes a string argument.

#As their names imply, the functions return either the first, the second or the last word in the sentence they receive as their string argument.

#In each case you may assume the argument string contains at least two separate words, and all words are separated by exactly one space character. There will be no spaces in the beginning or at the end of the argument strings.

def first_word(sentence: str) -> str:
    words = sentence.split()
    return words[0]

def second_word(sentence: str) -> str:
    words = sentence.split()
    return words[1]

def last_word(sentence: str) -> str:
    words = sentence.split()
    return words[-1]

sentence = "it was a dark and stormy python"

print(first_word(sentence)) # it
print(second_word(sentence)) # was
print(last_word(sentence)) # python

#Please write a function named most_common_character, which takes a string argument. The function returns the character which has the most occurrences within the string. If there are many characters with equally many occurrences, the one which appears first in the string should be returned.

def most_common_character(string: str) -> str:
    max_char_count = 0
    most_common_char = string[0]
    for char in string:
        char_count =  string.count(char)
        if char_count > max_char_count:
            max_char_count = char_count
            most_common_char = char
    return most_common_char
        
first_string = "abcdbde"
print(most_common_character(first_string))

second_string = "exemplaryelementary"
print(most_common_character(second_string))

#Please write a program which asks the user to type in a string. The program then prints out all the substrings which begin with the first character, from the shortest to the longest. Have a look at the example below.

def main():
    string = input("Please type in a string: ")
    substrings(string)
def substrings(string):
    for i in range(len(string)):
        print(string[:i + 1])

#Please write a program which asks the user to type in a string. The program then prints out all the substrings which end with the last character, from the shortest to the longest. Have a look at the example below.
def main():
    string = input("Please type in a string: ")
    substrings_from_the_end(string)
def substrings_from_the_end(string):
    for i in range(len(string)):
        print(string[-(i + 1):])

#Please write a program which asks the user to type in a string and a single character. The program then prints the first three character slice which begins with the character specified by the user. You may assume the input string is at least three characters long. The program must print out three characters, or else nothing.

#Pay special attention to when there are less than two characters left in the string after the first occurrence of the character looked for. In that case nothing should be printed out, and there should not be any indexing errors when executing the program.

def main():
    string = input("Please type in a word: ")
    character = input("Please type in a character: ")
    result = first_substring(string, character)
    return result

def first_substring(string, character):
    index = string.find(character)
    if index == -1 or (len(string) - index) < 2:
        return ""
    else:
        return string[index: index + 3]
    
#Please make an extended version of the previous program, which prints out all the substrings which are at least three characters long, and which begin with the character specified by the user. You may assume the input string is at least three characters long.
def main():
    string = input("Please type in a word: ")
    character = input("Please type in a character: ")
    all_substrings(string, character)


def all_substrings(string, character):
    #create a list to store the indices of the character in which it appears
    occurances = []
    #find the first occurrence of the character and store the index
    index = string.find(character)
    #while the character is found in the string, append the index to the list of occurances
    #and find the next occurance of the character using the next position after the current index
    while index != -1:
        occurances.append(index)
        index = string.find(character, index + 1)
    #if there are no occurances of the character or when there are less than two characters left in the string after the first occurrence of the character looked for
    if not occurances or (len(string) - occurances[0]) < 2:
        #print nothing
        print("")
    else:
        #otherwise create a list to store all the substrings that are at least three characters long
        all_substrings = []
        #for each index in the list of occurances, if there are at least three characters left in the string, append the substring to the list of all substrings
        for index in occurances:
            if len(string) - index >= 3:
                all_substrings.append(string[index:index + 3])
        #iteralte through the list of all substrings and print each substring
        for substring in all_substrings:
            print(substring)

#Please write a program which finds the second occurrence of a substring. If there is no second (or first) occurrence, the program should print out a message accordingly.

#In this exercise the occurrences cannot overlap. For example, in the string aaaa the second occurrence of the substring aa is at index 2.

def main():
    string = input("Please type in a string: ")
    substring = input("Please type in a substring: ")
    the_second_occurrence(string, substring)

def the_second_occurrence(string: str, substring: str):
#find the first occurrance index of the substring
    first_index = string.find(substring)
#find the second occurrence of the substring using the next position after the current index plus the length of the substring 
    second_index = string.find(substring, first_index + len(substring))
    if first_index == -1:
        print("The substring does not occur in the string.")
    elif second_index == -1:
        print("The substring does not occur twice in the string.")
    else:
        print(f"The second occurrence of the substring is at index {second_index}.")
    
