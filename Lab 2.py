
# a) Rabin Karp Algorithm

#q=prime
# d is the number of characters in the input alphabet ( if decimal , d = 10; alphabet
def rabinKarpMatcher(text, pat, radix, q):
    textLength = len(text)
    patLength = len(pat)

    p = 0           # pat(string ) corresponds to p(decimal) ; hash value for pat
    t = 0           # text(string ) corresponds to t(decimal) ; hash value for text
    h = pow(radix, patLength - 1) % q

    for i in range (patLength) :    #preprocessing  #Horner's method
        # Calculate the hash value of pattern and first window
        # of text
        #ord function()
        p = (radix * p + ord(pat[i])) % q
        t = (radix * t + ord(text[i])) % q

    for s in range (textLength - patLength + 1)  :     #matching #note +1
        # Check the hash values of current window of text and
        # pattern if the hash values match then only check
        # for characters on by one
        if p == t :
            if pat[0:patLength] == text[s : s+patLength] :
                print("Pattern occurs with shift", end=" ")
                print(s)
                break
        if s < textLength-patLength:
        # Calculate hash value for next window of text: Remove
        # leading digit, add trailing digit
            t = (t - h * ord(text[s])) % q  # remove letter s
            t = (t * radix + ord(text[s + patLength])) % q  # add letter s+m
            t = (t + q) % q     # make sure that t >= 0

# b) KMP algorithm

def kmpMatcher(T,P):
    textLen = len(T)
    patLen = len(P)
    arr = computePrefix(P)
    q = 0 #index for P[]

    for i in range (0,textLen):
        if P[q] != T[i]:  #next char do not match
            if q > 0:
                q = arr[q - 1]
        if P[q] == T[i] :       #next char matches
            q += 1
        if q == patLen:     #is all of P matched?       #!
            print(f"Pattern occurs with shift {i-(patLen-1)}") #!
            q = arr[q - 1]          #look for next match



def computePrefix(P):
    patLen = len(P)

    #if you wanted to use the Python list like an array in other languages,
    # then you could pre-create a list with its elements set to a null ,
    # and later, overwrite the values in specific positions
    # using python list as arrays
    arr = [0]*patLen
    i = 0
    for j in range (1,patLen):
        if P[i] != P[j]:
            if(i > 0 ):
                i = arr[i-1] #*
                if P[i] == P[j]:
                    i += 1
                    arr[j] = i
                else:
                    arr[j] = 0
            else :
                arr[j] = 0
                
        if P[i] == P[j]:
            i += 1
            arr[j] = i
    return arr

# c) TRIES
class Trie:
    head = {}  #create dictionary

    def add(self,word):
        cur = self.head     #to iterate
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]       #?
        cur['*'] = True
        print(cur)
        # * denotes the Trie has this word as item
        # if * doesn't exist, Trie doesn't have this word but as a path to longer word

    def search (self,word):
        cur = self.head
        for character in word:
            if character not in cur:
                return False
            cur = cur[character]

        if '*' in cur:
            return True
        else:
            return False

class SuffixTrie(object):

    def __init__(self, word):
        word += '*'  # add terminator
        # * denotes the Trie has this word as item
        # if * doesn't exist, Trie doesn't have this word but as a path to longer word
        self.root = {} #create dictionary
        for i in range(len(word)):
            cur = self.root #to iterate
            for char in word[i:]:
                if char not in cur:
                    cur[char] = {}  # adding new outgoing edge
                cur = cur[char] # to iterate , cur = cur.next

    def followPath(self, string):
        cur = self.root
        for char in string:
            if char not in cur:
                return None
            cur = cur[char]
        return cur

    def hasSubstring(self, string):
        return self.followPath(string) is not None

    def hasSuffix(self, string):
        node = self.followPath(string)
        return node is not None and '*' in node



# Driver code
text = "algorithmisfun"
pat = "fun"

# a)
rabinKarpMatcher(text, pat, 10, 997)

#b)
#print(computePrefix(pat))
kmpMatcher(text,pat)

#c)

if __name__ == "__main__":
    st = SuffixTrie("algorithmisfun")
    a = input()
    print(str(st.hasSuffix(a)))