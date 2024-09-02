# # F = open("input.txt", "w")
# # F.write("Hello\nWorld")
# # F.close()
# # lines = []
# # for line in open("input.txt"):
# #     lines.append(line.strip())
# # print(lines)
# # def modify(mylist):
# #     mylist[0] *= 10
# #     return(mylist)
# # L = [1, 3, 5, 7, 9]
# # M = modify(L)
# # print(M is L)
# # # def is_vowel(letter):
# # #     if letter in 'aeiouy':
# # #         print(True)
# # #     else:
# # #         print(False)
# # def is_vowel(letter):
# #     if type(letter) == int:
# #         letter = str(letter)
# #     if letter in "aeiouy":
# #         return(True)
# #     else:
# #         return(False)
# # print(is_vowel(4))
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         N = 1
#         for i in range(1, n+1):
#             N*=i
#         return(N)
# print(factorial(10))
# import string
# alphabet = string.ascii_letters
# sentence = 'Jim quickly realized that the beautiful gowns are expensive'

# count_letters = {}
# for i in alphabet:
#     count_letters[i] = 0
# print(count_letters)
# for i in sentence:
#     if i not in alphabet:
#         continue
#     else:
#         count_letters[i]+=1
# print(count_letters)
# print(alphabet)