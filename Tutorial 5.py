# 1. Naive/ Brute Force Algorithm
def naive_string_matcher(T,P) :
    textLength = len(T)
    patternLength = len(P)
    for textLength in range(0,textLength - patternLength)  :
        if P == T[textLength: textLength + patternLength] :
            print("Pattern occurs with shift ",end="")
            print(textLength)


# Python find substring in string:

# Driver code
P = "314153" #pattern
T = "2359022673314153921" #text

naive_string_matcher(T,P)