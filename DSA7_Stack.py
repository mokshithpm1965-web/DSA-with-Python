'''#Stack
#Valid Parentheses
#Min stack
#Evaluate Reverse Polish  Notation
#Daily Temperatures
#Car Fleet
#Largest Rectange Histogram


#Valid Parentheses
#Ex "()[]{}"-True
#([)]-False
#A stack is data structure  that follows LIFO -Last in , Firts out
#Think like plate a,b,c,  the plate which was placed last is  c s o we have to remove the plate c firts


## in valid paraentheses we need to determine wheather nthe brackets are properly matched or not
#()[]{} - these are valid
#([]),{[]},() - these can be nested
#([)],(], ([]  - thes are invalid
#when we see an opening bracket , w eput it into the stack  c-push,[-push,{-push
#whenn we see a closing bracket ,we check the  most  recently opened bracket
s="([])"
stack=[]
for char in s:
    if  char == "(" or  char == "[" or char == "{":
         stack.append(char)
    else:
        if not stack:
            print(False)
            break
        top=stack.pop()
    if  char == ")"  and top != "(":
        print(False)
        break
    if char == "]"  and  top != "[":
        print(False)
        break
    if char == "}" and top != "{":
        print(False)
        break
else:
    print(len(stack)==0)
    
        
                   
    
#stack.append(char)-put something on top of the stack
#stack.pop()-remove the  most recently added item

#stack[] 0=i an empty list  thatw e use as a stack
#this is a box we we put opening brackets temporarily

#for char in s:- Go through the string s,one charecter at a time and temporarily call the current charecter char
#char is just variable ,right is avarible that we use to strore an index  we can use any of them

# if char =='(' or char =='[' or char == '{' - we check open braket If  yes  stack.append(char)
#take the curent charecter and put it at the end/top of stack


#else  it mus be closing bracket ),],}
#so we neeed ro find its matching opening bracket

#we use  if not stack:- If stack is emty  stack[] ,in python not[] is true  - if the stack is empty
#an emptylist is considerd false in python , If stack - means  a non-empty list is considered true
#python knows stack is empty or not  if not stack: and if len(stack) ==0;
#print(False)-  False means brackts are not valid


#top/end-the alst charecter
#stack=['(','[','{'] -top= stack.pop() top='{' the stack becomes ['(','[']


#  top=stack.pop()- stack.pop() -removes the last element
#if break -stop for loop -do not execute remsaining loop code
#AFTER POP REMOVES ONE LEMENT STOLRE IT IN   TOP THEN CHECK THE C ONDITIONS A
#top=- stores that removed element  inside the variable top  like top ='{' ,stack=['(','[']

#there is no instruction aying now select a closing bracket
#the string itself determines what char gets
# it goes to else immediately when the currebt char is a closing bracket .it does not wait until all closing brackets are finished
#if statement gets wrong then to avoid double printing  we can write else statement under the for loop

#we have two differnt situations
#opening bracket   we simply put it into the stack
#closing bracket
#we need to check weather there is an opening bracket in the stack
#remove the top opening bracket
#check wheather it matches  the current closing bracket

#if -opening brackets the confdition is false goes to else  and the possibilities are closing brackets
#break -for loop

#print(len(stack)==0)- it checks  wheather len(stack) is equal to zero  and then prints the reult of that check
# after matching all the brackets we have removed everinthing from the stack os now stack ength =0 which is  0==0

#so   prints True

#example  2 : if un matched opening  bracket
#supoose s="([" we put both opening brackets into the stack
#len(stack)=2 2==0 -False


***********************************************************************************************

#Min stack  is a stack that supports the normal stack operations
#push(x)-add x
#pop() - remove the top element
#top()-see the top element

class Minstack:
    def __init__(self):
        self.stack=[]
        self.min_stack =[]
    def push(self ,x):
        self.stack.append(x)
        if not self.min_stack:
              self.min_stack.append(x)
        else:
            self.min_stack.append(min(x,self.min_stack[-1]))
    def pop(self):
        self.stack.pop()
        self.min_stack.pop()
    def top(self):
         return self.stack[-1]
       
    def getMin(self):
        return self.min_stack[-1]


#we creating a class named MinStack  - it is a blueprint for our Min stack object
#__init__- cnstructor  it runs automatically whenever we create an object  when puthon runs it we get s= MinStack()
#self refers to the current object here self refers to s
#self.stack=[]- an empty list ,we use to store actual numbers
#self.min_stack =[]- empty list  minimum values
#def push(self ,x)- creating another method ,  it tales  current minstack object  and x - value we want to push
    

# suppose we do  s.push(5) self.stack.append(x)- add 5  to the stack belonging to object s  after it stack =[5]
# if not self.min_stack: - if min_stack is empty then condition is true
#then self.min_stack.append(x)  add 5 t0 the min_stack
##then we do push x=3 , now min_stack is not empty  so condition false hence


# self.min_stack.append(min(x,self.min_stack[-1])) , self.min_stack[-1] gives =5  wehave x=3  so  min(3,5) =3
#then append  min_stack=[5,3]

#pop() menas remove the top/last element
#we remove from both stacks because both stacks correspond to the same push operations

#top()
# return self.stack[-1],self.stack[-1],s.top() =7,it doesn't remove 7
#pop()-removes the top
#top()- just look at the top

# min stack allows us o perform  push, pop,top and getMin  operations in 0(1), time , we maintain an additional stack to keep track of the current minimum , so we d ont have  to
# scan all the elements  whenever we need trhe minimum
# consider if stack has  1 million elemnts  python should check  all  one million words so that  it can get min in simple min  operation


******************************************************************************************************************

#Reverse Polish Notation
#normally we write  2+3
# this is called infix notation becas ethe operator (+) is berween the numbers
#in reverse polish notation the operator comes after the numbers   2 3+
# both mean 2+3
#another example 2 3+ 4* ,(2+3)* so answe is 20
# its a mathe maticaloperator named after polis logician Jan    Lukasiewicz
#reverse means the operator is moved after its operands

#why dowe stack , we read one item from left to  right ,consider 2 3 +4 *
#2 is the number put itointo the stack  3- another number push it  we take  top elements  3 -pop ,2-pop  2+3=5
#put the result back: stack =[5],4 push it stack =[5,4], take the toptwo 4-pop, 5-pop
#calculate 5*4 =20 , stack =[20]
#numbers goonmo the stack ,when we encounter an operator , we pop the required operands ,perform the operation and push the result back

#we have an input like
#tokens=["2","1","+","3","*"]
#left- right <-> one item , there are two possibilities  if te item is a number put into the stack by stack.append(number)
#if the itemis an operator, take the top nos out of the stack:
#b=stack.pop(), a= stack.pop() ,aoperator b put answer back to the stack if stack=[2,1]= b=1,a=2,2+1=3, stack =3

#when an operator appears
#b=stack.pop(),a=stack.pop(),then a-b,a/b,a+b,a*b
#then order matters for substraction and  division
#code


def evalRPN(tokens):# tokens is the parameter
#the paremeter tokens is used  to receive the input that we wqant  the function toprocess
    stack=[]
    for token in tokens:
        if token not in "+-*/":
            stack.append(int(token))# we right int to convert the numbers from stings to int
        else:
            b=stack.pop()
            a=stack.pop()
            if token == "+":
                stack.append(a+b)
            elif token == "-":
                stack.append(a-b)
            elif token == "*":
                stack.append(a*b)
            elif token == "/":
                stack.append(int(a/b))# truncation towards zero we int here because  division is supposed to produce  an integer by truncating toward zero
    return stack[0]#first elemnt of the stack
tokens=["2","1","+","3","*"]
print(evalRPN(tokens))
#we return the first element because after we have finished evaluating the  entire expression
#there should be only one value left in the stack , Example 2 1 +3 *, eventually stack will be 9 there is only one element
# its index o the value is 9 , mena sgive the final answer back to whoever called the function

# the order of if lese statements does not matters  python checks  top to bottom ,+ -false,-f, *-TRUE
#RETURN IS OUTSIDE THE FUNCTION  BECAUSE IT NEED TO PROCESS ALL THE TOKENS
#if we writr return inside for loop python  return immediately during the firt iteration ,so remaining tokens would never be processed 
                
*************************************************************************************************************************



#Daily Temperatures
#this one introduce an important new technique: the Monotonic Stack
#you have given the temperatureof several days
#[73,74,75,71,69,72,76,73]
# 73 -1 day 73-74 index 1-0 = 1day 75 4 days 75=2 next warmer than 75 is 76 is at index 6 so 6-2=4days, 69-72 -1 day
#72-76-1day,76- no warmer temperature
#for each day er need to find
#how many days do we have to wait until a warmer  temperature occurs
#for example 73-74 -1 day ,75-76 , 4 days
#this is where the monotonic stack - a stack maintained in a particular increasing / decreasing order

#Instuition - For every temperature ,keep looking to the right until you wind a warmer one
#but that can become o(n^2) because we may repeatedly examine the same temperature
#instead, we use a monotonic decreasing stack
#we store there indices not the temperature themselves
#bcz we need to calculate  current index-previous index

def dailyTemperatures(temperatures):
    result=[0]*len(temperatures)
    stack=[]
    #result stores the number of  days to wait


    for  i, temp in enumerate(temperatures):
        while stack and  temp>temperatures[stack[-1]]: #if todays temperature is warmer than the temperature
            #represented by the  topof the stack 
            previous_day=stack.pop()#remove that day from stack
            result[previous_day]=i-previous_day#calculate how mnay days it waited,store the answer in result
            #put today's index  into the stack
        stack.append(i)
    return result
temperatures=[73,74,75,71,69,72,76,73]
print (dailyTemperatures(temperatures))

# result=[0]*len(temperatures)= if len is 8 then result will be [0,0,0,0,0,0,0,0]
#creates a result list with the same number of positions as the temperature list ,initially filled with zeros
#we do this because we eventually need one asnwe for every temperature ,8 temperature-8 answers
#as we find warmer temperature the zeros will be filled with days else it remains 0

#the stack stores indices not temperature
#for  i, temp in enumerate(temperatures): ,if we writ fpr temp in temperature we  would get only the temperature
#but we need both index abd the temperature , enumerate gives us two things one i=index, temp=value
#when i=0 tempn =73

#  while stack and  temp>temperatures[stack[-1]]: , 2conditions, is the stack non empty python treates a non empty list as true and
#empty list as false ,while stack -keepdoing this  while the stcak has something inside it
#temp>temperatures[stack[-1]]:-is todaya's temperature warmer than the temperature represented by the top index of the stac
#suppose stack=[0] temperatures =[73,74,75], then stack[-1] mena slast item ijn the stack =0, means temperatures[0]=73
#now suppose temp=74>73 -true so while loop runs

#so as long as stack is not empty   AND today's temperature is warmer than the temperature belonging to the index at the
#top of the stack , keep processing
#previous_day=stack.pop(),suppose i=5,temp=72, the topof the stack is stack[-1]=4 ,pop removes the last word
#and stores in previous_day
#now i=5,previous_day=4 i- previos_day =5-4=1, that means the day at index 4 had to wait 1  day to reach a warmer temperature

#so result[4]=1 , now it becomes result=[0,0,0,.0,1,0,0,0],weare basically saying at index 4 ,the ans is 1 day
#stack.append(i),after dealing with the preivious day we add the current day to the stack
#before[2,3],after [2,3,5]
#dailyTemperature(temperature) - calculates result- return result- answer =result - print(answer)
#calling the function  executes the funcion, and the function'sreturn statement sends the calculated result back to the caller

***********************************************************************************************************************************



#Car Fleet
#This is another Stack-based problem,but it introduces a different idea:processing cars  based on their  arrival time
#car Fleet is aproblem where several cars are travelling toward the same  destination
#Each car has  a position ,a speed,the same destination
#Afaster  car behind a slowe car will eventually catch up to it.when that happens they travel together as a fleet(a group
#of cars moving together)

#intuition
#suppose the desitination is target =12, position [10,8,0,5,3],spped=[2,4,1,1,3]
#instead of speed we clculate ho much time each car needs ton reach the desination
#ex car at position 10 ,(12-10)/2=1,car at position 8 ,(12-8)/4=1 ,s ince the car at position 8 is behind  the car at 10 ,and

#both would arrive in the same time they form one fleet

def carFleet(target,position,speed):
    cars=sorted(zip(position ,speed),reverse=True)
    stack=[]
    for pos ,spd in cars:
        time=(target-pos)/spd

        if not stack or time>stack[-1]:
            stack.append(time)
    return len(stack)
target =12
position=[10,8,0,5,3]
speed=[2,4,1,1,3]
print(carFleet(target,position,speed))

#def carFleet(target,position,speed):  function which contains target-destination ,position,speed of cars
#cars=sorted(zip(position ,speed),reverse=True),zip pairs the position and its corresponding speed
#(10,2) (8,4),(0,1)(5,1)(3,3),sorted(), no we sort those pairs according to the position
#we use reverse =True ,so they are arranged from largest position to smallest position (10,2) (8,4) (5,1) (3,3)(0,1)

#because 10 position is closest to the target 12, so we want to process that car first
#creates cars=[ (10,2),(8,4) ,(5,1),(3,3),(0,1)]
#the stacks stores  the  arrival time of each fleet ,it does not store the car bthemselves
# for pos ,spd in cars:-we are going through each car 


# time=(target-pos)/spd -this calculates how long that car would take to reach the target if it travelled without being slowed down by another car
#formulta time= distance/speed 
#  if not stack or time>stack[-1]: not stack -if stack is empty,suppose stack=[1] and current car's timenis 7 then 7>1
#that means this car would arrive later than the fleet ahead, theresore it cannot catch that fleet
#so it forms a new fleet

#stack.append(time),if the condition is true we add this fleet'sarrival time to the stack
#after thate we get stack=[1,7]
# return len(stack)at the ebd the stack cntins the arrival time of every separate fleet
#stack=[1,7,12],len(stack) is 3

#reverse tells the sortbto sort the list in decending order

*************************************************************************************************************************************************
'''

##Longest Rectangle  in Histogram
#The Longest Rectangle in Histogram problem asks us to find the largest rectangular area that can be formed inside a histogram
#you are given an  array of heights , where each  number represents the height of a bar , and ecah bar has a width of 1
# our task is determine the maximum possible  araea opf a rectangle  formed by one or more  consecutive (adjacent ) bars
#ex , heights =[2,1,5,6,2,3],the largest rectangle has height =5,width =2, area =5*2=10
#ands =10

#A histogram is a graphical representation made of adjacent(directly next to each other  whrew height of each bar represents a numerical valu
#**** extra
#Frequency histogram ,relative frequency histogram , cumulative frequency histogram ,density / probability histogram
#THESE ARE TYPES BY data representation
#Frequency Histogram = shows the raw count of data points inside each specific interval
#Relative Frequency Histogram - Displays the fraction  or percentage  of the total  data set in each bin instead of araw count
#cumulative frequency-adds the count of each  bin to the sum of all previous bins to show a running total
#density /probability histogram :Scales  the y -axis   so the total area of all bars  adds up to 1 ,showing probability density

#types of distribution shape:
#Symmetric(Bell -shaped): forms a balanced  mirror image from the center , showing normal distribution ,forms bell -shaped curve where left and right  sides mirror each other
#uniform histogram:has bars of equal height , meaning values are venly spread across all bins 
#Bimodel Histogram :Features two distinct peaks ,often showing that the data combines two different groups
#Right -Skewed Histogram : Has a long tail on  the right soide ,meaning  most data  is low with a  few high value s
#left -skewed Histogram :Has a long tail on the left side,meaning most data is high with a few low values 

def largestRectangleArea(heights):
    stack=[]
    max_area=0
    for i ,h in enumerate(heights):
        start=i
        while stack and stack[-1] [1]>h:# if i write only -1 we get entire tuple ex:(3,2) v     `
            index ,height =stack.pop()
            width =i-index
            max_area=max(max_area ,height *width)
            start =index
        stack.append((start, h))
    for i, h  in stack:
        width =len(heights)-i
        max_area=max(max_area,h*width)
    return max_area
heights =[2,1,5,6,2,3]
print(largestRectangleArea(heights))


#the purpose of this program is  given a histogram , find the maximum area a rectangle that can be formed using consecutive bars
#while stack and stack[-1] [1]>h:-what is inside stack , stack.append((start,h]),we are putting a pair of tuple inside  into the stack
#(index,height),for ex stack=[(0,2),(2,5),(3,6)],so stack contains pairs not just numbers ,  stack[-1]-last elements ,stack[-1][1]-now we take [1]
#from that pair,python indexing (3,6),stack[-1][1],get the height from the last pair in the stack >h  we do this because previous bar =6 , current =2
#previous bar is taller `when we encounter shorter  bar the bar of heright cannot continue its rectanglethrough the current position
#therefore ,we need to calculat the rectangle that the 6-height bar could from before removing it fropm the stack

# index ,height =stack.pop() - index tells  us where that bar started in the original heights list
#so basiucally we take  the lat pair out of the stack and separate its two values
#its eqivalent to
#pair=stack.pop()
#index =pair[0]
#height =pair[1],  we are just using unpacking  to write it more cleanly ,index ,height =stack.pop()

#width =i-index, it vcalculates how many bars are there in loner and shorter bars
# we asking jho many consecutive bars can this height cover before we encounter  bar that is too short
#max_area=max(max_area ,height *width) we are finding the max area
#start =index,used to remember where the rectange startts 
#  stack.append((start, h))- rember this bar'sheight and the earliest  position from which it can form a rectangle

#for i, h  in stack:
#      width =len(heights)-i
#       max_area=max(max_area,h*width)

##we do this because while  during the min loop , some bars never encounterd  a shorter bar
#so they were never  popped from the stack  that means we haven't calculated thjerir rectangle areasit , ex heights=[2,4,4,4]
#after finishing the loop there is no shorter bar  after the 4s so the stack might contain [(0,2),(1,4)]
#the 4 height rectangle still waiting  so we need to calculate  its width other wise it can extend all the way to the end

#of the histogram  so we need to calculate width ,  width =len(heights)-i  4-1 =3 h=4 , w=3  a 4*3
#stack does  not contain poped elements ,so we calculate  width of unpoped bars in the stack
3








































    
    














