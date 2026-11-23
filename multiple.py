try:
    top, bottom = eval(input("enter two numbers, separated by a comma: "))
    value = top / bottom
    print("result is", value)

except ZeroDivisionError:
    print("division by zero is error")

except SyntaxError:
    print("comma is missing enter numbers seprated by comma 1, 2")

except:
    print("input")

else:
    print("exception")

finally:
    print("excute the code")
