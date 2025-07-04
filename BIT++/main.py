n = int(input())
answers = [input() for _ in range(n)]
x=0
for i in answers:
    if "++" in i:
        x=x+1
    if "--" in i:
        x=x-1
print(x)