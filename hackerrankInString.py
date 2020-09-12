#DESCRIPTION:
#We say that a string contains the word hackerrank if a subsequence of its characters spell the word hackerrank. 
#For example, if string s="hhaacckkeerrannkk" it does contain hackerrank, but s="haackerank" does not. 
# In the second case, the second r is missing. If we reorder the first string as , it no longer contains the subsequence due to ordering.
#For each query, print YES on a new line if the string contains hackerrank, otherwise, print NO. 

#s = input string

def hackerrankInString(s):
    original = "hackerrank"
    j=0
    for i in range(len(s)):
        if s[i] == original[j]:
            j += 1
            if j == 10: #this stops the for loop from continuing in the event that "hackerrank" is found and the string is longer than that point
                break
    if j == 10: #if j reaches 10 then hackerrank has been found in the string
        return "YES"
    else:
        return  "NO"
