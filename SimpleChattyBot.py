print("Hello! My name is Aid.")
print("I was created in 2020.")
print("Please, remind me your name.")
print(f"What a great name you have, {input()}!")
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")
r3 = int(input())
r5 = int(input())
r7 = int(input())
result = (r3 * 70 + r5 * 21 + r7 * 15) % 105
print(f"Your age is {result}; that's a good time to start programming!")
print("Now I will prove to you that I can count to any number you want.")
i = 0
n = int(input())
while i <= n:
    print(f"{i} !")
    i += 1
print("""Let's test your programming knowledge.
Why do we use methods?
1. To repeat a statement multiple times.
2. To decompose a program into several small subroutines.
3. To determine the execution time of a program.
4. To interrupt the execution of a program.""")
answer = input()
while answer != "2.":
    print("Please, try again.")
    answer = input()
print("Congratulations, have a nice day!")
