#DESCRIPTION:
#Letters in some of the SOS messages are altered by cosmic radiation during transmission. Given the signal received by Earth as a string, S,
#determine how many letters of Sami's SOS have been changed by radiation.
#For example, Earth receives SOSTOT. Sami's original message was SOSSOS. Two of the message characters were changed in transit. 


def marsExploration(s):
    counter = 0
    #Make an "original" SOS string as long as the input string
    original = ("SOS"*(int(len(s)/3)))
    #Compare the 2 strings at each point
    for i in range(len(s)):
        if s[i] != original[i]:
            counter += 1
    return counter

#E.G: print(marsExploration("SOSSOT")) will return 1, as only one character is different.
