user = input("String-->")
k = list(user)
my_set = list(set(k))
for i in my_set:
    print(i,k.count(i))
