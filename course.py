#1
#my_string ="This is me"
#print(my_string[::-1])
#user_name=input("Enter your name:")
#print(type(user_name))
#print(f"Hi {user_name},How are you?")
#print(f"hi{user_name},your name has {len(user_name)}characters")
#print(f"hi{user_name.upper()},your name has{len(user_name)}characters")
#message="Hi Pranika"
#msg=message.replace("Hi","Hello")
#print(msg)

# my_list=["coffee","tea","sugar","milk"]
# print(my_list[1:3])

#my_list.append("cream")
#print(my_list)

#my_list.insert(1,"cream")
#print(my_list)

#my_list.remove("milk")
#print(my_list)

#forgot=my_list.pop(3)
#print(f"I forgot:{forgot}")
#print(my_list)

#my_list.sort()
#print(my_list)

#my_list.sort(reverse=True)
#print(my_list)
# my_list=["coffee",
#          "tea","sugar","milk"]
# my_list1=[1,2,3,4,5,6,7]
# print(my_list+my_list1)

#tuple
# my_tuple =(1,2,3,4,5)
# my_tuple2=(1,3,4,5)
# print(my_tuple+my_tuple2)
# count_1=my_tuple
# print(my_tuple)
# new_tuple=sorted(my_tuple,reverse=True)
# print(new_tuple)
# print(type(new_tuple))
# print(type(tuple(new_tuple)))
# print(min(new_tuple))
# print(max(new_tuple))


# my_tuple=(10,20,'a','b','True')
# print(my_tuple)
# print(my_tuple[2])
# tuple_1=(1,2,3)
# tuple_2=('x','y','z')
# concatened_tuple=(tuple_1+tuple_2)
# print(concatened_tuple)
# repeated_tuple = ((my_tuple) *3)
# print(repeated_tuple)
# print(len(concatened_tuple))
# sliced_tuple=my_tuple[2:5]
# print(sliced_tuple)

#dist
# my_dist={
#     "Name":"Hari",
#     "Age":"30",
#     "Address":{
#         "Address1":"Kathmandu",
#         "Zip":4477
#     }
# }
# print(my_dist)
#my_dist1=("college":"kmc")
# my_dist=["age"=="30"]
# print(my_dist)
# print(my_dist["Age"])
# print(my_dist["Address"] ["Address1"])
# del (my_dist["Name"])
# print(my_dist)


#write a program to show the multiplication table of first 20 prime numbers using for loop.

def is_prime(number):
    if number <2:
        return False
    for i in range(2,int(number/2)+1):
        if number%i ==0:
            return False
    return True    






count=0
number=1
prime_list=[]
while count<20:
    if is_prime(number):
        prime_list.append(number) 
