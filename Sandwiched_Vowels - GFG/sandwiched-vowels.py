#User function Template for python3

  
def Sandwiched_Vowel(s):
    #Complete the function
    vowels=['a','e','i','o','u']
    s=list(s)
    li=s[::]#this creates a copy of string ,by modifying the list the string cannot change
    for i in range(1,len(s)-1):
        if s[i-1] not in vowels and s[i+1] not in vowels and s[i] in vowels:
            li[i]=0# This line assigns the value 0 to the element at index i in the list li. In this line,
                        # i is a variable that presumably holds a specific index value.
    li=[x for x in li if x!=0]#This line creates a new list comprehension. It iterates over each element x in the original list li and includes it in the new list only if x is not equal to 0. In other words, it filters out all 0 values from the list. After this line of code, li will contain only the elements from the original list that are not equal to 0.
    return "".join(li)#This line joins the elements of the modified list li into a single string. It uses the join() method of strings to concatenate the elements in the list. The "" empty string is used as a separator, which means that the elements will be concatenated together without any spaces or characters in between. The result is a single string containing all the non-zero elements from the original list.
            
    
 


#{ 
 # Driver Code Starts
#Initial Template for Python 3


   

for _ in range(0,int(input())):
    s = input()
    v = Sandwiched_Vowel(s)
    print(v)
    
# } Driver Code Ends