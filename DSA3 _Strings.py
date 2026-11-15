#Strings
#Reverse  a string
text="Hello"
reversed_text =" " # we have an empty string 
for i in range(len(text)-1,-1,-1):
    reversed_text += text[i]
print(reversed_text)
#we are goingto build the reversed string inside it
#the for loop
##so i moves backward
3-1  len("Hello") is 5  but the last index is 4 , this tellspython start t 4
#-1  gountil  -1 but don;'t ninclude -1 it works as the stopping point because range() stops before the second number
#if w ewrite (4,0,-1) # w ewould get n4,3,2,1  we not get index 0
#-1 -step to move back eaxh time

*****************************************************

#Check wheather a string is a palindrome
#A palindrome reads the same forward and backward

text="madam"
reversed_text=""
for i in range(len(text)-1,-1,-1):
    reversed_text +=text[i]
if text == reversed_text:
    #we are checking the test amnd reversed_text here to   confirm the similarities 
    print("Palindrome")
else:
    print("Not a palindrome")
    

******************************************************

#Alright,next string program Count vowels in a string
text="hello world"
count=0
for i in range(len(text)):
    if text[i] in "aeiou":#checks weather the current charecter is one  of a e,i,o,u
       count+=1
       #increase4s the count whenever we find a vowel b
print("Vowels:", count)

'******************************************************


#Count consonants in astring
text ="hello  world cloudy "
count =0
for i in range(len(text)):
    if text[i]. isalpha() and text[i] not in "aeiou":
        count +=1
print("Consonants :",count)
#we ignore the space other then vowels here all are cosonants means a letter
# we use .isalpha() because the string can contain  space ,numbers or symbols and those are not letters
#alpha=alpabet



*****************************************************

text ="Hello"
for char in text:
    count=0
    for ch in text:
        if char==ch:
            count +=1
    print(char,count)



#The first loop goes through the string
# we are asking  how many times h is appears in hello
#we haven't  found any h yet
#first loopalso goes wholestring but it takins one charecter at a time
# after  taking  one variable it enters to the second loop and comes back to the first loop  after finishing one loop in second       
#count=0
#Then second is forloop
#for ch in text
#this goes through wholestring  h,e,l,l,o
#char- charecter we're counting
#ch- charecter we're currently checking
#**************************


#Remove the duplicate charecters
text="hello"
result=""
for char in text:
    if char not in result:
        result +=char
print(result)
#because append is alist method not a string method  hence it not works

****************************************************


#Finding  the first non- repeating  charecter
text ="swiss"
for char in text:
    if text.count(char)==1:
        print(char)
        break
#the loop tales one value at time
#checks how many times that charecter occurs in the whole string
#when it  finds the non repeative number  stops the loop

*******************************************************




#Intermediate Strings-1     Anagram
#Two strings are anagrams if they contain the same cahrecters withe same frequency, justin a difefrent order but bthey should
#be same after sorting
#example
#listen
#silent

text1="listen"
text2="silent"
if sorted(text1)==sorted(text2):
    print("Anagram")
else:
    print("Not anagram")
# sorted means  e,i,l,n,s,t
# all charecyters ,must be same
#How many times a particular character appears
#spaces are not allowed here


*******************************************


#Most frequent charecter
text="hello"
most_frequent =""
max_count= 0
for char in text:
    count =text.count(char)
    #char is the variablethat created  in the for loop 
    if count>max_count:
        max_count=count
        most_frequent=char
print(most_frequent)
#count on the left is our own variable
#count on the right is built in string method
#max_count  remebers the highest count found so far ,so we can compare future charecters againist it
#without this no highest count is stored we get oa sthe frequent charecter


******************************************************

#Reverse the words in a sentence
text="Python is easy"
words=text.split()
reversed_words=[]
for i in range(len(words)-1,-1,-1):
reversed_words.append(words[i])
result="".join(reversed_words)
print(result)

#split() Breaks the sentence into separate words
#in for loop we go backwards
#puts the words back together with a space between them
#The append it is still a list method here we dont use it on strings here
#because here  reversed_words=[] - a list then we convert the list bck to the string
#words=text.split is a list
#join is the method that conveerts from anoher iterable to string

**********************************************************


#count the numberof  words in a  sententce
#Example

text="Python is very easy"
words=text.split()
count=0
for wor in words:
          count +=1
print(count)

#splity does
"Python verye asy"
#into
#["Python" ," is", "very", "easy"]
************************************************************

#String Rotation

#text1="abcd"
text2="cdab"
if len(text1)==len(text2) and text2 in text1 + text1:
    print("Rotation")
else:
    print("Not a rotation")
    
# text1 + text1 = abcdancd  is cdab is in side the text1+text1 -yes
#Both strings must have same length

#rottion means you take cjharecters from one end of a string and move them to the other end  without changing the order
#ex og- abcd - move 1 charecter to end bcda  -thats a rotation if we move  2 cdab thats also a rortation we can move 3
# but should not change in order like this abcs -- acbd

*****************************************************************


#Find the lomgest word in a sentence
text = "Python programming is interesting"
words = text.split()
longest=""
for word in words:
    if len(word)>len(longest):
        longest=word
print(longest)

**************************************************************


#Remove spaces  and special charecters from a string
text =" hello, world! 123"
result=""
for  char in text:
    if char.isalnum():
        result +=char
print(result)        
#alnun - is the  charecter a letter or a number        

***************************************************************


#String Compression
#this idea is toconvert repatred consecutive charecters into charecter+ number of repetitions

text="aaabbc"
result =""
count=1
for i in range (1,len(text)):
    if text[i]== text[i-1]:#wecheck the current charecter with preivious one 
        count+=1
    else:
        result+= text[i-1]+str(count)
        count=1
result+=text[-1]+str(count)
print(result)

# we strt with 1 because we alreday know the first value
#if  first condition is false to store the count   and the alphabet we use else loop
#when theloopginishes the final charecter has not added yet  because lese only runs when there is change in charectyer
#count is abn inter result is an string so we covert 1 to "1"
#count in the else refers to starting the   new data from 1
#-1 refers to the last remained index

**********************************************

 #Longest substring without repreating characters
#we want find the longest continuous part where no character repeates
text="abcabcbb"
longest=""
for  i in range(len(text)):
    current =""
    for j in range (i, len(text)):
        if text[j] in  current:
            break
        current+=text[j]
        if len(current)>len(longest):
            longest=current
print(longest)
print(len(longest))

#the outer loop chooses whre the substring starts
# A substring means  a continuous part of the string
#for abcabcbb , abc ais a substring
#in first loop i tells where should i start looking for a substring
#current  = for trhis starting popsition , I havent't byuilt a substring yet
# second for i=0 ,j= whole string
#break is for  if the elements already there in  substring(current) the loop stops?

**********************************************************



#advanced strings-1
#Longest palindromic Substring

#we want find a longest substring  that is also a palindrome
text="babad"
longest=""
for i in range(len(text)):
    for j in range(i,len(text)):
        current=text[i:j+1]
        if current==current[::-1]:
            if len(current)>len(longest):
                longest =current
print(longest)                

# j represents the where the substring ends
#text[i:j+1]- t6his actually creates the substring
#for example i=0,j=2, text[0:3] - bab
#remeber the end number is not in cl;uded  in slicing so we use j+1
#current==current[::-1]:- 6his is whre  palindeome actually comes 
#[::-1]:- - reverses the string if current is bab then its  vice versa is bab trhen its  a palindrome
#oif we get  current longest tyhen then longest w ereplace
# that menas this tye trhe longest palindrome  found so for
#3csubstrings re nothing but continuous charectes without skiipinfg the lelement in the original string

**************************************************************

#Longest   common prefix
#wewant longest  beginning part thatr all  strings share

words=["flower", "flow", "flight"]
prefix=""
 for i in range(len(words[o])):
     char=words[0][i]

     for word in words:
         if i>=len(word) or word[i] !=char:
             
             break

     else:
         prefix+=char
print(prefix)         
#words[0]is "flower",length 6 , so i is range and checks the position
         # second loop goes through  evey words , flowwrr, flow, flight
         #we are asking does  every word have the same charecter at the position i
         #i>=len(word) - this asks  does this word even hve a charecter at position i
         #word[i] !=char-Is this word's charecter different from our reference charectern

*****************************************************************

#Anagram
#Two words are anagrams if they contain the same  letters with the same frequencies , just arranged differently
words=["eat","tea","tan","ate","nat","bat"]
groups={}
 for word in words :
     key ="".join(sorted(word))
     if key not in groups:
         groups[key]=[]
     groups[key].append(word)
print(list(groups.values())

#key ="".join(sorted(word)) - sort the letters and  then combine them into one string
#if the key is already present then there is not nedd of  adding it agin
# like "ate" - same fot tea, ate
#groups.values() itself returns a special dictionary - values object , not an ordinary list so to convert it ito
#normal list
      
******************************************************************


#Minimum Window Substring \

#we need to find the smallest continuous part of text tht contins  all the charecters  of target


text="adobecodebanc"
target="abc"
need={}
for char in target:
    need[char]=need.get(char,0)+1
left=0#start iof the window
count=0
start=0
min_length=float("inf")
for right in range(len(text)):
    char=text[right]
    if char in need:
        if need[char]>0:
            count+=1
        need[char]-=1
    while count == len(target):
        if right - left + 1<min_length:
            min_length=right-left+1
            start=left
        left_char= text[left]
        if left_char in need:
                need[left_char]+=1
                if need[left_char]>0:
                    count -=1
        left +=1
print(start)
print(min_length)
print(text[start:start+min_length])            

#Find the smallest  continuous  part of the  text that contains A,B and c
#we needall abc one time so valisdd window  should contain all three
#look   for key  'a' in need if it doesn't exist, give me zero  so currently it dosent exist so a = 0-0+1=1
#hemce need{"A"]=1
#now need={"A":1}
#then same for B and C
# if target is  "AABC" then A will be 2  
#left=0 start of the window
#count =0 says how many required charecters have we currently found
#0,a=1,b=2,c=3- counts
#start=0 # this will evantually remember  whre the best(smallest) window starts ,w edont know answe yet so it is zero
#start is the variable that storest starting element of the text ,
#we use float in min i_length in finity  it creates a floating value represents positve in finity, it is just starting value that




#min_length=float("inf") - inf -infinity
# it is basically saying I have not found any valid window yet so is infinity
#right tells us whre  the right edge of our window currently is 
#char=text[right]-look at the each charecter one by one `and store
#is current charecter one of the charecters that we need
#char ="a", need[char]=need["a"] =1 ,1>0 -true ,count =1
#suppose char="a" ,need["a"]-=1,a:1=, now a=0  we dont neeed another a right now we need b and c
#after c ba and c count reaches 3 so while becomes true
#float= guarntees that the first reaslwindow length we find will be smaller 

#It says  as long as my current  window contains everything i need  keep trying to make window samller
#char=text[right] suppose our window is adobec ,012345 -indexes
#there are 6 charecters
#so right-left+1 = 5-0+1=6,+! is needed becaus  both left and right are included


#6<min_length
#then menlength = right-left+! ,no we atre saying smallest valid window i have found so far hs length 6
#< we use trhis ebacuse we  are looking for  smallest window
##start stores where out best window starts # left gives the side window 
# left_char= text[left],left
#-char ="A"- lest_char=text[0]



#if left_char in need:-  this asks is charecter we are about to remove one of the charecters that the target requirees
#if yes true
# left_char is the charecter we're removing from the left side of our window
#left_char ="A"
#and currentlyma,0, b,0,c,0
#because we already have found the a we needed
#so  need[left_char]+=1  now  +1, a=1, now we know that current window is missing one a
#if need[left_char]>0:- 1>0, there fore counr -=1
#count -=1 ,for ex count =3 becomes count =2
#because we just removed an important a , so the windopw no longer contains everything required
#left+==1, moves the left side forward
#print(text[start:start+min_length])  -start stores where our best /smallest window begins ,min_length stores length of
#main window,now slicing becomes text[9:9+4],text[9:13]
# staring from the position where our window begins ,take exactly the number of charecters  in our  best window


***************************************************************************


#Longest Substring  without repeting charectrs
#we want the longest continuous substring that has no repeated charecters
text="abcabcbb"
left =0
max_length =0
seen=set()
for  right in range(len(text)):
     char =text[right]
     while char in seen:
         seen.remove(text[left])
         left+=1
     seen.add(char)
     max_length=max(max_length,right-left+1)
print(max_length)

#seen has no value   ,aswemove through the strind=f we put charecters to seen
#set is pecifically useful here because we only care about , have i alreday seen this cahercter ,we dont need duplicates
#()-empty set ,{} -empty dictionary,{"a"}- set containg a
#if  charecter is repetyed remove the  cahrector  at left ,lef+=1 means  left =0+1 ,next start from 1
#if it is not repeated add tothe set
##trhis finds the largest valid window length we havr seen so for ,right-left +1=3- current window length
#max(2,3)
#so max length is 3
#if anothe window is present maxt(3,2)-it gives 3
#print returns the longest susbstring without repeating chraecters
         
*****************************************************************************


#Longest Repeating charector Replacement
#we want the longest sustring that can be made into the  same charector

text="AABABBA"
k=1
count={}
left=0
max_length=0
max_frequency=0
for right in range(len(text)):
    char=text[right]
    count[char]=count.get(char,0)+1
    max_frequency=max(max_frequency ,count[char])
    while (right-left  +1)-max_frequency>k:
        count[text[left]]-=1
        left +=1
    max_length =max(max_length,right-left+1)
print(max_length)

#k tells  us we are allowed to replace at most 1 charecter
#For example aaba ,we can replace b witha  aaaa, so window can becomw all the same charecter using 1 replacement

#count={}
#weusie to count how many times each charecter appers inside our curernt window
#this creates an empty dictionary
#left means left6 side of our window
#max_length =0 we havent found any valid window yet


#max_frequency =0 - The highest number of times the same charecter appers inside our current window
#count[char]=count.get(char,0)+1- this is counting  how many times the current cjharecter has appeared
#firts A DOESNT EXUST =0+1 = A=1 , next time when A comes -1+1=2 right =2
#at third right=2,b =0 0+1 =1
#max_frequency=max(max_frequency ,count[char]) - count char means  the number of time s the current ncharecter has
#appeared  in the current window
# compare the old highest frequency with the current charecter's frequency , and keep whichever is bigger
#for example aaba,a=3, b=1 ,max_frequency n=3
#while (right-left  +1)-max_frequency>k:-total cahrecter we neeed to change to make all cahrector same
# k means- needed replacements> allowed replacements
# 2>1  -true - we need to shrink it

# count[text[left]]-=1 we are removing the charectyer at the left side of the window
#left +=1-  now we movw the left position causw we eremoved one element from the left
#max_length =max(max_length,right-left+1) compare the old longest length with the current window length, and keep whichever is bigger


******************************************************************************



#Permutation in string

#if s1='ab'
#s2='eidbaooo'
#we need to check wheathee anypermutation of s1 apperas as a substring of s2

#permutation o ab is ba  we need ttocheck this ba  in  s2


s1="ab"
s2="eidbaooo"
if len(s1)>len(s2):
    print(False)
else:
    count1={}
    count2={}
    for char in s1:
        count1[char]=count1.get(char,0)+1
        left=0
    for  right in range(len(s2)):
        char=s2[right]
        count2[char]=count2.get(char,0)+1
        if right-left +1> len(s1):
            left_char=s2[left]
            count2[left_char]-=1
            if count2[left_char]==0:
                del count2[left_char]
            left+=1
        if count1== count2:
            print(True)
            break
    else:
         print(False)
            

#If the target string islonger than the sytring we're searching in ,immediately answe is False
            
#Permutation mena srearranging the same charecter into diferent order
#  here if statement is false and we dont enter this statement
##hence in else we create  two empty dictionaries\
#count1 will count the charecters in s1
#and count 2 will count the charrecetyrs in our current window s2

# for char in s1 - go through  every charectyer of s1, count 1 will become "a" :1,"b":1
#left =indicates left side  of our sliding windown   right moves from left to end of the length of s2
# then i takes every element  count 2 becomes "e":1,"i":1
#right-left+1=current window lenght 3>2 so remove the  left element  ,move the left position one step forward

#if count1 and count2 containssame charecters with the samecounts  that menas its permutation of s1
#wegot our result so break else  do it again   
     
# supoose s1 ="ab", socount1 = "a":1,"b":1,now imagine current window  is "ea" count 2 is e:1,a:1
# when window moves we remove e count2["e"]-=1
#count2={"e":0,"a":1}
#so we dont want e in the dictionary anymore because thre are xzero e is in the current window so we do del count2["e]
# now count2={'a':1}
#this matters because python compares dictionaries including keys whose value  is zero
#{"a":1,"b":1}
#{"a":1,"b":1,"e":0}
#these are not erqual even  with no  e
# if count2[left_char]==0:,
#del count2[left_char]
#Means  this character has completely left the current window, so remove its zero- count key from, the dictionary

****************************************************************************************



#Find All Anagrams  in a String
#An anagram is a word or string made by rearranging all the  charecters of another string , using each charexcter the same
#number of times

s="cbaebabacd"
p="abc"
result=[]
if len(p)>len(s):
      print(result)
else:
    count_p={}
    count_s={}
    for char in p:
        count_p[char]=count_p.get(char,0)+1
        left=0
    for right in range(len(s)):
            char=s[right]
            count_s[char]=count_s.get(char,0)+1
            
            if right- left+1>len(p):
                left_char=s[left]
                count_s[left_char]-=1
                if count_s[left_char]==0:
                    del count_s[left_char]
                left+=1
            if count_p==count_s:
                 result.append(left)
    print (result)

#if len(p)>len(s)

#if the pattern p is longer than the main strinmg s,there is no posiible  anagram to find
# resultmeans there are no possible positions ,so return the empty result list
# result.append(left) it does not append the charecter ij just append the index it adds then v alue of left(starting index of  anagram)


*********************************************************************************************************


#Sliding Window Maximum3
#given an array of numbers and a window size kj, move the wundow from left to right and find the mac=ximum value inside
#each window

#the window alaways contains k element

#the secial paart of this program is that we'll use a deque so we can   efficiently keep track of the largest value 

nums=[1,3,-1,-3,5,3,6,7]
k=3
from collections import deque
dq=deque()
result=[]
for right in range(len(nums)):
    while dq  and nums[dq[-1]]<=nums[right]:
        dq.pop() 
        dq.append(right)
        if  dq[0]<right-k+1:# right is an index 
            dq.popleft()
        if right >=k-1:
            result.append(nums[dq[0]])
print(result)

#deque we pronounce it deck
#it comes  from double-ended queue
#what is a deque
#a normal queue is like
#Front -[A,B,C]<-Back
#A deque lets us add and remove things from both ends

#Front <->[A,B,C]<->bACK
#import Python's built -in  deque data structure from the collections module

#dq=deque()-creates  emty deque
#we'lluse it strore the indexes of useful numbers while the window moves

#the deque hwlpsus efficiently keep track of which indexes can potentially be the maximum

#queue follos FIFO ,first in first out

#imagine people waiting foraticket
#back -d , front a,b,c
#if a arrived first,a mist leave first
#add at the back e
#remove from the front -a

#soa,b,c,d
#remove a
#bcde
#you generally don't remove b,c,d from  the middle


#Deque
##you can add and  reove fromthe both windows  so its calleddouble -ended queue

#back:   front :a,b,c,d
#remove a from the front
#remove d fromthre baxck
#add something to thje front
#for examplea,b,c,d
#after removing the botj  we get b,c

#in sliding window maximum,wesometimes need to remove the largest/useless candidates from the back nd remove expired indexes fromthe front

#while dq and nums[dq[-1]]<=nums[right]:
# while dq - means  ids the deque  not empty

#if dq contains something continue checking
#if it is emptry ,stop the while

#dq[-1]- lat element  in the deque  ,we are storeing the indexes notr actual numbers
# nums[dq[-1]]-now we use the index to get actual number

#when dq is empty ,dq itself is treated as faslse in python so if its empty means false then python  does not checksfor nums[dq[-1]]
#so we execute dq.append(right)- means add the value to trhe right end of the deck now dq=[0]

# if  dq[0]<right-k+1:-it checks  wheather the index at the front of the deque has gone outside the current window
#right-k+1-calculatess the left boundary of the current window

#it checks is the oldest index in our deque now to the left of the current window ,if yes that index is no longer part of the current window
#dq.popleft() - so remove it


#<=nums[right]:- no we comparing
# number at the back of deque vs number er are currently looking at
#ex deque's number =-1,new number =5 ,we ask -1<=5? yes-True ,Threfore ,we remove -1 fromthe deque because it can never become the maximum while 5 is in the window
#the important idea is: smaller numbers behind a bigger new number are useless for finding  the maximum ,so we throw them  away


****************************************************************************************************************













































































































































































         







































        







