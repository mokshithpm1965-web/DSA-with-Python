
'''#Sliding Window
#Maximum Sum Subarray of Size K
#find maximum sum of 3 consecutiuve elements
#nums=[2,1,5,1,3,2]
#k=3
#three consecutive elements means three numbers that are next to each other in the array without skipping any number

nums=[2,1,5,1,3,2]
k=3
window_sum =sum(nums[:k])
max_sum=window_sum
for right in range(k, len(nums)):
    window_sum+=nums[right]
    window_sum-=nums[right-k]
    max_sum=max(max_sum,window_sum)
print(max_sum)

#first take  k=3 numbers:
#[2,1,3],their sum=8
#then the qindow slides [2,5,1]->[1,5,1]
#we remove 2 and add 1; 8-2+1=7,next [1,5,1]-[5,1,3]-7-1+3=9
#the largest sum we saw was 9 so answee is 9
#dont recalculate the entire window
#remove the element leaving the window and add the element entring it

#sum(nums[:k])- give me the elements from the beginning up to ,but not including index
#means 2,1,5- sum -add them
# window_sum+=nums[right] ,8+3=8+1=9 but arry becomes [2,1,5,1]
#since k=3 so  window_sum-=nums[right-k] ,3-k,3-3=0 ,9-0,9-2=7, now our window is [1,5,1]
#then compare both max_sum and window_sum,store it in max_sum and print max_sum

************************************************************************************


#Maximum Average Subarray
#this is still a fixed - size sliding window ,so the logic will be very similar to wh maximum sum subarray
#nums=[1,12,-5,-6,50,3]
#k=4
#Find the maximum average of any 4 consecutive elements

nums=[1,12,-5,-6,50,3]
k=4
window_sum=sum(nums[:k])
max_sum=window_sum
for right in range(k,len(nums)):
    window_sum+=nums[right]
    window_sum-=nums[right-k]
    max_sum=max(max_sum,window_sum)
print(max_sum/k)

#average =sum+numbers of elemnt 

# we call it subarry because ita continous portion if a larger array
#[1,12,-5,-6,50,3]- this is original array
#[1,12,-5,-6]-  this is sub array  ,these elements are next to each other in the original array
|#subarray must be continuous


***********************************************************************************************


#Longest Substring  without Repeating Charecters
#this one is little different becayuse window size is not  fixed

#s"abcabcbb"
#we need to find longest with no repeaated  charecters
#possible substrings "abc" ,"bca" ,"cab"

#Asubstring is a continous part of the original string .you cannot skipcharecters
s="abcabcbb"
left=0
max_length =0
seen=set()
for right in range(len(s)):
    while s[right] in seen:
         seen.remove(s[left])
         left+=1
    seen.add(s[right])
    max_length =max(max_length,right -left+1)
print(max_length)

#seen contains the charecters  currently inside our window
#first chareter  is "a" a is not in seen so  senn={"a},after right  2 we get {"a","b","c"}
#now right =3 so [3]=a  but a is already present  remove a at left[0] =a is removed now set becomes {"b","c"}
#left+=1 then left move sto index b


#max_length =max(max_length,right -left+1) -is how we calculate how many charecters are currently inside the window
# left =0, right =2,left-left+1  ,2-0+1=3 ,+1 because indexes atart at 0  s0 indexes are 0,1,2
#there are 3 charecters even though 2-0=2 so we add 2-0+1=3 

******************************************************************************************************


#Longest Repeating Charecter Replacement
#This introduces an important new sliding window idea -. frequency counting
#s="AABABBA"
#k=1

#weneed to find the longest substring that can be made entirely of the same charecter
#ne things are
#a frequency dictionary
#finding the most frequent charecter in the current window
#deciding when window is invalid
#shrinking the window when necessary
s="AABABBA"
k=1
left=0
max_length =0
max_freq=0
count={}
for right in range(len(s)):
    count[s[right]]= count.get(s[right],0)+1
    max_freq=max(max_freq,count[s[right]])
    window_length= right-left+1
    if window_length -max_freq>k:
        count[s[left]]-=1
        left +=1
    max_length =max(max_length,right -left+1)
print(max_length)

#count is the dictionary  we use it to remember how many times each charecter appears in our  current window
#during firts iteration we get count[A]=count.get('A',0)
#look for 'A' inthe dictionary.If it's there.give me its value ,if it's not there ,give me 0
#since 'A' isn't there  =0 then count['A']=1 ,count={'A':1}
#[A]- square bracket says that  acess the  dictinory using the key called A , next ietration of A values becomes 2

# max_freq=max(max_freq,count[s[right]]) - the highest number of times any single charecter apperas in the current window
#for example if ,
#count ={'A':3,'B':1}
#then max_freq =3
#because a appers 3 times

#window_length  this says how many charecters are there currently inside our window
#for an example if left =0 , right =2
#2-0+1=3
#if window_length -max_freq>k: - this asks how many charecters dow we need to change to0 make the entire  window
#the same charecter

#supppose our window is   A A B we have A:2, B:1 so window_length =3 , max_freq =2
#the mos frequent charecter i s a keep the two as A A we only need to change the remaining B TO a
#so number of replacements needed is window_length -max_freq,3-2=1

#and k=1 we are allowed to make one replacements 1>1 is False so window is valid
#if window is A A B B  we need 2 replacements  ,2>1 -shrink the window so 2 replacements are too many

#hence we move left forward before moving we delete left element  count['A']-=1 , A:2 - A:1 then left+=1
#If the conditionis false then  we execute max_length =max(max_length,right -left+1)

#suppose left=0 ,right =2 then  right -left+1 =2-0+1=3 ,socurrent windowlength is3
#if max_length =2 then max(2,3) them=3 n we are saying I have found a valid window of length 3.
#If that is bigger then privious  If it is bigger remember 3
#print current length



*************************************************************************************************************



#Minimum Size Subarray  Sum
#This one teaches another important Sliding window pattern ,shrinking the windo when a condition is satisfied

#nums=[2,3,1,2,4,3]
#target=7

#Find the smallest length of a consecutive subarray whose sum is at least 7
#for example  [4,3]-sum-7-length =2

#key idea is Expand the window with right ,and after sum==  target ,shrink it from the left

nums=[2,3,1,2,4,3]
target =7
left =0
window_sum=0
min_length =float('inf')
for right in range (len(nums)):
    window_sum+=nums[right]
    while window_sum >=target:
        min_length = min(min_length ,right -left+1)
        window_sum-=nums[left]
        left+=1
if min_length == float('inf'):
    print(0)
else:
    print(min_length)


#window_sum+=nums[right] , during firt itertaion nums[o]=2 window_sum=0 ,0+22,window_sum=2
#add the new number entering the sliding window to the current window sum after second iteration it becomes 5 
#firts window is[2,3],then [2,3,1],then[2,3,1,2]
#while loop checks for every iteration of the for loop,and checks the target  is reached or not


#after meeting the while condition , record the current length
#min_length=min(min_length ,right -left+1)  left -0 , right =3 3-0+1=4
#initially  min_length =infinity  so 4 is smaller so  4 is  smaller value untill for now
#remove the left most number ,left =0  window_sum-left[0]= 8-2 =6


#move left left+=1 ,our window is now [3,1,2] = sum6 thyen while loop again checks
#Then the for loop continuous to next right , tht's how  window expads with right and shrinks  with left

#if min_length == float('inf'):- we are checking  infinity at end because imagine if target =10
#no sub arry can reach 10 soit yes it prints0if we find the target it prints len of smallest sub array

#it doesnt mater  that sum is equalor greater to target bur length matters
#once we get target we   start shrinking the window from the left



*******************************************************************************************************************





#Permutation in string
#s1='ab'
#s2='eidbaooo'
#Does s2 contain the same cahracters as s1 ,with the same frequencies , next to each other

#A permutation means rearranging the same charecters
#for ab ,the possible permutations are "ab" and "ba"
#this is a fixed-size window because   s1 length has 2 ,our window in s2 must always contain exactly 2 charecters
#so we are combining   two things
#Frequency counting
#count how many times each charecter apperas
#Fixed -size sliding window
#window size stays len(s1)

s1="ab"
s2="eidbaooo"
count1={}
count2={}
for char in s1:
    count1[char]=count1.get(char,0)+1
    left=0
for right in range(len(s2)):
     count2[s2[right]]=count2.get(s2[right],0)+1
     if right -left+1>len(s1):
        count2[s2[left]]-=1
        if count2[s2[left]]==0:
           del count2[s2[left]]
        left+=1
     if count1==count2:
       print(True)
       break
else:
    print(False)

#lese executes only when the for loop finishes normallywithout hitting break
#it is not execute after every failed if
#after checking every element else condition runs
# for -else means : If the loop finishes  without break , run else

#right is the index and s2 is actual charecter we use f count2[s2[left]]==0:- because dictonary needs the charecter
#as key

##second if only checks the condition =0sp regardless of wheather the count becomes zero , the charecter has left
#the window

# so left must move forward every time the window is too large
#char -charecters , right -index hence use  use s2 to grt charecter




***************************************************************************************************************************


#Final all anagrams in a string
#s="cbaebabacd"
#p="abc"
#we need  to find all positions where an anagram opccurs
#the anagrams are abc,acb,bac,bca,cab,cba
# keep sliding through the entire string and collectevey matching window's starting index;

s="cbaebabacd"
p="abc"
count_p={}
count_s={}

#count charecters in p
for char in p:
    count_p[char]= count_p.get(char,0)+1
    left =0
    result=[]
for right in range(len(s)):
    count_s[s[right]]=count_s.get(s[right],0)+1
    #keep window size equal to len(p)
    if right - left+1>len(p):
            count_s[s[left]]-=1

            if count_s[s[left]]==0:
                del count_s[s[left]]
            left+=1

    if count_p == count_s:
        result.append(left)
print(result)


#we append the starting index(left) of the matching window
#weare storing  result.append(0)
#now result=[0]  we are storing 0 not cba
#cehcking is one element at a time

*************************************************************************************************************************************



#Minimum Window Substring
#s="ADOBECODEBANC"
#t="ABC"

#find the smallest substring of s that contains every charecter of t with the required frequency
s="ADOBECODEBANC"
t="ABC"
count_t={}
for char in t:
     count_t[char]= count_t.get(char,0)+1
count_window={}
left=0
have=0
need=len(count_t)
min_length =float('inf')
result=""
for right in range(len(s)):
    count_window[s[right]]=count_window.get(s[right],0)+1
    if s[right]in count_t and count_window[s[right]]==count_t[s[right]]:
        have+=1
    while have == need:
        window_length=right-left+1
        if window_length<min_length:
            min_length = window_length
            result =s[left:right+1]
        count_window[s[left]]-=1
        if s[left]in count_t and count_window[s[left]]<count_t[s[left]]:
                have-=1
        left+=1
if result:
    print(result)
else:
    print("")

#count_t -what we need
#coun_window - what out current window has
#have - how many required charecter re currently satisfied
#need - how many different charecters we need

#count_t[char]= count_t.get(char,0)+1 - to make a valid window ,I need A ance , B ance  and C once
#Count_window ={}
#this is an empty dictionary
#Because count_t tells us what we need but we also need to know

#what does our  current window contain
#for example if our current window is ADOBE - then A:1,D:1,O:1,B:1,E:1
#have=0 - How many of the required charecter types have we completely satisfied
#we want 3 elemnts A,B,C ;If we counter any If A then have =1 If B have =2 If c have =3
    
#so have is not the number of charecters in the window
#The number of different requirements ftomt that have  been completely satisfied

#need is howmany different requirements exist


#after A and B we see c,our window is  ADOBEC
#now count_window={
#A:1,D:1,0:1,B:!,E:1,C:1} have =3,need =3  so have == need  so  we know current window is valid  thwn we calculate window lenght
#left=0 ,right =5 5-0+!=6 ,if window_length<min_length:  6<infinity  so store 6 as  min_length

#result =s[left:right+1]- we want to store the actual substring not just its lengh
#s[0:5+1] = ADOBEC  to include end we do =1  give all the charecters from left to right
#count_window[s[left]]-=1 - remove one occurance  of the charecter at the left side of the current window
# if s[left]in count_t and count_window[s[left]]<count_t[s[left]]:

#right  is an index and  start from 0
#right  issimply current position at the window

#if s[right]in count_t and count_window[s[right]]==count_t[s[right]]: - right is an index in  s not in  t
#count_window[s[5]=c ==count_t[s[right]]=count_t['c']
#so  we are comparing how many c's do i have?== how naby s'sdo I neeed
#so c=- we hvae com-pleterly satisfied one required charecter type -c

#we are asking after removing theleft charecter did we lose something that we needed ,a-0  , a in count_t -true
# 0<1  ;yest sophave -=1 have =2

#then left+=1
#if result contains substring -print it
# if result is still empty -print empty string
# If we dont remove A after doiing A:0 ,If for loop acesses another A  the same A is incremented by 1
#0+1 =1


***************************************************************************************************************************************
'''



    

    

















































    







































    


























