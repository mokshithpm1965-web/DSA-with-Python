#INSTRODUCTION  TO DSA
#A data structure is a way of organizing data so it can be used efficiently
#Books scattered on the floor  hard to find
#Books arranged on a bookshelf easy to find
#A data structure organizes data just like a bookshelf organizes books

 #what is an Algorithm
#An algorithm is a step-by-step proceduere to solve a problem
#Example making a tea
#boil water
#add te powder
# add milk
#add sugar
#serve
#Rhose steps form an algoritm
#Real DFSA Example  
#suppos your college has 5,000 students
#you want to find MokshithPM
#Methopd 1
#Start from the first student  and check one by one
#Slow
#Method 2
#Store the students in a good data structure and use an efficient searching algorithm
#fast
#thats why DSA is so important


#Lesson one arrays
#what is an arrays
#an array is a collection  of elemnts stored in contiguous(continous) memory locations
#In python there is no built in array type used like c or java .we usually use a list to represent an array because it behaves  similarly for learning DSA
#example 
arr=[10,20,30,40,50,60]
#important things
Index-0,1,2,3,4,5
value-10,20,30,40,50,60
Index-Position of an elemt
value -actual data stored

arr=[10,20,30,40,50,60]
print(arr[2])
#arrays are important because  if you want to store the marks of 100 students
#without an array:
m1=85
m2=90 
m3=76
#this becomes difficult to manage
#withh array
marks=[85,90,76,88,95]
#everything is stored in one place .,making it easy to access and process
#operations on arrays
#accessing elements
, #traversing(visiting every element)
#insertion
#deletion
#searching
#updating

#Practice question 1
#predict the output

#Accessing elements
arr=[12,24,36,46]
print(arr[1])
print(arr[3])

#Next Topic:Traversing an Array
#Traversing means visitring every element of the array one by one
#Example
arr=[10,20,30,40,50,60]
for i in arr:
     print(i)
#Here, the for loop visits each elemnt one by one.This process is called array traversal
#Predict the output
arr=[5,10,15]
for i in arr:
    print(i*2)
    #here i represents the current element  of the array
    #I sotres the current value not the iteration count
    # if you want the iteration count(0,1,2)
    #you would use enumerate()
    #Traversing an array means visiting every elemnt exactly once to perform some operation on it

    
#Interview Question
#there are two ways to traverse an array in python
#method 1:Direct Traversal
arr=[10,20,30]
for i in arr:
        print(i)
#HOW IT WORKS
#FIRST:I=10
#SECOND:I=20
#THIRD:I=30
#PYTHON TAKES EACH ELEMT ONE BY ONE
#here i is the value not the index

#Method 2 :Idex Traversal
arr=[10,20,30]
for i in range(len(arr)): #itgives 3 becaus there  3 elements are there
    produces 0,1,2
    print(arr[i])
#loop runs like this
    #First i=0-arr{0}=10
    #second i=1-arr[1]=20
    #third i=2-arr[2]=30
    #out put is same
    #range is used to generate the  index numbers of the list
#The main difference
    #method 1
    for i in arr:
        i= value. easy to write, use    it when you need the values
    #method 2
     for i n range(len(arr)):
         i=index
         arr[i]=value
         #use it when youneed the index ,or when you want to update elemts
#why is method 2 impotant in DSA
         #suppose you want to change every element

arr=[10,20,30]
for i in range(len(arr)):
   arr[i]=arr[i]*2
print(arr)   
#we can do it because i is the index
#with the first method
   for i in arr:
       i=i*2
    
#the original array does not change,because i is only a temporary variable holding the value
print(arr)


arr=[1,4,6]
for i in range(len(arr)):
   print(i,arr[i])


#First iteration
   #i=0
   #arr[i]=arr[0]=2
   # 0 2
   #second iteration
   #i=1
   #arr[1]=4-1,4
   #Third iteration
   #i=2
   #arr[2]=6 2,6
   # Output
   #0 2
   #1 4
   #2 6
   #in this loop'i' is the  current index

a
# first iteration
i=0
#this line executes:
arr[0]=arr[0]+5
#which means arr[0]=10+5  3noe array becopmes  [15,20,30]
#notice something important:
we are not just calculation 10+5
#we are storing the new value back to the same index
# when we do this   it says take the value from the 0 box ,and put the new value back into nrhe box
#so old value(10) is replaced by the new value (15)


#Compare these two programs
#program 1:
arr=[10,20,30]
for i in arr:
   i= i+5
print(i)
   #here i is just a temporary variable
   #Changing i does not change the array

rr=[10,20,30]
for i in range(len(arr)):
   arr[i]=arr[i]+5
print(arr)
#i is the index here
#arr[i] refers to the actual elemnebt inside the array
#So replacing arr[i] changes the original array                              


arr=[10,20,30]
for i in arr:
           print(i)
           
# in first iteration i goes to 10 and second iteraion i goes to n20 so on
# i is not permanently equal to one # pyuthon keeps changing i on every ietration

arr=[10,20,30]
for i in arr:
    i=i+10
    print(i)

    #first iteration  15
    #second iteratiojn python does not remember 15 it goesr back to the array and takes next value
print(arr)   #because we are change the i  not the array 


arr=[10,20,30]
for i in arr:
    i=i+10
print(i)
# if i write this now there is no print(i) inside the loop
#first iteration
#i=10
#i=15
#second iteration
#i=20
#i=25
# third iteration
#i=30
#i=35
# the loop finishes the  value is 25 becaus the lat  iteration lest i with the values 35


#Insertion in Arrays
# adding a new element into an array
arr=[10,20,30]
#insert at the end
arr.append(40)
print(arr)

arr.append(50)
print(arr)


#Insert at a specific position
arr=[10,20,30]
arr.insert(1,15)
print(arr)

arr.insert(2,16)# arr.insert(index,value)
print(arr)
#means put 15 at index 1
#The existing elements(20 and 30) shift one position to the right

#impoertant DSA point
# insertion has different costs:
#insert bat the end
arr.append(value)
# usually faster : o(1)

# insert in the middle:
arr.imsert(index,value)
#needs shifting elements: 0(n)


***********************************


#Deletion in Arrays
#removing elements from an array

arr=[10,20 ,30,40]
del arr[2]
print(arr)# it will del;ete  30

del arr[1]
print(arr)

#it removes 20 so  array cant have thee empty space  so 40  moves left

#important DSA point:
#deleting from the end is easy
# only 40 is removed no shifting needed
#but deleting from the middle requires  shifting




# Another important deletion method
#pop()
arr=[10,20,30]
x=arr.pop(1)
print(arr)
print(x)
#remove the element at index 1 and store that removed value in x

p=arr.pop(0)
print(arr)
print(p)

# del removes the element
#does not return the deleted value
#del=delte and foprget
#pop=Remove and give it back


# one more thing if you write
arr=[10,20,30]
arr.pop()
print(arr)
#now it returns the last element

***********************


#Serching in Arrays(finding an element in an array)

#very important for interviews
#Searching means finding wheather a particular element exists in an array or not

arr=[10,20,30,40]
Search for : 30

#we want know
3 is 30 present
#if yes, where is its position

#There are two main searching algorithms:
#Linear Search(Beginner level)
#Binary Search(Faster ,but requires sorted data)


#Linear Search

#Linear search  checks each element one by one from the beginning  until it finds the target
#for example



arry: [10,20,30,40]
Find :30
#check 10- not
#check 20 -not
#Check 30 -Found

arr=[10,20,30,40]
target=30
for i in range(len(arr)):
   if arr[i]==target:
      print("Found at index",i)
      
#first i=0
#arr[0]==30? =10 is not equal to 30
#arr[1]==30? =10 is  not equal to 30
#arr[2]==30? =10 is equal to 30
#so it  prints  found at index 2

#O means time complexity


#It tells us how much an algorithm takes as the dada increases

o(1)-Constant time
#meaning:
#The algorithm takes the same amount of trime ,no matter how big the array is
#Example
arr=[10,69,56,40,90,1,]
print(afrr[2])
#Python directly goes to index 3
#it does not check
#10-69-56-40
#it  directly  gets 40

#whether the array has
#10 elements
#10000 elements
#1000000 elements

#Accessing an index is almost the same speed
#Accessing by index =0(1)

#0(n)-Linear Time
 
#The time increases  as the number of elements increases
 arr=[10,20,30,40,50]

 #find 50
 #python checks :
 10
 20
 30
 40
 50
 #it checked all 5 elements
 #if there are 1,000 elements ,it may check 1,000 elements
 #so
#Linear search=o(n) 
#Easy memory trick
#0(1)-"One direct jump"
#0(n)-"Check every item  one by one"
#interviews may ask
 #which solution is faster and why

#Important Dsa Point
      #Linear Search checks
      #Best case-Element is at the beginning-O(1)
      #worat case- Element is at the end or not present -O(n)
      #n= no of elements
      
arr=[5,15,25,35]
target=25
for i in range(len(arr)):
   if arr[i]==target:
      print(i)


#Binary Serach
#What is Binary Search
#Binary Search is a faster searching method  that works by repeatedly dividing the search area into half

#but there is one important condition:
      #THe array must be sorted
#Example:
arr=[10,20,30,40,50,60]
#this is sorted(small to large)
#Find
#Traget=40

#How lenear Search works
#Linear Serch:
10-20-30-40-
#it checks one by one

#How binary Search works
arry:P
Index:0 1 2 3 4 5
value: 10 20 30 40 50 60

Step 1:Find the middle element
#middle index:
(0+5)/2=2
#here python code we used
mid=(low+high)//2
#the symbol // is integer dision , it removes decimal part 

#middle value:
arr[2]=30

#compare
30==40 not ,40 is bigger so,we ignore the left half

#Remaining
40,50,60

#Step2 Find middle again
#Middle value- 50
low-=0
high=50
mid=(0+5)//2
mid=2
arr[2]50

#compare
50==40
#40 is smaller , so search left

#Remaining
#40

#Found

#why is binary Search fastyer
#For 1000000 elements
#binary search
#only about 20 checks
#because every time it cuts the search area into half 

arr=[10,30,20,40,60,16]
arr.sort()
print(arr)#it the array is not sorted to sort the arry we can use it




 
arr=[10,20,30,40,50,60]
target=40
low =0 #start  ing index of search area,always point to the first index in list 
high =len(arr)-1
while low<=high:
   mid=(low+high)//2

   if arr[mid]== target:
      print("Found at index",mid)

      break # if you found then  stop the loop
#What happens without break
#the while loop continuous running
#but low doesn't change, high doesn't change  ,so mid stays the same
#Python keeps checking  the same  element again and again
#this  can cause infinite loop
   elif arr[mid] <target:
      low=mid+1# mid is   2 so we laredy no 2 =30 which is not equal to 40 hence
               #we don't want to search it again so mid +1 =2+1=3
   else:
      high=mid-1# mid -1= 2-1= 1 

#initially low is 0
#high- ending index of search area  

#len(arr) gives: 6
#last index is  6-1=5

#hence high is 5

#while loop
#while low<=high:
#continue searching while there is still a valid area
#finde middle
#mid=(low+high)//2
#finds the nidlle index

#check if found
#if arr[mid]==target:
#Example:
#arr[3]==40
#if yes:
#Found

#IF target is bigger
#elif arr[mid] <target:
#low=mid+1
#Meaning Target on the right side ignore the left half
      
#if target is smaller
#else:
#high=mid-1
#target on trhe left side ,ignoere the right half

while loop starts
        if

/             \
found          no
                \
                elif/else
                  \
                update low\high
                   \
                go back to while condition
                    \
                  if again





arr =[12, 15,24,26,55,66]
target=40
low=0
high =len(arr)-1
found=False
while low<=high:
   mid=(low+high)//2
   if arr[mid]==target:
      print("Found at index",mid)
      found =True
      break
   elif arr[mid]<target:
      low =mid+1
   else:
      high=mid-1

if found ==False:
   print("Element not found")
#If we dont find the element
#then we can write this \
#the dound variable is justa a signal to remember whether  the search was successful or not
# if found is otside trhw loop

#we can also write
arr=[10,20,30,40,50,80]
target=80
low=0
high=len(arr)-1
while low<=high:
   mid=(low+hig)//2
   if arr[mid]==target:
      print("Found ata index",mid)
   elif arr[mid]<target:
      low=mid+1
   else:
      high =mid-1
else:
   print("Element is not found")


   arr=[50,10,20,40,30]
target=50
low=0
high=len(arr)-1
while low<=high:
   mid=(low+high)//2
   if arr[mid]==target:
      print("Found at index",mid)
      break
   elif arr[mid]<target:
      low=mid+1
   else:
      high=mid-1
else:
   print("Element is not found")
 
#here it wont work , binary array is not guranteed to work with every target
#correct answer in one case does not mean the algorithmis reliable fo all cases
#This is why DSA  says Binary Search requires a sorted array
#binary Search-only sortes array
 


      
#note
#Linera Search:
      O(n):
         3could check 100 times
#Binary Search O(logn)
#because  binary search does not check every element
         #Each mstep cuts the data in half :
         1,000,000
         500,000
         250,000
         125,000
#Only around 20 steps
         #sowe write O(log n)
         #because the number of steps grows according to the logarithm of n
         #The first charecter is capital O
         #it means Order of complexity

****************************

#Updating Elements in an Array
#updating means changing an existing value at  particular index
arr=[10,20,30,40]
arr[2]=100
print(arr)

arr=[10,15,90,64]
arr[0]=11
print(arr)
#updating is easy  because arrays allow direct acess using index
#this takes o(!)-constant time #beacse it does not check evey element

#why does indexing start from 0?
#this is a deeper concept
##in programming ,an index reopresents the distance from the starting point

#Imagine  an arry stored in memory
memory:
   start
   |
   [5] [10] [15] [20]
#The first element is at the starting position
   #Distance from the start:
   5-0 steps away
   10-1 step awy
   15-2 steps away
   20-3 steps away
   #so that indexes start from zero


#Searching and Updating together
arr=[10,20,30,40]
for i in range(len(arr)):
   if arr[i]==30:#condition is true means arr[2]=100 replace the  value at index 2 
            arr[i]=100
print(arr)
#actually
#i=index
#arr[i]=value at that index
#i-position
#arr[i]=data stored at thatposition

example
#i=2
#arr[i]=arr[2]=30






      





































































    
     

