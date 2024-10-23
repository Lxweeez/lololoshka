# # # # a = 1234 % 10
# # # # b = 1234 // 10 % 10
# # # # c = 1234 // 100 % 10
# # # # d = 1234 // 1000 % 10
# # # # print(a + b + c + d)
# # #
# # #
# # # # result = f"result {a}{b}{c}{d}"
# # # # print(type(result))
# # # # print(result)
# # #
# # #
# # # # 1) ()
# # # # 2) **
# # # # 3) * / % /
# # # # 4)+ -
# # #
# # #
# # # # s = '''программа пропонує деякі
# # # #          дані з консолі (швидше за все, з клавіатури,хоча)
# # # #                        це може бути і головне бла'''
# # # # print(s)
# # #
# # #
# # #
# # # print(str(True))
# # # print(str(0.8))
# # # print(str(5000))
# # #
# # # print(float("0.5")) працюе
# # # print(int("0.5")) не працюе
# #
# # # print(2 < 5)
# # # print(2 > 5)
# # # print(2 <= 5)
# # # print(2 >= 5)
# # # print(2 == 5)
# # # print(2 != 5)
# #
# #
# # # user = int(input('введи число' ))
# # # if user %7== 0 :
# # #       print("Number is a multiple of 7")
# # # else:
# # #       print("Number is a not multiple of 7")
# #
# #
# # # a = int(input())
# # # b = int(input())
# # #
# # # if a > b:
# # #     print(f"Max = {a}")
# # # elif b > a:
# # #     print(f"Max = {b}")
# # # else:
# # #     print(f"Max = {a, b}")
# # #
# # #     if a < b:
# # #         print(f"min = {a}")
# # #     elif b > a:
# # #         print(f"min = {b}")
# # #     else:
# # #         print(f"min = {a, b}")
# #
# #
# #
# #
# #
# #
# #
# # a = int(input("введи число"))
# # b = int(input("введи число"))
# # print("1 добуток 2 різниця 3 множення 4 віднімання")
# # action = input('выбор')
# # if action == '1':
# #     print(f'{a+b}додавання чисел')
# # elif action == '2':
# #     print(f'{a/b}ділення чисел')
# # elif action == '3':
# #     print(f'{a*b}множення чисел')
# # else:
# #     print(f'{a-b}ділення чисел')
#
#
# # a = 8
# # b = 8
# # print(a is b)
#
#
# # word = "Hello"
# #
# # if "a" in word:
# #     print('ok')
#
#
# # num = int(input('F '))
# #
# # i = 0
# # while i <= 10:
# #     print(f'{1} * {num} = {i * num}')
# #     i += 1
#
#
# # for i in range(1, 11):
# #     for j in range(1, 11):
# #         print(f'{j} * {j} = {i * j}')
#
#
# # num = int(input('Number '))
# # num1 = int(input('Number 2 '))
# #
# # while True:
# #     x = int(input('x '))
# #     if x > num and x < num1:
# #         break
# #         # for i in range(num, num1 + 1):
# #         #     if i != x:
# #         #         print(i, end=" ")
# #         #     else:
# #         #         print(f'!{i}!', end=" ")
# #
# # s =""
# # for i in range(num, num1+1):
# #     if i != x:
# #         s += str(i)
# #     else:
# #         s += "!"+ str(i) + "!"
# #         print(s)
#
# # h = int(input('h '))
# # w = int(input('w '))
# # for i in range(h):
# #     for j in range(w):
# #         if i == 0 or i == h-1 or j == 0 or j == w-1:
# #             print("*", end="")
# #         else:
# #             print(" ", end='')
# #     print()
#
# a = 1
# b = 10
#
# for i in range(a, b + 1):
#     print(i, end=" ")
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i)
#
