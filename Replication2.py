def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text) - len(Pattern) + 1):
        if Text[i:i + len(Pattern)] == Pattern:
            count += 1
    return count 

def FrequencyMap(Text, k):
	freq = {}
	n = len(Text)
	for i in range(n-k+1):
		Pattern = Text[i:i+k]
		freq[Pattern] = 0
		for i in range(n-k+1):
			if Text[i:i+k] == Pattern:
				freq[Pattern] += 1
	return freq			

def FrequentWords(Text, k):
    words = []
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    for key in freq:
       if freq[key] == m:
       	words.append(key)
    return words

    #run the FrenquencyMap(Text, k) function as a subroutine to the above function

def ReverseComplement(Pattern):
    Pattern = Reverse(Pattern) # reverse all letters in a string
    Pattern = Complement(Pattern) # complement each letter in a string
    return Pattern
def Reverse(Pattern):
    rev = ""
    for char in Pattern:
        rev = char + rev
    return rev
def Complement(Pattern):
    complement = ""
    for char in Pattern:
        if char == "A":
            complement += "T"
        if char == "T":    
            complement += "A"
        if char == "C":
            complement += "G"
        if char == "G":
            complement += "C"
    return complement 

def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    for i in range(len(Genome)-len(Pattern)+1):
        if Pattern == Genome[i:i+len(Pattern)]:
            positions.append(i)
    return positions

def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        array[i] = PatternCount(symbol, ExtendedGenome[i:i+n//2])
    return array    

#run PatternCount(Pattern, Text) as  a subroutine

def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    array[0] = PatternCount(symbol, Genome[0:n//2])
    for i in range(1, n):
        array[i] = array[i-1]
        if ExtendedGenome[i-1] == symbol:  #if the previous element excluded from the window is symbol, then reduce the count of the symbol by 1 
            array[i] = array[i]-1
        if ExtendedGenome[i+(n//2)-1] == symbol: #if the new element added in the widow is symbol, then add 1 to the symbol count, else add 0. 
            array[i] = array[i]+1
    return array
    
    #this window just looks at the first or the excluded element of the window and the last or the newly added element in the window and sees if it matches with the given symbol
    #run PatternCount(Pattern, Text)    

  #SkewArray
  def SkewArray(Genome):
    Skew = list(range(len(Genome)+1))
    Skew[0] = 0
    for i in range(1, len(Genome)+1):
        if Genome[i-1] in "AT":
            Skew[i] = Skew[i-1]
        elif Genome[i-1] == "G":
            Skew[i] = Skew[i-1]+1
        elif Genome[i-1] == "C":
            Skew[i] = Skew[i-1]-1
    return Skew         
   
  #MinimumSkewArray
  def MinimumSkew(Genome):
    positions = [] 
    SA = SkewArray(Genome)
    m = min(SA)
    for i in range(len(SA)):
        if SA[i] == m:
            positions.append(i)
    return positions

    #run SkewArray(Genome) as a subroutine


  def HammingDistance(p, q):
  	count = 0
  	for i in range(len(p)):
  		if p[i] != q[i]:
  			count += 1
  	return count
    	
 def  ApproximatePatternMatching(Text, Pattern, d):
 	positions = []
 	for i in range(len(Text) - len(Pattern)+1):
 		if HammingDistance(Text[i:i+len(Pattern)], Pattern) <= d:
 			positions.append(i)
 	return positions		
    		
  #run HammingDistance(p, q) as a subroutine  		  	
#for the last ApproximatePatternMAtching(), a count is generated instead of a list 
    

