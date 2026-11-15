'''#Binary search
#Binary search is an algorithm used to efficiently find an  element in a sorted arry
#list must be sorted
#instead of checking every element one by one , Binary search checks the middle element and eleminates half of  the remaining search area
#after every comparision
#Basic binary search
def binary_search(numbers,target):,#numbers - we wnat to search
#target -values - we are looking for 
     left =0#first index of the current search
     right =len(numbers)-1# stiores the last index of the currentn area
     while left <= right:
         mid=(left+right)//2
         if numbers[mid]==target:
             return mid
         elif numbers[mid]<target:
             left= mid+1
         else:
             right =mid-1
     return-1
numbers=[1,3,5,7,9,11,13]
target =9
print(binary_search(numbers, target))

# while left <= right: - keep searching as long as there is still a valid search area
#if numbers[mid]==target: - gives the middle no ,//. - division that gives the whole -number result - inter division
#return-1-mans  the target was not found

****************************************************

#Search Insert position
#given a sorted list and a target value , find  the index where the target is located .if the target does not exist , find the index
# where n it should be inserted to keepthe list sorted

def search_insert(numbers ,target):
    left =0
    right =len(numbers)-1
    while left <= right:
       
        if numbers [mid]== target:
            return mid
        elif numbers[mid]<target:
            left =mid+1
        else:
            right=mid-1
    return left
numbers=[1,2,5,6]
target =4
print(search_insert(numbers,target)

#return left -we dint  find the  target so return the position where the target should be  inserted
#during the search  left keeps moving forward  whenever the middle value is smaller  than the target
#eventually when the loops finishes , left breaches the correct insertion position
# mid=(left+right)//2=1 so 4 is >3 so  left =mid+1 = left =2 now after it 4 is lesser than 5 so right =mid-1=1
#hence left>right loop stops , return left  we get insertion position 

********************************************************************************


#First and Last Poition of an Elemnt,/ Binary Search with Duplicates
#in a sorted list with duplicate values we may want to find
# First position  - the earlist index where the target appears
#Last position The latest index where the target appers


def search_range(numbers , target):
    left=0
    right=len(numbers)-1
    first=-1
    last=-1
    while left <=right:
        mid=(left+right)//2
        if numbers[mid]==target:
            first=mid
            right=mid-1
        elif numbers[mid]<target:
            left=mid+1
        else:
            right =mid-1
    left=0
    right=len(numbers)-1
    while left <=right:
        mid=(left+right)//2
        if numbers[mid]== target:
            last=mid
            left=mid+1 
           
            
        elif numbers[mid]<target:
            left =mid+1
        else:
            right =mid-1
    return(first , last)
    
numbers=[1,2,2,2,3,4]
target =2
print(search_range(numbers, target))

# first=-1- creates the variable to store the first positiuon of the target,we jhave -1 initially beacuse w e havent found the target
# last=-1- same as  right
#  while left <=right: - keep searching the loop untill you have valid area
#first=mid we found the target  so we temporarily record as the first index 
#right=mid-1, this line is important for finding the first occurance, after finding  the target at mid we move right before the moid  and search the rearler part
#because w ewant to kno wis there another targetr befor e the mid


#elif numbers[mid]<target:, if middle is smaller then the target
#left=mid+1 -so we move left after the mid

#else, the middle nva;ue is largetr than the target  so we search before the mid right = mid-1
#now lest =0  , we are settimng it to zero, because we  are starting a new binary search
#this time we are looking for last occurance
# right=len(numbers)-1 = reset the right
#while left <=right:- checkig the valid condition
# mid=(left+right)//2-find mid

# last =mid = storing  its position last
#left=mid+1= this is the key dfifference from first and last
#for the last occurance ,after finding the target we  search after mid
#return[first,last]-returns foirts and last element indexes
#while loop runs until the condition  is true
#we only change left  in elif and statement

*******************************************************************************************




#Find Minimum in Rotated Sorted Array
#A rotated  sorted array is a sorted array that has been shoiftes around
#normalsorted array =[1,2,3,4,5,6,7,8,9,]
#Rotated [4,5,6,7,1,2,3] our goal is find trhe minimum

def find_min(numbers):
    left=0
    right=len(numbers)-1
    while left<right:
        mid=(left+right)//2
        if numbers[mid] > numbers[right]:
            left=mid+1
        else:
            right =mid
    return numbers[left]
numbers=[4,5,6,7,1,2,3]
print(find_min(numbers))
#here we are noot search9ng by directr method , we are using  the sorted / rotated structure to determine which
#half  contains the minimum
#while left<right:= we are not using left == right   beacuse  we have  when we did that w enarrowed the search down to one element
#that element must be minimum



#if numbers[mid] > numbers[right]: , compare middle value with the rightmost value
#it tells if   minimum is less in rigth side tham minimum must be at right side

#else  this happens  numbers[mid] <= numbers[right]
#the middle value is smaller than or equal to the rightmost value
#so right =mid not right =mid-1 ,because  mid might be minimum so we must keep it 
#return numbers[left]  eventualyy left == right at that point only  one possible  position remains that positon contains the minimum
 
         
********************************************************************************************************



#Binary Search in Rotated Sorted Array
#Here ,we have a sorted array that has been rotated , and we need to find a target  vaalue inside it
#the challengw is bthat array is not completely sorted anymore so normal Binary search does not directly work
#the key idea is atleas one half of the current search area will always  be sorted
#we identify  that sorted half and decide whether the target can be inside it or not

def search(numbers,target):
    left=0
    right=len(numbers)-1

    while left <=right:
        mid =(left+right)//2
        if numbers[mid]== target:
            return mid
        if numbers[left]<= numbers[mid]:
            if numbers[left]<= target<numbers[mid]:
                right =mid-1
            else:
                left =mid+1
        else:
            if numbers[mid]<target <= numbers[right]: 

            
                left=mid+1
            else:
                right = mid-1
    return-1
numbers=[4,5,6,7,0,1,2]
target =0
print(search(numbers,target))


#if numbers[left]<= numbers[mid]: #we are checking wheather the left half is sorted or not
#fpor rxample [4,5,6,7,0,1,2]# left =4 ,mid =7 s= 4<=7 -true ,the left half 4,5,6,7 is sorted
#if numbers[left]<= target<numbers[mid]: so after  checking sorting we ask is the target inside this sorted left half
#left value =4,target =6,  mid value =7  check 4<=6<7 , Threfor 6 must be somewhere between left and right
#right =mid-1 , since target is in the left halkf we discard the right  hal f


#els e,this mea means traget is not in side the sorted left half so search  in other half
#left= mid +1, move left past mid  - search in   right  half
#else- if numbers[left]<= numbers[mid]: ,means left half isn't sorted,there fore right half must be sorted
#if numbers[mid]<target <= number
#weask is the target inside the right half ,ex mid =0 target =4,righ=5
#then 0<4<=5- so target in right half
#so mov the left+1- right side
#else:
#if target isn't in the right half , so we need to serch the other side mov eright before mid   v   


******************************************************************************************************************


#Binary serach on an Answer
#Binary serach on answer  is different  form of normal binary search
#In normalbinar serach w eserach a  value inside an array
#Here we  search  for the correct anwer within a range of possible anwers


#For ex  imagine wht;s the minimum speed   needed  to finish a task  within a certain time
#instead of seeachin an array  w esearch  possible speeds  1,2,3,4,5,67,8,....
#for every possible ans we ask  , can this answer  satisfy the require ment
#ther answer usually have a pattern like **** ////,*=False,/=True once we find /  ,we have ans

#Suppose we nmeed  the smllest num,ber  from 1  to 10 that is atleast 7
def find_answer():
      left =1
      right =10
      while left <right :
           mid=(left+ right)//2
           if mid >= 7:
                right =mid
           else:
                left =mid+1
      return left
print(find_answer())
#normal binary search - is the target is the array
# binary search  on answer - is this possible answer good enough
#we crete the function  def find_answer  , there is no array here , the function's job is to find the smallest no feom
#to 710 that is at least 7
#left =1 = smallest possible answer
#right =10 - the largets possible answer

#while< right : - we keep searching  while there is more than one possible anwer  left == right
# if only one possible answer remains we stop
#the we calculate middle value  initialy  left=1 , right =10 , mid = 5
#if mid >=7 , we are asking if 5>=7 = False,
# if right = mid then mid >=7  we re true it would mean  , this answer is good enough ,nut may be there's and even smaller good answer
# ex if mid =8. then right =8,we keep mid because it might be the smallest valid answer

#else  we do left = mid+1 now possible answer 6,7,8,9,10
#eventually left =7 ,right =7
#the loop stops
#only one possible answe remains 7 so return left ,binary search finds the first valid answer efficiently

************************************************************************************************************************
'

#Koko Eating Bananas
#This is bthe firt  practical problem under Binary Serach  on Answer
#Defination
#Koko has severalpiles of bananas  and has h hours to eat them
#she cooses an eating speed k(bananas per hour)

#the question is what is the minimum eating speed  k  that allows koko to finish all the bananas  within h  hours
#ex piles =[3,6,7,11],h=8
#we need to find  the minimum k ,the possible speeds are 1,2,3,4....11
# we need   binary search because :
#small speeds - may not finish
#large speed - can finish

def min_eating_speed(piles,h):
    left =1
    right = max(piles)
    while left<right:
        mid=(left+right)//2
        hours=0
        for  bananas in piles:

            hours += (bananas + mid -1)// mid#mid = Koko'seating speed  we use this to  fond whole hopurs reuired   by the Koko to finish one pile

        if hours <=h:
            right =mid
        else: 
            left= mid+1#means current speed of mid is too slow  so we don't wanr to check mid or anytrhing smaller  soif one speed is smaller than anything less than that speed will bi smaller
    return left
piles=[3,6,7,11]
h=8
print(min_eating_speed(piles,h))

#koko is simply a fictional charecter in the problem .She's a monlkey  who wants to eat  all the bananas within a give  number of hours
#pile means a collection or heap  of something kept together
#heap- means a larger amount of  something  collected  or placed together in one place
#so pile = heap , ther are synonyms
#piles- no of bananas in each piles
#h-maximum number of hours available


#piles=[3,6,7,11];means koko must fifnish all 27 bananas  within 8 hours
#h=8

#left=1, the minimumpossible eating speed is 1 banana  per hour
# if we use 0koko wouldn't eat anything

#right=max(piles)-the maximum usefulspeed is the largets pile  here largers is 11

#why don't we need a speed grater thamn 11 ,because at 11 bananas/hour ,Koko  can finish  the largets pile of 11 bananas  in one hour
#Going faster cannot reduce a pile  below one hour

#so our possible speeds are 1,2,3,4,5,6,7,8,9,10,11
#while left <right : keep searching while thre is more than one possible speed
#when left== right we have found the minimum possible  valid speed
#we calculate mid now we get mid =6  we are asking can Koko finish all the bananas if she eats 6 banans per hour

#hours=0 create a variable to copunt hoow many hours koko needs at speed mid
# for bananas in piles - go through each pile one by one  , our piles are 3,6,7,11, so banans will become 3-6-7-11
#hours  +=(bananas+mid-1)//mid; how many whole ours Koko needs for the current pile
#pile 3-(3+6-1)/6=1,pile 6-1, pile 7-2,pile 11- 2 total hours =6=1+1+2+2

#so at spped 6 koko needs6 hours
#we ask if hours<=h  we ask can koko finidh within the available 8hours  sp=6<=8 -true ,speed 6 is valid
#right =mid, at speed 6 it works , we dont immediately choose 6
#we want the minimum speed
#may be 4 or 5 alsoworks  so right becomes 6

#we now search 1 2 3 4 5 6 ,else  this happens  hours >h meaning Koko is too slow and cannot ginish within the available toime
#ex if dpeed3 requires 10 hours 10>8 so left=mid+1 If ,mid is too slow we know mid and everything  smaller than it cannot work
#so return left  eventually  the serach narrows  left =4, right =4  ,4<4  the loop stops becaus  False

#finalanswe Koko'sminimum speed  4
**********************************************************************************************************************


#Binary Search - Topic 8:
#Capacity to Shift Packages Within D Days
#You have  Package with different weights , and you need  to ship all the packages within a given numbersn of days
#The package must be shipped in the given order
#you need to find  The minimum ship capacity that allows  all packages to be delivered within D days

#ex : weights =[1,2,3,4,5,6,7,8,9,10]
#days=5
#we are searching for the minimum capacity

#possible capacities have a pattern
#too small - cnanot finish in 5 days
#large enough - can finish in 5 days
#code

def ship_capacity(weights,days):
    left =max(weights)
    right=sum(weights)
    while left <right:
        mid =(left+right)//2
        
        current_weight =0
        required_days=1

        for weight in weights:
            if current_weight +weight >mid:
            
                required_days +=1
                current_weight=0
            current_weight+=weight

#suppose   mid =32,current_weight =30,weight=5
#if  current_weight+weight>mid:,we check 30+5>32 now required_days +=1 =2,and count_weight =0
            #thye second day starts with  0 kg  but weight is still 5 n  

        if required_days <=days:
            right =mid
        else:
            left=mid+1
    return left
weights=[1,2,3,4,5,6,7,8,9,10]
days=5
print(ship_capacity(weights,days))

#weights - weights of allpackages  ,days - maximum noof days availble
# left=max(weights)- find heaviest package =10
# start at 10 because the ship must be able to carryu the haviest package at least by itself
#a acapacity of 9 coud not carry the package  weighing 10
#right=sum(weights)- Adds the weight of evey package

#1+2+3+4+5+6+7+8+9+10=55,right=55 because if the shiphas the capacity 55,it can theoretically carry everything in one day
#so answer  must be somewhere between 10(minimum possible)  and 55(maximum)
#while left<right;keep searching while more than one possible capacity remains  when left == right we have found the minimum
#then we calculate mid  initially 10+55//2=32 so we are asking can we ship all packages  with 5 days if the
#ships capacity is 32,

#current weight =0,initially  and required_days =1 we start with day 1 ,required _days =1
#for weight in weights  ,  we go through every package in order 1-2-3-4-5-10
#weight represents the current package
# if current_weight +weight >mid: this asks  if i put this package on the current day's ship ,will i exeed thecapcity
#suppose ;mid =32;current_weight=28,weight =5 then 28+5=33 ;but capacity is only 32 so 33>32 - true
#We can't put that package on the current day

#required_days+=1,Since current day's shipisfull,we need another day
#required_days +=1, if it was 1 it become s2
#current_weight =0 , the  new day starts with an empty ship,then we can put the current package into this new day
#current_weight+=weight ,add the current packages's weight to the current day's total

#For example:
#current_weight=0
#weight =5,then current_weight+=weight becomes_current_weight =5
#the loop continues package by package

#if required_days <=days:
#after checking all packages ,w eknow  that how  many days are required ,suppose required_days=4,days=5 then 4<=5
# which is true we can finish within the allowed days
#right =mid ,we keep the mid because it is valid and might be minimum
#lese this means rrequired_days>days, the capacity is too small

#ex required_days=6
#days=5
#we need 6 days , but only have 5 , so capacity does not work ,so left = mid +1
#si8nce mid is too smaller than it cann ot work
#so we move  left=mid+1,for example  mid=20,left =21now we search only capacities 21  and above  , return left  eventually left == right  so minimum capcity that
# that works  so return left retiurn it

#capacity means the maximum weight the ship can carry in one day it must be in order so 15
#so smallest means the smallest capcity in which all the given values  can be delivered within 5 days
#if left is lesse than 9 it cant hpld one individual package
#so there is no way  it can shipmal;l packages
#if the ship cant hold the heaviest individual package,it definetely cannot complete shipping task

****************************************************************************************************************************************


#Find Mximum in a Rotated arry
#defination  , a sorted array like [1,2,3,4,5,6,7]
#can be rotated [4,5,6,7,1,2,3]
#Our job  will be to find the maximum element using binary search, instead of simply scanning every elementz
#code
def find_max(nums):
    left=0
    right=len(nums)-1
    while left<right:
        mid=(left+right)//2
        if nums[mid]>nums[right]:
            left=mid+1
        else:
            right=mid
    return nums[left-1] if left  > 0 else  nums[-1]
#we dont use :  in the on eleine version  , because tis is Python's condtitional expression (also called a ternary expresion)
#if:
#else:- here we write : because this is a blacok of code
#in above  if is the condition  and else is the poart of it both are same way but it is written in different manner
nums=[4,5,6,7,1,2,3]
print(find_max(nums))

#this one is slightly differnt from finding the minimum,  we are going tounderstand why left =mid+1 and right =mid work
#for  finding the maximum ,rather than memorizing them

#left=0 -we start fromthe first index
#initially left =0 and right =6
#while left<right , keep searching  while there is more than one possible position  ,when left== right the loops stops
#we calculate mid 

#if nums[mid]>nums[right] - compare the middle value with the rightmost value ,If nums[mid]=7 an dnums[right]=3
#then 7>3 -True  #this tells us something impoertant,[4,5,6,7][1,2,3]
#The maximum is around the middle left side  not in the right sorted possition
#left =mid+1,since mid=3,we get left =3+1,left =4  sp now left =4 ,right =6
# that mean swe are searching this portion  index 4,5,6,number  12 3

#But here'stheomportant point: this code is  finding the minimum/ rotation point , not directlyfinding the maximum
#we are looking where the  rotated array starts it starts at 1,2,3
#so left =mid+1  moving  us toward the minimu n,then eventually left becomes 4 which is the index 1

#after the loop
#return nums[left-1] if left>0 else nums[-1]
#since left =4 we use nums[left-1]=mums [3]=7 , we are using  the minimum's position toonbtain maximum
#else nums[-1], remember : our binary search finds the minimum element's index , for wxample   we use nums[left-1]

#if left >=
#nums[4,5,6,7,1,2,3], left =4  ,now check left >0 , 4>0 -TRUE, so we execute  return nums[left-1]=7
# If left >0 is False  now  take an arry that has not been rotated
#nums=[1,2,3,4,5]
#the minimu is alreday at the first position, so  after the binary search  left =0 , left>0 0>0 -False
#therefore we go to else: return nums[-1] , [-1] means last elemnt  so answer is 5


#else: right =mid , we are trying to find the minimu elemebnt first
# suppose nums[mid]<= nums[right]  ,- else starement executes  If nums=[6,7,1,2,3,4,5],left=0,right=6,mid=3
#then nums[mid]=2,nums[right]=5 so 2<=5 -True , Now what does that tell us , The section from mid to right is sorted
#mid =2 ,3,2 rigt=5 , the minimu could actually be nums[mid, so we cannoth throgh the mid  , so right =mid
#we are searching for left side , includibng mid  if right =mid  left =0., right =3

#so we continue searchig [6,7,1,2]
#so we discard everything after mid
#right = mid =- serach the lef side ,keep mid
#left =mid+1 , search the right side  remove mid

***********************************************************************************************************************************


#Advanced Binary Search Peoblems:
#1Median of Two Sorted Arrays
#we  we have two arrays A=[1,3] B=[2,4] we have to find the  median  we copbune them [1,2,3,4] , middle values are 2
#and 3 its adavanced because  we are using binary serach  to find the correct  partition(division point) between the two arrays

def find_median(nums1,nums2):
    #always binary search on the smaller array
    if len(nums1)> len(nums2):
        nums1, nums2=nums2,nums1
    m=len(nums1)
    n=len(nums2)

    left=0 
    right =m
    while left <=right:
        cut1=(left+ right)//2 #midddle elemnt
        cut2=(m+n+1)//2-cut1 # we use to decide where to cut the second arry  so that the total no of elemnts on the left side of both arrys is half

        left1=float('-inf') if  cut1==0 else nums1[cut1-1]
        #it means,inf means negative infinity - a value smaller than evry vale so when cut1==0  is true then partition is bfore the first elemnt b
        #ther is nothing on left side so we can't write nums1[cut1-1] bcz that would be nums[1-] = last elemnts so  we use -inf
        #if not zero then  so the lement immediately go to the  left of the cut
        #nuyms1[cut-1]
        #if cut1==0:
        #left1= float('-inf')
        #else:
        #left1=nums[cut1-1]
            
        right1= float('inf') if cut1==m else nums1[cut1]
        #right mena sthe elemnt  immediately to the right of he cut
        # its +inf we use  it sometimes when no elemnts on the right side ,so if there is no right boundry w etreat  is as
        #infinity ,if cut1==m so then ot means cut is afetr the  last elemnt
        #else  take the elemnt  immediately to the right  of the cut
        

        left2=float('-inf') if  cut2==0 else nums2[cut2-1]
        right2= float('inf') if cut2==n else nums2[cut2]

        if left1<=right2 and left2<=right1:
            if(m+n)%2==0:
                return(max(left1,left2)+ min(right1,right2))/2
            #we are adding two middle elemnts 
            else:
                return max(left1, left2)
            #we see the miidle value [1,2,3]so  [1,2],[3] right of second array is +inf so [1,2,3] ,median =2
            # [1,3],[2,4,5]  left2=4,right1=3 4<=3 false so algorithm says we have taken too many elemnts from num2 into the left  side ,so we need to move  cut 1  to the right
            
        elif left1> right2:
            right = cut1-1
           #it  means cut1 is too far to the right  , so we move the cut  to the left
            #elif means  if left1>right2so move to the left
                
        else:
            left=cut1+1
            #it says serach on right
nums1=[1,3]
nums2=[2,4]
print(find_median(nums1,nums2))

#if len(nums1)>len(num2):- is nums1 larger  than nums2  for example  nums1=[1,3,5,7]-len -4 amd nums[2,4]- len 2
#4>2  so we dont want nums1 to be larger array , so sap the arrays
#because binary searh will operate on nums 1 ,if nums1 has fever elemts ,there are fewer possible partition
#positions to search , next get the lengths m=len(nums) and n is same  so  for the given code we get m=2,n=2
#Star with binary serach  left =0,right=m ,if m=2  then left =0,right=2

#why right=m not m-1 , Because  we are not seraching for an element  ,we are searching for  a partition position
#For[1,3] possible cuts are 0|1|-11|3|-2 - so there are 3 possible cuts 0,1 and 2 that's why right =3 , so right=m

#while<= right: - keep searching while there is at lest one possible  partition position remaining

#Find the first partition cut1=(left+right)//2  this is the middle partition position in nums 1 , initially left=0
#right=2 so we  do cut1=(0+2)//2 =1
#so we divide nums1 =[1<-|3] ->cut at 1

#Find the second partition
#cut2=(m+n+1)//2 -cut1
#we are  making sure the left side of both arrays together  contains half of the lement
#for m=2,2, n=2 cut1=1
#cut2=(2+2+1)//2-1=5//2-1=2-1=1
#so nums1=[1|2],nums2=[2|4] - the lkeft side contains 1,2 and the right side contains 3,4
#now we need four boundary values
#these  four variables tell us what's immediately around our two partitions
#left1=float('inf) if cut1==0 lese nums1[left-1]
#means  whivh is the number immediately to the left of curl1 , num1=[1|3],cut1=1 ,left1=num1[0]=1

#right1=float('inf) if cut1==m else nums1[cut1]
#means  which is immediately  tob the right of cut1 here:
#right1=nums[1]=3,so nums1=[1][3]  s=left1=1 right1=3
#and same for left2=2, nd right2=4
#now we check whether the partions are correct
#Main condition

#  if left1<=right2 and left2<=right1: 1<=4 -True, 2<=3 -true
#the combined arranfement effectively [1,2|3,4]
#check whether total length is even if (m+n)%2==0:
#herem+n=4 aand 4%2=0- so the total numbers elemnts is even , for an even numbers of elemnets , the median is the average of the two middle values

#Find the two  middle  values , return(max(left1,left2)+ min(right1,right2))/2,left1=1,left2=2
#largest max(1,2)=2 ,right side right1=3,right=4  smallest 3 ,therefore  median (2+3)/2 =2.5

#what is total numbers is odd , return max(left1,left2), Because with a odd number of elements , there is one middle elemnt
#what is our partition is wrong tjhere are 2 possibilites
#left1>right, right = cut-1 means  we put too many elements  fromnums 1 on the left side  so we move partion in nums 1 to the left
#cut 1 becomes smaller

# otherwise  else: left =cut1+1 -this means we need to put more elements from nums1 on the left side sow e move the partion tothe righte
#cut 1 becomes larger,our current partion  cut1  is  too far to th left , so we  move the partion tothe left 



****************************************************************************************************************************************************************


#K-th elemnt of two sorted arrays
#given two arrays A=[1,3,5],, b=[2,4,6] ,If we combine them [1,2,3,4,5,6]
#1st elemr =1 ,2 nd =2 ......
#so if k=4 our ans is  4
# The importan part is that we dont actually merger the arrays we use binary search  to find  the correct position ,
#similar to the median problem

def kth_element(nums1,nums2,k):
    #Always binary search on the smaller array
    if len(nums1)>len(nums2):
              nums1,nums2 = nums2 , nums1

    m=len(nums1)
    n=len(nums2)

    left=max(0,k-n)# minimum we can take from nums 1
    #to find the minimum  we m,ust take from nums1 ,ask: "How many elemnts can   nus2 give me , nums 2  can give most n 
    right=min(k,m)# maximum we can take from nums 1

    while left<= right:
        cut1=(left+ right)//2#how many elemts we take fron nums 1
        cut2=k-cut1# how many ymbers w etke from nums2




        left1=float('-inf') if  cut1==0 else  nums1[cut1-1]
        right1= float('inf') if cut1==m  else  nums1[cut1]
        left2= float('-inf') if  cut2==0  else  nums2[cut2-1]
        right2= float('inf')  if  cut2==n else  nums2[cut2]

        if left1<=right2  and  left2<=right1:# it checks did we put the elements   into the left and right sides correctly
#if yes partions are correct 
            return max(left1,left2)
        elif left1>right2:
            right=cut1-1
        else:
            left=cut1+1
nums1=[1,3,5]
nums2=[2,4,6]
print(kth_element(nums1,nums2,4))

#NUMS-1 FIRST SORTED ARRAY ,NUMS2- SECOND SORTED ARRAY  K- POSITION WE WANT
#make nusm1 - smaller arrays  we  wan perform binary search on the smaaller array becasue  it gives  us fewer possible partition  position s to search
#swap,  m=3, n=3-lengths
# left=max(0,k-n)-we are deciding the smallest possible number of elementsthat can be taken fromnums 1
#left is the minimum number  of elemnts we are allowed  to take from nums1,we are trying to put exactly k elemts on the left side

#so m=3, n=3 hence  k=4 , we need 4 elemnts -on the left side  suppose we  reied to take 0 elemnts from nums2  , then
#we would have to take  all 4 elemts but nums 1 -0 elemnts nus2 -4 elemts  s0 that is impossible
#maximum we can take is 3 if we need k=4 elemts total k-n =4-3=1 ,so we must take at least 1 elemt from nnums1 ,thats why left=max(0,k-n)\
#so thats why  left=max(0,1)=1, so our seach starts fromleft =1
#why max(0,...) -bcz left can never be negative because if k=2 then we get -1nso we use max
#left=max(0,k-n) means: the smallest possibl;e number of elements we can take from nums1 is either 0 , or k-n if  nums2 doesm't have enough

#elemnts to proovide all k elemnts ,if nums has  elemnts enoufgh to k them we get 0 at max
#we dont take  left=0  if we do then eventually cut 1 necomes = bur we have k=4 and  cut2=k-cut1 but cut 2 not has 4 elemts so our condition will become false


#right is the maximum elemnt  e are allowed take for nums1  suppose m=3 ,we need exactly 4 elemnts on left
#we cannot take more thank k =4 elemnts from nyms1 , because we only need 4 elemnts total but we also can't take mpre trhan 3 bcz m=3
#so min(k,m)= min(4,3)=3  now our possible  cut1 values are 1,2,3
# we have left =1 , right =3 so cut 1=2  so nums1=[1,3|5] cut1=2  means take 2 elements from nums1 into the elft partion

#cut2=k-cut1 , we want exactly k elemnts on the left side  here k=4 and  ct1=2- elemnts from nums1, so how many do we need from  nums2
#obviously 2 so 4-2=2  so  cut2=2 so nums1=2 partion ,nums2 - 2 partion so hence total 4 elemnt s = k
#return max(left1,left2) - we are finding the kth snmallest elemnts on the left side  so nums1=[1,3|5],nums2=[2,4|6]
#left side contains 1,3,2,4 the largest  value on the left is: max(3,4)=4 and 4 is the 4 the smallest elemt  so we return 4
# elif left1> right2 this means cut 1 is topo far to the rigjht  ex left1=8 , right2=5 so  8>5

# we have to put 8 on the left even though  5 belongs  befor it
#therefore w e need  to take fewer elemnts from nums1   so we cut1 to the left
#right = cut1-1 ,here right is the binary s- search boundary not rigjht 1 or right2

#else left=cut+1 - left2>right1 , that means  we have takemn  too few elemnts from num1,cut is too far left 
#so we need to move cut1 to the rioght
#therfrore  left= cut+1
# return max(left1,left2)- suppose nums1=[1,3,5,7,9]
#cut is at =2 so evrything before the cut on the left is 1,3,5 so we know nums 1 is sortedhence 1<3<5
#so left1=nums1[cut1-1]= cut1=3 left1=nums[3-1],nums1[2]=5



*****************************************************************************************************************************************************************************




#Aggressive  Cows
#This is a classic Binary Search on Answer problem. The  main  idea is different from the median problem , but it connects directly
# to Koko eating  Bananas  and Capcity to Ship Packages
#problem  you are fiven stall positions  -[1,2,4,8,9], and you have k=3 cows
#you need to place the 3  cows  in different stalls so that the minimum distance between any two cows is as larger as possible
#for example cow1 -1, cow 2-4,cow 3-8 ,distances 1-4=3, 4-8=4 ,so minimum  distance  is  3

#But perhaps another placement gives a minimum distance of 4   , soour goal is to maximize the minimum distance   between
#the cows , this is why  this is called as  Binary Serch  on the Answe , we are binary - searching the possible distance
def aggressive_cows( stalls,k):
     stalls.sort()
     left=1
     right=stalls[-1]-stalls[0]
     answer=0

     while left<=right:
         mid=(left+right)//2
         cows=1
         last_position=stalls[0]

         for position in stalls[1:]:
             if  position-last_position>=mid:
                  cows+=1
                  last_position=position
         if   cows >=k:
             answer=mid
             left=mid+1
         else:
             right=mid-1
     return answer
stalls=[1,2,4,8,9]
k=3
print(aggressive_cows(stalls,k))
         


#stalls   - positions of the stalls,#k= number of cows we need to place    ,so we have 5 talls and need to place 3 cows
#stalls.sort()- we sort the stallpositions from smallest to largets,[1,2,4,8,9]- we need them sorted bcz we will calculate
#distances from left to right
#here left=1, left represents the smallest possible distance we are going to test
#left=1 because  two cows cannot occupy the same stall ,so minimum meaningful distance  between 2 different stalls is at least 1
#when stall positions are integrs

#right=stalls[-1]- stalls [0] -  largets possible distance between two cows right =9-1=8 ,therefore our ans must be somewhere
#between 1<= answer <=8     - this is the range where we do perform binary serach
#answer=0- we  create a variable to remember the best valid distance we have found so far    ,initialy 0 later we fill it with  best valid distance
#we continue  searvhoing a slong as  there is at least one possible distance remaining
#then w echoose middle as the possible distance

#if mid =4 the we are asking Can we place  all 3 cows whiule keeping at leat 4 distance between consecutive cows
#so we will test cows =1 - because we lreday have one  cow placed ,so dont start at 0 because  the first cow doesn't need to maintan a distance from another cow - we simply place it at the firts stall
#so at this point left=1, right=8, mid =4 , cows=1, last_posoition = stalls[0] -we put the first cow t the first stall
#our stalls are [1,2,4,8,9] so stalls[0]=1, last_poition=1,this variable remembers where the most recently placed cow is

#for position in stalls[1:]:, we check the remaing stalls  it menas [2,4,8,9] ,we dont check 1 again  becaue w have  already placed the first cow there   so loop checks  2.4.8.9
# #if position - last_position >=mid  ,this checks wh ther the current stall is far enough away from the last cow  , we found mid=4 , last_position =1
#  first position =2  , distance 2-1=1 so 1>=4 no  so we cannot place a cow at 2 next position 4 n so 4-1=3
#3>=4, no ,position =8 ,8-1=7  is 7>=4 -yes , so we can place another cow at 8

#so cows+=1 ,Becayuse  6 is far enough from the previous cow, we place another co  now cows =2
#last_position = mposition  we just placed a cow  at the current position ,  in our ex we placed the second  cow at:position =8
#so now  last_position =8  , bcz when we check the next stall 9 we ned to calculate its distance  from the  most recently placaed cow which is now at 8
# if cows >=k : w echeck wheather we have success fully  placed at least the required number of cows here  cows=2,k=3

#so 2>=3 - False , thersore  this condition doesn't execute  yet  , it eventually cows =3  so true
#so that means our current  mid distance is possiple , hence  answer = mid  we save current distance as our best valid   so if mid =4 cows=3
# we are saying  a minimu distance of  4 is possible  ,let's  remenber  ir
#left=mid+1  , this is the binary  serach on asnwer part so if mid is valid , we wnt to try a larger distance
#if mid  is valid , we want to try a larger distance  so left =4+1 =5 , bcz 4works so we should try a larger number
# the else is the opposite situaton   means we cound not place the enough cows  in to the shops

# so 2>=3 - false  so rigjht =mid-1 nso distance 4 does not work  , so the mena  if  we cannot  place 3  cows with  a minimum
#distance of 4 , we definitely cannot place  them with ajn  even larger distance like 5,6 7,or 8
#because  a larger required distance makes the problem harder , not easier    so we serach the smaller side like 1,2,3


*****************************************************************************************************************



#Allocate Books ;This is another classic Binary Search on the Answer problem  , very similar ti capacity to ship packages
#problems  Given with books with pages [12,34,67,90], 2 students , allocate books  contiguously  so that the maximum number opf pages assignes
#to any one student is as  small as possible
#for an example  student1 -12+34+67=113
#student 2-90
#maximum =112 ,we want find the minimum possible maximum

def allocate_books(pages,students):
    if students>len(pages):
        return-1
    left =max(pages)
    right=sum(pages)
    answer=right

    while left <=right:
        mid=(left+right)//2

        student_count=1
        current_pages=0

        for page in pages:
            if current_pages+ page>mid:
                student_count +=1
                current_pages=page
            else:
                current_pages+=page
        if student_count <= students:
            answer =mid
            right=mid-1
        else:
            left=mid+1
    return answer
pages=[12,34,67,90]
students=2
print(allocate_books(pages,students))

#pages= no of pages in each book\
#students - no of students  who need books
#if students >len(pages):  we check it because each student should get  one book  if condition is true it writes  no valid
#left=max(pages)-left represents  the smallest possible maximum number of pages that one student could receive

#why it cant be smaller than the largest book ,our books are [12,34,67,90]
#the largest book ha 90 pages , A student must receive that 90 page book ,therefore the maximum ppages  asigned to a student can never be less than 90
#so  left = max(pages) =90 , our answer is somewhere betweein  90<= answeer<=....
#right= sum(pages)-right represents the k largest possible maximum pages one student could receive

#so 12+34+67+90=203,right =203 , why is 203 the maximum ,Because  in the worst possible allocation ,one student could receive all the books
#so our answ eis between  90 and 203 ,answer=  right , we initially store 203 as our answer
#it is  just a starting value , later when  we find  a amallr valid calue we will replace it ,it is  just a starting value ,later , when we find a  smaller
#valid  valid , we weill replace it

#while left <= right
#while left <= right ,this starts our binary serach  currently ;left =90 , right=203
#s0 we continue  searching
# mid= (right+left)//2  , we calculate the middle possible maximum  initially  mid =146

#so we are asking can we allocate all the books to 2  students suvcjh that no strudent gets more than 146 pages
#student_count=1,we start with 1 strudent  assing books to the first student
#current_pages=0, this keeps   track of how many pages the current student has receive so far

# then we go throgh every books , we MUST PROCESS  BOOKS IN OREDR , BECAUSE THE BOOKS MUST BE ALLOCATED  CONTIGUOUSLY
#if current_pages+ page>mid:,this asks If I give this book to the current student, will their  total pages  exceed our
#allowed maximum  0+12 =12 so its 12>146 ,so we can give the 12 - page book  to the same student
# 12+34 - w ecn n give the  book to  same stuent again


#so  mid is leesser  nthan  current_page than  same student can't take take the book  so   w edo student_count+=1  =2
#so current_page = page , new student gets  this page  so current_ pafe =30- an example
#else:  this means ad d the page to  the student  number 1
#if studentr_count <= students:
#did we allocate  all the books  using the allowed numbers ofd  students or fewer, ex , students=2,suppose ,student_count =2 then -true  so mid is valid
#then answer is  mid =146
#but we   are tring   to find the smalles t valid maximum , so we dont stop here , #right=mid-1 ,can we  even better witha smaller maximum  , sow e search smaller values
#so we serach 90...................145
#therefore right =146 -1 124
#this is the  opposite of Aggressive Cows:
#Allocate Books : valid - go left/ smaller
#Agrresive Cows valid -  go right/smaller

#Because here we want the minimum valid ,mximum
# else : left = mid+1
#this happens  when student_count > strudents  so if studebnt_count=3,students=2, we cannot allocate the books  with mid as the ,maximum, so mid is too small

#we need to allow each students  to tke  more pages ,s o we search toward larger values  
            

********************************************************************************************************************************



#Split Array Largest Sum
#tHIS IS VERY SIMILAR TO aLLOCATE bOOKS , SO IT WILL REINFORCE WHAT YOU JUST LEARNED
#problems , nums[7.2.5.10.8] k=2, split the array into 2 contiguous subarrays so that the largets subarray sun is as small as possible
#ex: [7,2,5]|[10,8] sum =14 , sum =18 ,the largest sum is 18

def split_array(nums,k):
    left= max( nums)
    right=sum(nums)
    answer =right
    while left <= right :
        mid=(left+right)//2
        subarrays=1
        current_sum=0
        for num in  nums:
             if current_sum + num > mid:
                 subarrays+=1
                 current_sum=num
             else:
                 current_sum += num
        if subarrays <=k:
            answer = mid
            right = mid-1
        else:
            left = mid +1
    return  answer
nums=[7,2,5,10,8]
k=2
print(split_array(nums,k))

#nums- the array we need to spslit
#k- the number of  subarrays we must create
#left is the smallest possible  value of  the largest subarray sum  it shou;ld be 10 becayuse  the number 10 itself must belong to some sub array
#so atleast  o0ne subarray will have a sum of 10 or more

#right =sum(nums)  0- this is the largest possible  varlue for the largest sub array sum  so answer must be somewhere bt  10<= and <= 32
#answer = right  - this is just our starting vlue later , when we find  a smaller valid anser we will replace we give right- answer  because its valid
# next we chevk the condition, we find the middle  possible number ,#we are asking  can we sploit the array into k sub arrays if the maximum allowed sum is 21
#subarrays=1 - we are staring iths sub array one, cuttent_sum =0 ,this stores the sum of thye current  subarray
#now  we process far loop
# if current_sum+ num> mid  ,means if  we add this number to the currentsubarray, will its sum become greater than mid
#iIf yes  subarrays+=1
#current_sum =num , the new subarray starts with the  current number, else we add  the number into same  currens subarray
#if subarrays<= After processing all the numbers , we check how mnay sub arrays  we needed  is subarrays=2  <=2 - True  answer=mid. right =mid-1, because we wantthje smallest possible valid answer

#else: if subarrays>=k  so mid nis too small ,we   allow a larger maximums  sum
#return answer , Sfter thye while loop finishes , we have found the smallest maximum  sum that works
#answer =18
#return answer

*******************************************************************************************************************************************************************************************************************

'''










                
                
    
    



 


















   



























































            
