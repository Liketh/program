try:
    a=int(input("Enter a value"))
    b=int(input("Enter a value"))
    c=a/b
    print(c)
except ZeroDivisionError:
    print("Enter the value of denominator > 0")
except ValueError:
    print("enter only number")