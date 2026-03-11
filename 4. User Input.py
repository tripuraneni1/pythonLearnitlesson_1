
try :
    temp = float(input("Type a number:"))
    print("100 + {} +{}= {}".format(temp,100+temp,200+temp))
except:
    print("You did not input a valid number")
    print("Type 'quit' to exit")