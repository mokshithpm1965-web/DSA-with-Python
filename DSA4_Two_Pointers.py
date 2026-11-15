#What are two pointers
#Two pointers means we use two variables to keep track of positions(indexes) in an array/ string

#usually we call them
left=0
right =len(nums|)-1
#so left starts from  the begining
#right starts from the  end

#Then we move them toward ecah other  depending on the p[roblem



*********************************************************************************


#Palindrome Check
#cheeck wheather  a string  reads  the same from both  directions

s="madam"
left=0
right =len(s)-1
while left<right:
    if s[left] != s[right]:
        print(false)
        break
    left +=1
    right -=1
else:
    print(True)

# when left = right they are  pointinmg to the same charecter hence else will run
#the lese has same  identation as  while so else belongs to the while  so run else when while finishesnormally

************************************************************************************


#Two sum in a sorted array
#find the two numbers whose sum is 6

nums=[1,2,3,4,6]
target =6
left=0
right =len(nums)-1
while left<right:
    total=nums[left]+nums[right]
    if total== target:
        print(nums[left],nums[right])
        break
    elif total <target:
        left+=1
    else:
         right -=1
# sum is too small -move left forward  make sum bigger
#sum too big - move right backward make sum smaller
#because array is sorted  left -right - increasing
#right - left decreasing
    
************************************************************************************


#Move zeros
#nums=[0,1,0,3,12]
#Move all 0s to the end ,while keeping the order of the other numbers
#[1,3,12,0,0]
#code
nums =[0,1,0,3,12]
left =0
for right in range(len(nums)):
    if nums[right] !=0:
        nums[left],nums[right]= nums[right],nums[left]
        left+=1
print(nums)

##right -scans every element
# left- tells us where the next non -zero element should go
#in firts iteration both left and right are 0 so condition false  eight automatically moves to 1 while left stays 0
#after iterariion finishes , the for loop automatically takes the next value


*******************************************************************************************


#Container with most water

#heights =[1,8,6,2,5,4,8,3,7]
#Imagine each number is avertical wall .We need to find two walls that can hold the maximum amount of water

heights=[1,8,6,2,5,4,8,3,7]
left=0
right =len(heights)-1
max_water =0
while left <right:
    width =right -left
    height =min(heights[left],heights[right])
    water =width *height
    max_water =max(max_water,water)
    if heights[left]<heights[right]:
        left+=1
    else:
        right -=1
print(max_water)
# idea: we always move  the pointer at the shorter wall
#water can only rise as the wall becomeshorter

#  height =men(heights[left],heights[right]) -firts we have 1,7
#weuse min here because  if you try to fill water higher than 1 ater will spillover the left wall

#the shorter wall controlls the water height
#width initially the distance between the walls is 8

#water=width*height = 8*1=8- this is basically area of the container
#formula water = width * shorter wall
#or  water =(right-left)*min(heights[left],hights[right])
# left+=1 - we move left forward toget taller wals musch as we can

# right -=1- if right wallis shorteror equal move right backward
#max _water stays until  the water becomw gigher than the max_water, when left =right the loop stops



*******************************************************************************************************

#3Sum
#nums=[-1,0,1,2,-1,-4]
#Find three numbers whose sum is 0
#the answer is [-1,-1,2],[-1,0,1]
#firts importenet stepsort

nums =[-1,0,1,2,-1,-4]
nums.sort()
result=[]
for i in range(len(nums)-2):
    left =i+1
    right=len(nums)-1
    while left<right:
        total=nums[i]+nums[left]+nums[right]
        if total==0:
            result .append([nums[i],nums[left],nums[right]])
            left+=1
            right-=1
        elif total<0:
            left+=1
        else:right-=1
print(result)

#for i in range(len(nums)-2):  3sumneeds three positions
#we use i as the fixed firts number and  then left an dright find the the other two numbers


#there are 6 positions we  do -2 to get 4 ,soagter getting firts b3 positions there are no more three positions
#so len(nums) -2 makes sure there are alaays at least twopositions remaining after i

#right=len(nums)-1 - we start right at end because we want the  largest available numberon the right side .Since the array is sorted ,the last index contains the largest number
#right never moves outside the while, so for loop changes i , while loop changes, right and left

#result .append([nums[i],nums[left],nums[right]]) -square bracket is used to crete list
#square brackets create one list containg three numbers 


****************************************************************************************************************

#Remove the duplicates from the sorted array
#remove the duplicates values in place  so that each number appears only once
#nums=[1,1,2,2,3,4,4]
#use the two pointers technique
#expected output will be [1,2,3,4]

nums=[1,1,2,2,3,4,4]
left=0
for right in range(1,len(nums)):
     if nums[right] !=nums[left]:
        left+=1
        nums[left]=nums[right]
print(nums[:left+1])

#print(nums[:left+1]- This is python slicing ,means print the array starting from the index 0 up to left ,including left?
#weare using print(nums[:left+1])  todisapperar from the output 


*******************************************************************************************************************


#Valid Palinderome

#use two pointers (left and right) to determine wheather it reads  the same forward and backward ,ignorging spaces ,punctuation and capittalization

s="A man ,a plan , a canal: Panama"
left=0
right=len(s)-1
while left<right:
    if  not s[left].isalnum():
        left+=1
        continue
    if not s[right].isalnum():
        right -=1
        continue
    if  s[left]. lower() !=s[right].lower():
        print(False)
        break
    left+=1
    right-=1
else:
    print(True)

#lower(0 -converts  a letter tolower case
    #continue -skips the current iterarion and goes back to the while condition
    #left moves forward
    #right moves backward
    #panama =is a country in Cetral America

#s[left]. lower() !=s[right].lower():- it actually converts the code into lower and compares
# like "a" !="a" -False  o, if they area a,B , then "a"!="b" -True 

    

************************************************************************************************************************

#Trapping Rain water - Two Pointers

# in the given array of heights ,where each number represents the height of a vertical wall
# we have to find how much rainwater can be trapped between  those walls aftyer it rains

#example
#height =[0,1,0,2,1,0,1,3,4,1,2,1]
#anwer =6
#Because  the taller  walls  on theleft and right hold water in the lower areas between them


height=[0,1,0,2,1,0,1,3,2,1,2,1]
left=0
right=len(height)-1
left_max=0
right_max=0
water =0
while left<right:
    if height[left]<=height[right]:
        if height[left]>=left_max:
            left_max=height[left]
        else:
             water += left_max -height[left]
        left +=1
    else:
        if height[right] >= right_max:
                  right_max =height[right]
        else:
              water+=right_max-height[right]
        right -=1
print(water)

#left_max and right_max are the tallest  walls we have encountered so far
#if left side nhas shorter wall we are processing left and if right side has shorter wallwe are procesing right

#left_max = tallest wall seen fron left
#right_max= tallest walls seen from right
#water =total water collected
# so left_max and _right_max are the largest walls encountered so far

**********************************************************************************************************************************


  












































































































