def hello():
  print("Hello from a function")


def name(fname):
  print("Hi " + fname)

def addfunction(a,b):
    return a+b

def main():
    num1=1
    num2=2
    res=addfunction(num1,num2)
    if type(res)!=int:
        print("WARNING")
    else:
        print("Test passed")
