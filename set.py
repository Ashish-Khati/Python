#it is unordered. denoted by {}. it only stroe unique value
Days={"Monday","Tuesday","Wednesday","Thrusday","Friday","Saturday","Sunday"}
print(Days)
print(type(Days))

#looping through set elements

for d in Days:
    print(d)

# other method to define set

a=set([1,2,3,3,4,5,2,4,1,3,5,5,6,6,7])
print(type(a))
print(a)

# It can contain any type of element such as integer, float, tuple etc. But mutable elements (list, dictionary, set) can't be a member of set.
s1={1,2,3,("A","B",2,4,1,3)}
# s1={[1,2,3,4,"Ashish"],1,2,3,("A","B",2,4,1,3)}  #it will give error bcuz list can't be used in set
print(type(s1))
print(s1)

# method used with set
Days.add("January");  #used to add single data in set
print(Days)
Days.update(["Hello","World"])  #used to update or add data in set
print(Days)

# deleting from set
Days.discard('Hello')   #used to delete element from set
print(Days)
Days.remove('World')  #used to remove element from set
print(Days)
Days.pop();   #used to remove last element from set
print(Days)
Days.clear()  #used to remove all element from set
print(Days)


# if user try to remove element which does not exist in the set using discard() it will not give any error but if we use remove() in this case error will be generated

# union of set (|)
a1={"A",'B',"C","D","E"}
a2={'F','G','H','I','J','A',"B"}
a3={1,2,3,4,5,6,7,8,9,"A"}
print(a1 | a2 )
print(a1.union(a2,a3))

#intersection of set (& and)
print(a1 & a2 & a3)
print(a1.intersection(a2,a3))

#insersection_update () is used to remove items from the original set  that are not present in both or more the sets
aa = {"Devansh", "bob", "castle"}
ba= {"castle", "dude", "emyway"}
ca = {"fuson", "gaurav", "castle"}

aa.intersection_update(ba, ca)
print(aa)

#difference of set (-)
Days1 = {"Monday",  "Tuesday", "Wednesday", "Thursday"}
Days2 = {"Monday", "Tuesday", "Sunday"}
print(Days1-Days2)
print(Days2-Days1)
print(Days1.difference((Days2)))

#symmantric difference of sets (^)
num1 = {1,2,3,4,5,6}
num2 = {1,2,9,8,10}
num3 = num1 ^ num2
print(num3)
print(num1.symmetric_difference((num2)))




### frozenSet
# same as set only difference is it is immutable
data=frozenset([1,2,3,4,5])
print(data)
# data.add(6) #it will give error as frozenset is imutable
