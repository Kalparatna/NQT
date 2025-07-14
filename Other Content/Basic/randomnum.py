import random

num = [random.randint(1,100) for i in range(5)]
print(num)

#generate random integer
num2 =  random.randint(1, 50)
print(num2)

#generate random float 
uniform = random.uniform(1, 100)   #float
print(uniform)

#choose random from list
list = [1, 2, 3, 4, 5]
choice = random.choice(list)
print(choice)

#choosing random name from list 
list1 = ["sam", "Jay", "alex"]
choice1 = random.choice(list1)
print(choice1)

#suffeling list
mylist = [1, 2, 3, 4, 5, 6]
random.shuffle(mylist)
print(mylist)

