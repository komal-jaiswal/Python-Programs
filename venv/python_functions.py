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

#----------------------------Calculator--------------------------------------------------------------------
num1=float(input("Enter first number"))
operator=input("Enter operator");
num2=float(input("Enter third number"));
if operator == "+":
    print(num1 + num2)
elif operator =="-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Invalid input")

#-----------------------------------Python Dictonary------------------------------------------
monthConversions={
    "Jan":"January",
    2:"February",
    3:"March",
    4:"April",
    5:"May",
    "Jun":"June",
    "Jul":"July",
    8:"August",
    9:"September",
    10:"Ocober",
    "Nov":"November",
    "Dec":"December"
}
print(monthConversions["Jun"]);
print(monthConversions.get(5));
print(monthConversions.get("Fake","default"))

#-----------------------------------while loop-----------------------------------------------
i=1
while i<=10:
    print(i);
    i+=1

#---------------------------------Factorial using while--------------------------------------
def factorial(num):
    fact=1
    while num >= 1:
        fact=fact *num;
        num-=1
    return fact
num=int(input("Enter number to calculate factorial"))
if num <=0:
    print("Enter number bigger than 0 and 1");
fact=factorial(num)
print(fact);


