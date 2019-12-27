from math import *
#three basic types of data in python
character_name="forest gump";
character_age=35.00; #number
isMale=True; #boolean
print("hello all I watched the movie actor "+character_name);
print("Actor age is "+ str(character_age));

#updated the same variable with the same name

character_name="tom cruiz";
character_age="13";
print("Mission Impossible actor is "+ character_name);


print("subex\nLimited"); #insert new line
print("new\"york"); #to put quataion mark

#python built in functions

print(character_name.upper());
print(character_name.isupper());
#one line
print(character_name.lower().islower());
print(len(character_name));

#---------------------------------------------more string functions-----------------------------------
location="Bangalore Karnataka";
print(location[5]);
print(location.index("Karn"));
print(location.replace("Karnataka","India"));
#--------------------------------------------numbers in python------------------------------------------
num=-10.78;
print(num);
print(num % 3)
print(abs(num));
print(pow(3,5));
print(max(3,5));
print(round(3.4));
print(round(4.7));
print(ceil(3.4))
print(sqrt(36));

#-------------------------how to take input from user in python--------------------------------------------
name=input("Enter your Name: ");
age=input("Enter your age : ");
print("Hello  "+ name +" your age is "+ age);

num1=input("Enter first number ");
num2=input("Enter second number");
#bydefault python treat user entered number as string so convert number before showing desired result
result=float(num1)+ float(num2);
print(result);

#------------------------------mad libs program------------------------------------------------------
color=input("Enter a color");
plural_noun=input("enter a plural noun :");
celebrity=input("Enter celebrity name :");
print("Roses are " +color);
print(plural_noun +" are blue");
print("I love "+celebrity );

#--------------------------------------Python List------------------------------
#in list index starts from 0 and we can use negative values to access elements from end
languages=["python","c#","java","c++","ruby","panda"];
print(languages);
print(languages[2]);
print(languages[-1]);
#access the portion of list
#the first num from where we want to split the list and last num till where we want list excluding last no
print(languages[2:4]);
print(languages[0:1]);
print(languages[1:])
languages[-1]="abab";
#------------------------------Python List Functions-----------------------
friends=["john","merry","frannk","tina","jacob","forest"];
locations=["madrid","london","sydney","Florence","Paris","Rome","Paris"];
print(friends);
friends.extend(locations); #add second list to first
print(friends);
friends.append("Komal"); #add item end of the list
print(friends);
friends.insert(1,"Kelly"); #add to the specified position
print(friends);
friends.remove("forest") #remove specfied element
print(friends);
friends.pop(); # removes last element
print(friends);
print(friends.index("Florence")); #give the index if element is present
print(friends.count("Paris")); # count the occurance of specified element
friends.sort();
print(friends);
lucky_num=[34,2,4,99,8,6,21,11];
lucky_num.sort();
print(lucky_num);
lucky_num.reverse();
print(lucky_num);
friends2=friends.copy();
print(friends2);
friends.clear(); # clear the entire list
print(friends);