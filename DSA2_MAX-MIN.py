 
#Finding Maximum and minimum elements
'''
#Finding Maximum element in an Array
arr=[25,10,45,5,30]
#Find the largest number
#logic
# we need a variable to remember the bigget value found so far

#so we strat with
maximum=arr[0]
here
index 0
,1,2,3,4
value 25,10,45,5,30

#so initially
maximum=25
#now we compare each element 10>25,45>25 -yes update maximum =45
#step 4
#5>45?no ,30 no final answer is maximum =45



arr=[25,10,25,5,30]
maximum=arr[0]
for i in range(len(arr)):|#here i is the index or position
    if arr[i]>maximum:
        maximum=arr[i]#arr[i]is the value at thispodition
print(maximum)         

#Maxmumis not the final answer immediately when we find a bigger numbr.
#It is only the biggest number foundso far and trhat srored in arr(i)

#the variable maximum is not storing all values
#it only store sthe current winner


#Finding Minimum Element in an array

#it is the opposite of finding  the maximum
#Example:
arr=[25,10,45,65,30]
# we want to find the smallest value
#logic
#Assume the first element is the minimum
#compare it with evry other element
#if we find a smaller value,update the minimum


arr=[25,10,45,5,30]
minimum=arr[0]
for i in range(len(arr)):
    if arr[i]< minimum:
        minimum =arr[i]
print(minimum)
#keeps the minimum  value
#the only difference is
#finda the largest
#finds the snallest
*******************************
#Reversing an Array
#Reversing means changing the order  of elements from back to front
#Befor:
[10,20,30,40,50]
#after reversing
[50,40,30,20,10]
#The first element comest to the last postion and the last element comest to the first position

#Method  1:Using loop(DSA way)
#logic:
#We use two positions:
#start-beginning index
#end-last index
#Example:

arr=[10,20,30,40,50]
start =0
end = len(arr)-1
while start<end:
    arr[start],arr[end]=arr[end], arr[start]# it exchanges them without needing atemporary variable
    start=start+1
    end = end -1
print(arr)

Step by step undestaing
Index:0 1 2 3 4
value: 10 20 30 40 50
start=0
end =4
#first swap
arr[start]<->arr[end]
arr[0] <-> arr[4]
10 <->50
Array becomes:
    [50,,20,30,40,10]

#Now start=start+1
    end=end-1
start=1
end =3 #Now[50,40,30,20,10]
#condition  2<2 so faslse loop stops final arry 50,40,30,20,10
#start is not the value.it is  the index position
|#start -index 0-value 5
#end also indexes||(position)
#arr[start],arr[end]  values stored at those position
#this uses two-pointer logic,whichj is a very impoertant DSA pattern

arr=[5,10,15,20]
start=0
end =len(arr)-1
while start<end:
   arr[start],arr[end]=arr[end],arr[start]
   start=start+1
   end=end-1
print(arr)

********************

#Bubble sort
#one of the most famous DSA topics
#What is sortimng
#sorting means arranging elements in aspecific order
#For example:
#unsorted
[30,10,50,20]
#sorted(ascending order):
[10,20,30,50]

#How Bubble Sort works
#Bubble Sort compares two adjacent elements(neighbors)
#if the left element is bigger than the right element ,swap them

#Example:
[30,10,50,20]

#Firt Comparision
#30 and 10
since:
30>10
#swap them:
[10,30,50,20]

#second comparison
#Compare:
30 and 50
30<50
#no swap

#Third comparision
#compare: 50>20
#swap them

#The largest element(50) has "bubbled" to the last position
#thats why its called bubble sort

#reallife example
#similarly  bubblesin water te largest bubble rises to top,
#in Bubble Sort,the largest number moves to the end one complete pass through thearray

#now array will become [10,30,20,50]
# first 10and 30 no swappiing after swapping  30 and 20 python still checks  30 and 50
#then  we get as [10,20,30,50]
# The loopitself doesn't return arry ,The  loop just keeps comparing and swapping elements

#Bubble Sort is called Bubble Sort because ,after each pass, the largest unsorted element "bubbles up" to the end of the array,just like an air bubble rises to the surface of water



arr=[30,10,50,20]
n=len(arr)#How may elements are there
for i in range(n-1):#how many passes should Bubble sort make,n=4
    for j in range(n-1-i):
        if arr[j] >arr[j+1]: # arr[0]= 30 ,arr[j+1]= 0+1 =arr[1]= 10
            arr[j],arr[j+1]=arr[j+1],arr[j]n #30>10 ,swap
print(arr)            
#for i in range(n-1):
#How many passes shold Bubble Sort make
#n=4
range(4-1)
#becomes range(3)

#so
#i=0,i=1, i=2
#That means 3 passes

#for j in range(n-1-i):
#This is the comparision loop
#It compares two neighboring elements

#when i=0
#range(3)
#j=0,1,2


#Three comparision
#when i=1:
#range(2)

#so:
j=0,1
#only two comparision

when i=2
#range(1)
#so j=0
#onlyone comparision

#Why fewer comparisions
#Because after every pass,one moare largest element is already in its correct position at the end

#Line 5

if arr[j] > arr[j+1]:
    #compare two neighboring elements
    #Example:
     30 qand 10
     is:30>10
     #yes
     #so swapthem
arr[j],arr[j+1]=arr[j+1],arr[j]
#This swaps the two valuess
#Example:
Before:
     30 10 after 10,30
     
#Both i and j are used for indexs
#i = which pass i=0,first pass,i=1  second pass, i=2 -third pass
     30 vs 10-swap
     30 vs 50 -no
     50vs 20 swap
     #After whole round one pass occurs
#j- position we compare  j[0]=30,j[1]=10......

     

arr=[10,40,30,60,20]
n=len(arr)
for i in range(n-1):
   for j in  range(n-1-i):
      if arr[j] >arr[j+1]:
         arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)

#after one pass it again compares from the start note it wont compare the last largest number  becuase its is at the end and
#is largest  here it is 60
#1 st pass =4 comparison
#2- pass =3 comparision
#3 -pass 2 comparion
4 th pass = 1comparion
#whenever 60 met a smaller number it was moved to right and there is np0 biggest no in 60 hence it is at the last
#it is proved by coomparison

*******************

#Selection Sort
#It repeatedly finds the smallest element from the unsorted part and puts in the correct position

#   Example :
[40,10,30,20]
#First look fr the smallest
40,10,30,20
#10 is the smallest
#put 10 at the beginning =[10,40,30,20]

#Now ignore 10 because it's in its correct position
#look at remaining
[10,20,30,40]
#Then 30 and 40 are already in the correct order

#Bubble Sort:comapres neighboring elements and swaps them

#Selection Sort:searches  for the smallest element aand then swapsit into position 
#The key difference from bubble sort


arr=[40,10,30,20]
#step 1=start at index 0
#we assume the first element is the smallest

min_index=0
#so currently 40 assumed smallest
#But we dont trust that assumption yet we search the rest of the arry
#compare 10<40 n-yes
#so now min_index =1

#then compare 30 with 10 30<10 -no ,and then 20 with 10 no
#we have finished the searching
#so the smallest elemt is at index 1-value 10
#now sawp index 0 and 1  becomes [10,40,30,20]
#Now 10is fixed we dont touch it

#step 2
#min_index=#position of the smallest value
#now  assume 40 is smallest
#after comparison 20 is the smallest

# arr=[50,20,40,10,30]
#after the first swap
#we get
#arr=[10,20,40,50,30]
#smallest is at index 3 ,soswapping happens  at the index opf 0 and 3


arr=[50,20,40,10,30]
n=len(arr)
for i in range(n-1):
    min_index =i
    for  j in range(i+1,n):
        if arr[j]<arr[min_index]:
            min_index=j
            arr[ i],arr[min_index]=arr[min_index],arr[i]
print(arr)


#n=5
#range($)

#soi takes
i=0
i=1
i=2
i=3
#i tels us whre we are placing the next smallest element
#min_ index=i= For now i will asume the element at position i8 is the3 smallest
#temporarily assuming 50 is the smallest
#then we hve forj in range(i+2,n):

#first pass i=0
#range(0+1,5)
becomes range(1,5)
j=1,2,3,4
#wecheck the remainnig elements against our current min_index
# if arr[j]<arr[min_index]:
if j=1
#arr[1]=20
arr[min_index]=arr[0]=50
#so 20<50-True # there fore

#min_index=1

3we have found a smaller value
#then j continue to 2,3 and 4
when it reaches  to 10:
    10<20 =True
    so
     min_index =3
     #now we knoow the smallest   value is at the index 3
     arr[i],arr[min_index]= arr[min_index], arr[i]
     #means
     arr[0]<-> arr[3]

     #so it becomes
     [50,20 40 ,10,30
      

#for second pass i=1,range(2,5)
j=2,3,4
# the i tells nus whre the next smallest number should go while j searches the remaning array to find that smallest number       

arr=[50,20,40,10,30]
n=len(arr)
for i in range(n-1):
   min_index=i
   
   for j in range(i+1,n):
       if arr[j] <(
arr[min_index]):
          min_index=j
   arr[i],arr[min_index] =arr[min_index],arr[i]#even though one loop funishes the min _index still 3m
print(arr)                   


arr[i],arr[min_index] =
arr[min_index],arr[i])
# thisworksin singleline  bjut not in my version

  arr[i],arr[min_index] =(
arr[min_index],arr[i])
#if you wamnt to split twolines you must use brackets
#the (end)tells the python that  this statement contimnues   ontothe next the

#Method 3: using a tenmporary variable
 temp= arr[i]
 arr[i]=arr[main_index]
 arr[min_index=temp]
 #this is the traditioal method taught in many textbooks and  works in every version of python
 
 *****************************************
 

#INSERTION ARRAY
#TAKE ONE ELEMENT AND INSERT IT INTO THE CORRECT POSITION  AMOUNG THE ELEMENTS BEFORE IT
# takes n element and shifts larger elements rigjht ,thyen insrets the element  into the correct place
#like if first eleemnt is [11], second elemnet is 2 compare it with 11 11> then arr=[2,11]

arr=[8,5,10,3] 8 and 3 changed by indexes swappind 3-8
n=len(arr)
for i in range(1,n):
     key=arr[i]
     j=i-13 i is point towards the key and we want j to point the element immediately before the key 
     while j>==0 and arr[j]>key:#in 9nsertion sort j move sbackward
         arr[j+1]=arr[j] here  the valuemoves from index 0 to 1
         j=j-1#it means  0-1=-1   to move from 1 t0 0 we  us erevese  indxinh
        g
     arr[j+1]=key
print(arr)


#there are 4 elements s= n=4
#range(1,4) ,i=1,i=2,i=3
#why does i start at 1 instead of 0


#Because in insertion Sor,we treat the first element as alredy sorted
#so we dont want to insert 8 anywhere
#westrt with second  element 5 ,then 10,then 3
#soitellsus which element we are curenntly taking and tyring to insert unto the sorted portion onits left

#note:
#here for i in range(1,n):
#i is still a loop variable that represents an index
#it is not the  value itself

#when loop starts i=1
#so python sees
#key=arr[i],key =5

#we create key becuase 5 is the number that we currently trying to put into the correct position
#we temporarily keep5safe in
#key =5
#Thenwe can move 8 tothe right  without losing 5
#key stores the actualvalue we're currently trying to insert
i-1
arr[i]-5
key-5

#j=i-1
#curerntly i=1 ,j=i-1=0, j=0
#it means Look at the element immediately tothe left of the key
#Because insertion Sort checks the elements to the left of the current element


#while j>=0 and  arr[j]>key:
#it has two condition , bothmust be true
#j>=0 , wehave j=0, 0>=0-True
#Ehy do we check this?

#Because we are moving left through the array.once j becones-1, there is no arry position -1 that we want to check here


#condition 2
arr[j]>key
arr[j]=arr[0]=8
key =5
#sopython checks 8>5-True
#Both loops are true
#while loop runs
#it means as alomg as i haven't gone past the begining of the array and the number on the left is bigger than my key,
#keep going

arr[j+1]=arr[j]
#e currently have
arr=[8,5,10,3]
j=0
key=5

#so sub j=0
arr[0+1]=arr[0]
#which becomes  arr[1]=arr[0]
arr[0]=8 soat 0-8


#after j+1

#note  We have not put 5 back yet
# we tempoprarily have two 8s because we are shifting  8 one position to the right  to make a space for key

#arr[j+1] =arr[j] -copy the lest element one position to the right

j=j-1#this move j=1 position left = 0-1 =-1 j=-1
# because  insertion sort is checking wheather thre re more elements tothe lest that also need to bi shifted
#then whilecondion chclks again
#j>=0
#-1>=0- false

#arr[j+1]=key
#put the key value into one position immediately after j
#if j=-1 key=5 then 0=5
# j+1 because j has moved one position too far left
*****************



#Arrays common prioblems:

#find duplicate elements in an array

arr=[10,20,30,20,40,10]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j]:
            print ("Duplicate :", arr[i])

#note:
print("Duplicate:",arr[j])
#we can print j alsoinstead of i both give the same output since we are useing the if loop, we can print either one




#i goes ton each index
#then for j oin range(i+1,len(arr)):
#j checks the elemnets after i
#are these two values equal if yes- we found a duplicate
#i=5 and j =6  is performed but it does not prints anything becuase there is no value
# then  is stops because range is only six


*****************************************************


#Counting  frequency
# instead of asking which values are duplicates we'll ask:
#"How many times does each value appear
#Example:
#0- 3 times
#20=5 times etc

# This is very useful in array problems becaus eit teaches you hoew to count occurrence

arr=[10,20,10,30,20.,10]
for i in range(len(arr)):
    count=0
    for j in range (len(arr)):
        if arr[i]== arr[j]:
            count +=1
    print(arr[i],"_",count)

10 _ 3
20 _ 2
10 _ 3
30 _ 1
20.0_2
10_3
# it repeatedly prints again if numbers are repeted m
#  for i in range(len(arr)):
#so i seltecs one lement at  time-0,1,
#for j in range(len(arr)):
# inner loop for each i,j goes through the entire array
#This means the inner loop checks every element of the array against the current arr[i]
#Every time we choose a new,i we start its count from zero
#compares

#for every mtching value is fopund the count increases by 1
 
**********************************************************"

#Remove duplicates from an arry
arr=[10,20,10,30,20,10]
new__arr=[]
for i in range (len(arr)):
    if arr[i] not in new_arr:
        new_arr.append(arr[i])
print(new_arr)

#the new thing is here
#if arr[i] not in new_arr,add it
#new_arr is empty i moves through the original array:
#i=0=10
#10 is not in the new_array add it 20-qdd,10-alreday there dont add
#the key idea is only add the value if we haven't added it beforelm
#i  is the position arr[i] is the value here 



***********************

#Find the second largest element
#arr=[10,50,20,40,30]
#largest=50,#second largest is 40
#we we'll learn how to find 40 without sorting the array
#code:
arr=[10,50,20,40,30]
largest=float('-inf')
second=float('-inf')
for i in range(len(arr)):
    if arr[i]>largest:
        second=largest
        largest=arr[i]# we take lvalue fromarr[i]and store it in largest
    elif arr[i]>second and arr[i] !=largest:#if current value is different from largest ,10!=5=- true
        #bcz current values must br greater trhan current second
        #bcz we dont wnt the largest value to become second larget also  
        second =arr[i]
print("Largest:",largest)
print("Secondlagest:",second)

#When anew largest  number appears ,the old largest becomes the second largest

# intially largest =-inf,second =-inf
#thenthe loop cecks each value
value 10,50,20,40,30
largest 10,50,50,50,50,50
#second -inf ,10,20,40,40

#when a new largets is found second=largest,largest =arr[i]
# the ol largest is th second largest and new is the first largest
#-inf =a value smaller than any normal number

#inf i sthe string but the float()is afunction which converst that paerticular string toa spscial floatindg -point value
#Ex
#float("10"
#convers into  10.0

#similarly
#string "inf" into -inf
# we can't assign 0 to largest or second largest because array may contains
*************************************


#Check if an array is sorted
arr=[10,20,30,40,50]
is_sorted=True
for i in range(len(arr)-1):
    if arr[i]>arr{i+1]:
        is_sorted =False
        break #once we have wound the array isnt sorted there is no need to check array again
if is_sorted:# if you write it inside the loop you will get multiple answers
    print("Arry is sorted")
else:#now we can write it outside te loop because  value or data is store in is_sorted
    print("Array is not sorted")
#we want to make sure every number is less than or equal to number after it arr[i] ->curernt number, arr[i+1]->next number 
# we are using len(arr)-1
#because were using: arr[i+1]
#we nned next element
#we compare
#0 with 1
#1 with 2
#2 with 3
#3 with 4
# we dont need i=4 because there is nothing after index 4
*****************************************


#Linear Search
#We want to find wheather a particular value exists ina an array


arr=[10,20,30,40,50]
target=30
for i in range(len(arr)):
    if arr[i]==target:
        print("Found at index",i)
        break   
    else:
        print("Not found")
#we we dont use break it will  print for all elements in array


*******************************************


#Binary Search
#This  is faster  than linear search ,but the arry must already be sorted
arr=[10,20,30,40,50,60,70]
target=50
low=0
high =len(arr)-1
while low<= high:
    mid=(low+high)//2
    if arr[mid] ==target:
        print("Found at index",mid)
        break
    elif arr[mid]<target:
        low =mid +1
    else:
            high=mid-1
#Instead of checking every element we look at the middle and eliminate half of the arry each time
**************************************

#Left Rotation of an Array
# we rotate by one position

arr=[10,20,30,40,50]
first =arr[0]
for  i in range(len(arr)-1):
    arr[i]=arr[i+1]
arr[len(arr)-1]=first
print(arr)
#10= temporary stored in first
20= move stoposition 0
30=1
40=2
50=3
10=goes t0 last position
#basically shifting to the last

arr[len(arr)-1]=first
#we use first arr:
#Which position in the arry we are talking about
#second one how many elements are there in len array

#Right rotation of the array

arr=[10,20,30,40,50]
last=arr[len(arr)-1]
for i in range(len(arr)-1,0,-1):
    arr[i]=arr[i-1]
arr[0]=last
print(arr)
**************************************
                                                                                                                                                                                                                                                                                    

# Move all zeros to the end

arr=[0,10,0,20,30]
pos=0
for i in range(len(arr)):
    if arr[i]!=0:
        arr[pos]=arr[i]
        pos+=1
while pos < len(arr):
    arr[pos]=0
    pos +=1
print(arr)
#pos tells us whre the next no zero value should be placed
#doestnee to be sorted
#e dont need to know  the which no is missing
#wedo need toknow the expected range(1 ton)
#Exactly one number must be missing



**************************
#Find a pair with a give sum
arr=[5,4,11,15]
target=9
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] +arr[j]== target:
            print(arr[i],arr[j])
#find the pair of number whose sum is equal to give target
#if there is actual element withor without the pairs whose values is equalto target then it prints  nothing
 #i+1,makes j start agter  i , we dont compare no with itself or repeat the same pair
            
*************************************


#Merge  Two Arrays

#simpleway
arr1=[10,50,24]
arr2=[56,100,94]
merged=arr1+arr2
print(merged)

#Here , +joins the two arrays


#if you want tounder stand the logic manually
arr1=[10,20,30]
arr2=[40,50,60]
merged=[]
for i in range(len(arr1)):
    merged.append(arr1[i])
for i in range(len(arr2)):
    merged.append(arr2[i])
print(merged)

************************************

#Frequency of each element
#wewan tofind how mnay times each valueappears
arr=[10,20,10,30,20,10]
visited=[]
for i in range(len(arr)):# chhose which vlaue we are counting
    if arr[i] not in visited: # and visited makes sure we dont count/print the same value again
        count=0 #because every new value needs a fresh count
for j in range(len(arr)):# searches the entire array to count that value 
    if arr[i]==arr[j]:
        count +=1
print(arr[i],"-",count)
visited.append(arr[i])# it remenbers the value =append 
#take the current value of i and add it to the visited list

**************************************

#2D ARRY MATRIX
#The first index selects the row and next selects the coloumn
#matrix[1][2]

#Traverse a 2D arry:
matrix=[
    [10, 20,30],#-coloumn 0 1 2,#row #0
    [40,50,60],                      #1   
    [70,80,90]                       #2
    ]
for i in range(len(matrix)):
     for j in range(len(matrix[i])):
              print(matrix[i][j])# go tothye row i and columj give m,e that value
# i moves through rows
#j moves through columns

#matrix has three rows and each row has  3 values

#len(matrix) is 3 beacsue we have 3 rows
#so
#i=0,,3irepresents the row index
1,
2

#for j in range(len(matrix[i])):, matrix[i]means  curernt row
#when i =,matrix[0],=[10,20,30]

********************************************

#Find the sum ofall elements in a matrix
matrix=[
    [10,20,30],
    [40,50,60],
    [70,80,90]
    ]
total=0
for i  in range(len(matrix)):
    for j in range(len(matrix[i])):
        total+=matrix[i][j]#total=total+matrix[i][j]#take the current total and add the  current matrix elemnet to iter            
print(total)
#+= means add the new value to the existing value and store the result back in the same variable

*********************************************

#Find the largest element in a matrix\
matrix =[
     [10,20,30],
     [40,50,60],
     [70,80,90]
]
largest=matrix[0][0]
for i in range(len(matrix)):
       for j in range(len(matrix[i])):
                  if matrix[i][j]>largest:
                             largest=matrix[i][j]
print(largest)
#len matrix coutns length becaus eit contains three inner listes

***********************************************

#FInd the smallest  element  in a matrix
matrix= [
    [10,20,30],
    [40,5,60],
    [70,80,90]
    ]
smallest=matrix[0][0]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if  matrix[i][j]<smallest:
               smallest= matrix[i][j]
print(smallest)

***************************************

#Rowwise sum
#wewant to calculate the sum of each row separetely
matrix=[
    [10,20,30],
    [40,50,60],
    [70,80,90]
    ]
for i in range(len(matrix)):
    total=0
    for j in range(len(matrix[i])):
        total +=matrix[i][j]
    print("Row",i,"sum=",total)
    
#total=0 otside the for loop
#the total doesn't reset for each row
    row0-60
    row 1= 210
    r0w 2-450 # thats  a running total , not each row'sindividual sum

#total=0 inside the i loop
#this gives a new total for every row


#total=0insidethejloop
    #now you are resetting total every single time j change s
    10-total-10
    10-total-20
    30 -total=30
********************************************

#Column wise sum 
#matrix=[
         [10,20,30],
         [40,50,60],
         [70,80,90]
         ]
#we want add each columnseparately
         for j in range(len(matrix[0])):
             total=0
         for i in range(len(matrix)):
             total += matrix[i][j]
             print("Coloum",j,"sum=",total)
#Notice that  we switched the loops
             #For row wise-sum
             #i=row
             #j=columns
             #forcolumn-wise sum
             #j=columns
             #i=rows

*************************************

#main diagnolsum
matrix =[
    [10,20,30],
    [40,50,60],
    [70,80,90]

    ]
#The main  diagnol goes from top -lest to bottom right:

matrix=[
    [10,20,30],
    [40,50,60],
    [70,80,90]

    ]
total=0#adding n storing each value
#but if write this in the for loop  the total value gets replaced ecah time whine the loop runs 
for  i in range(len(matrix)):
    total+= matrix[i][i]
print(total)
#here both indexes are same so
#i=0-matrix[0][0]-10
#i=1-matrix[1][1]-50
#i=2-matrix[2][2]-90
## we dont need  second jloop because we're only intrested in the diagonal positions where rowindex =column index

*************************************


#Transpose of a Matrix
matrix=[
   [10,20,30],
   [40,50,666666660]
   ]

#The transpose changes rows into coloumns
#10 #40
#20 #50
#30 #60


matrix=[
    [10,20,30],
    [40,50,60]
    ]
transpose=[] # empty list we're  going to buildthe new matrix
for j in range(len(matrix[0])): #matrix 0 is [10,20,30]it's range is 3, j=0,1,2 ,j tells us  about columns 
    row=[]#inside every j we create a new bempty row
    # because we are going to take one whole column from the original matrix and turn it into one new row
    for i in range(len(matrix)):#there are two rows 
        row.append(matrix[i][j]) #[i][j]  because matrix is a list of lists in python so not i.j
        #take the one value at row  i, column j put it in to the new row
    transpose.append(row)
print(transpose)    

*******************************************

#Serch for an element in matrix
#wewant to fiind wheather the given target is exists or not
matrix=[
     [10,20,30],
     [40,50,60],
     [70,80,90]
     ]
target =50
found =False
for i in range(len(matrix)):
     for j in range(len(matrix[i])):
         if matrix[i][j]==target:
             found =True
             break
     if found:
          break

if found:
    print("Element found")
else:
    print("Element not found")
#Then break stop[s the loops because  we already found whar we are looking for 
#first break stops the j loop
    #second loop stops the i loop

******************************************
'''



       

 





        

















































 





















































