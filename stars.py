n = int(input())
print("* "+"- "*(n-2)+"* ")
for row in range(2, n):
    tire = n - 2
    print("! "+"- "*tire+"!")
print("* "+"- "*(n-2)+"*")