#Q15) wap to create a dictionary index and word pair 

# s = "tomorrow is weekend and non-veg special"
# words = s.split()
# word_dict = {}
# i = 0
# while i < len(words):
#     word_dict[i] = words[i]
#     i += 1

# print(word_dict)

#Q16) wap to create a dictionary words and its length pair
#s="tomorrow is weekend and non-veg special"

# s = "tomorrow is weekend and non-veg special"
# words = s.split()
# word_lengths = {}

# for word in words:
#     word_lengths[word] = len(word)

# print(word_lengths)

#17.wap to create a dictionary characters and its corresponding upper case characters
#s="sunday"
#o/p:-->{'s': 'S', 'u': 'U', 'n': 'N', 'd': 'D', 'a': 'A', 'y': 'Y'}

# s = "sunday"
# upper_dict = {}

# for i in s:
#     upper_dict[i] = i.upper()

# print(upper_dict)

#18.wap to create a dictionary Ascii and character pair
#l=[89,51,111,77,108,120]
#o/p:-->{89: 'Y', 51: '3', 111: 'o', 77: 'M', 108: 'l', 120: 'x'} 

# l = [89, 51, 111, 77, 108, 120]
# ascii_dict = {}

# for i in l:
#     ascii_dict[i] = chr(i)

# print(ascii_dict)

#Q) WAP to print count of all types of variables. 
# a="COME23 regul@rly2 FOR c!@ss donkey!4#"
# upper=0
# lower=0
# digit=0
# white=0
# special=0


# for i in a:
#     if i.isupper():
#         upper+=1     
#     elif i.islower():
#         lower+=1  
#     elif i.isdigit():
#         digit+=1 
#     elif i.isspace():
#         white+=1
#     else:
#         special+=1
# print('count of upper char is ',upper)
# print('count of lower char is ',lower)
# print('count of numbers is ',digit)
# print('count of white space is ',white)
# print('count of special char is ',special)

#Q) WAP to factch all int vallues in list.

# list = [10, "hello", 3.14, 25, True, "world", 42, False]
# dum = []
# for i in list:
#     if type(i) is int:
#         dum.append(i)
# print(dum)

#WAP to reverse a list

# original_list = [10, 20, 30, 40, 50]

# reversed_list = original_list[::-1]

# print("Original:", original_list)
# print("Reversed:", reversed_list)
