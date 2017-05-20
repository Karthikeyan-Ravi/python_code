def add_lists(a,b):
    z = []
    n = len(a)
    for i in range(0,n):
        sum = a[i] + b[i]
        z.append(sum)


    return(z)


if __name__=="__main__":
    x = input("enter the list1: ")
    y = input("enter the list2: ")
    result = add_lists(x,y)
    print result