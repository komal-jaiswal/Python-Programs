def hello():
    print("Hello World !")

def hello_person(name,age):
    print("Hello "+name +"your age is  "+ str(age))

hello()
hello_person("Ruby",10)

def cube(num):
    return num * num * num

result=cube(2);
print(result)

#----------------------------------------------Python If statement and AND OR  NOT operator---------------------

is_male=True
is_tall=True
if is_male and is_tall:
    print("he should be handsome")
elif is_male and not(is_tall):
    print("he is short male")
elif not (is_male) and is_tall:
    print("you are not mail but you are tall")
else:
    print("you are nither male not tall")

#--------------------------------------Largest of three numbers---------------------------------------------

def max_number(num1,num2,num3):
    if num1>=num2 and num1>num3:
        return num1
    elif num2> num1 and num2>num3:
        return num2
    else:
        return num3

result=max_number(3,5,88)
print(str(result) +"  is largest number")

