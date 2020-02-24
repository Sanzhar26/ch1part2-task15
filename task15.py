age = int(input())
def even_odd():
    for i in range(0, age+1, 2):
        if i % 2 == 0:
            print(i)
    for i in range(1, age+1, 2):
        if i % 2 != 0:
            print(i)
even_odd()        