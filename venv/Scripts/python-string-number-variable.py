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

