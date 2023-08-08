tuple_=('Hello', 'World',1,4,"This is tuple")
print(tuple_)

a=("Hello")  #this is treated as string
b=("Hello",)  #this is treated as tuple
print(type(a))
print(type(b))

# () brackets are not necessary to define tuple but elements must be separated by comma
c= "hello",  #it is a tuple
print(type(c))

# accessing tuple elements
d=("Python","Tuple",'List',"Java","Set",'Dictonary',[1,2,3,5,6,7])
print(d[3])
print(d[-1][3])
print(tuple);

# deleting tuple
del tuple_
try:
    print("tuple value is:", tuple_)
except Exception as e:
    print(e)


# tuple methods
t1=(1,2,2,3,1,2,2,4,4,2,3,5,2,2,0,8,7,7,7,5,3,3,2,2,8)
print(t1.count(2))   #it is used to count the occurence of a given number
print(t1.index(8))  # used to print the first index of given number
f=b+d
print(f)
