import sampleModule as md
x=10#int
print(type(x))
x=10.2#float
x="komal"#string
x=1j#imaginary
x=["apple","banana","cherry"]#list
x=("apple","banana")#tuple
x=range(6)#range
x={"name":"subex","location":"bang"}#dictonary
x={"subex","acc","bosch"}#set
x=True
def testFunAdd(*a):
    print("my favorite dry fruit is"+a[1])
md.testModule("Accenture")
md.person["rating"]=10;
print(md.person["rating"]);
print(dir(md))

testFunAdd("almond","cashew","manuka","pista")
