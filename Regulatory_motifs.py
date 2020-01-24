def Count(Motifs):
    count = {} 
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
             count[symbol].append(0)
        
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    
    return count

def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    count = Count(Motifs)
    for i in count:
        for j in range(k):
            count[i][j] = count[i][j]/t
            
    
    return count   

    #run Count(Motifs) as a subroutine 

def Consensus(Motifs):
    k = len(Motifs[0])
    count = Count(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus     
    
    #run Count(Motifs) as a subroutine   

def Score(Motifs):
    consensus = Consensus(Motifs)
    count = 0
    for motif in Motifs:
        for index in range(len(motif)):
            if motif[index] != consensus[index]:
                count += 1
    return count

 #run Consensus(Motifs) and Count(Motifs) as subroutines     

def Pr(Text, Profile):
   
    p = 1
    for i in range(len(Text)):
        p = p * Profile[Text[i]][i]
    return p


def ProfileMostProbableKmer(text, k, profile):
    n = len(text)
    m = 0
    index = 0
    for i in range(n-k+1):
        s = text[i:i+k]
        p = Pr(s, profile)
        if m < p:
            m = p
            index = i
    return text[index:index+k]        

 #run Pr(text, profile) as a subroutine        

 def GreedyMotifSearch(Dna, k, t):
    # type your GreedyMotifSearch code here.
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    for m in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][m:m+k])
        for j in range(1, t):
            P = Profile(Motifs[0:j])
            Motifs.append(ProfileMostProbableKmer(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs

    #run all the above functions as subroutines (except the last one, duh!)

def CountWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    count = {}
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
             count[symbol].append(1)
        
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    
    return count    

def ProfileWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    count= CountWithPseudocounts(Motifs)
    profile = CountWithPseudocounts(Motifs)
    for i in count:
        for j in range(k):
            profile[i][j] = count[i][j]/(count["A"][j]+count["C"][j]+count["G"][j]+count["T"][j])
    return profile


    #run CountWithPseudocounts(Motifs) as a subroutine

def GreedyMotifSearchWithPseudocounts(Dna, k, t):
    BestMotifs = [] # output variable
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    for m in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][m:m+k])
        for j in range(1, t):
            P = ProfileWithPseudocounts(Motifs[0:j])
            Motifs.append(ProfileMostProbableKmer(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs


    #run all the subroutines just as usual. However, change Counts() to CountsWithPseudocounts() and Profile() to ProfileWithPseudocounts()    
def Motifs(Profile, Dna):
    k = len(Profile)   #omit this while running this as a subroutine for RandomizedMotifSearch()
    ProfileMostProbableKmer = []
    for i in Dna:
        ProfileMostProbableKmer.append(ProfileMostProbablePattern(i, k, Profile))
    return ProfileMostProbableKmer   

    # Insert your ProfileMostProbablePattern(Pattern, k, Profile) and Pr(Pattern, Profile) functions here.

#import random module
def RandomMotifs(Dna, k, t):
    motifs = []
    l = len(Dna[0])
    for i in Dna:
        index = random.randint(1, l-k)
        motifs.append(i[index: index+k]) 
    return motifs        

def RandomizedMotifSearch(Dna, k, t):
M = RandomMotifs(Dna, k, t)
    BestMotifs = M
    while True:
        Profile = ProfileWithPseudocounts(M)
        M = Motifs(Profile, Dna)
        if Score(M) < Score(BestMotifs):
            BestMotifs = M
        else:
            return BestMotifs   

#run RandomMotifs(), ProfileWithPseudocounts(), Motifs(), Score() and their subroutines

def Normalize(Probabilities):
    norm = Probabilities.copy()
    for key in Probabilities:
        norm[key] = Probabilities[key]/sum(Probabilities.values())
    return norm    
        
   #from random import uniform     
def WeightedDie(Probabilities):
    kmer = '' # output variable
    p = uniform(0, 1)
    sum = 0
    for key in Probabilities:
        if sum <= p <= sum+Probabilities[key]:
            kmer = key
            return kmer
        else:
            sum = sum+Probabilities[key]
    
def ProfileGeneratedString(Text, profile, k):
    n = len(Text)
    probabilities = {}
    for i in range(0,n-k+1):
        probabilities[Text[i:i+k]] = Pr(Text[i:i+k], profile) #construction of the dictionary
    probabilities = Normalize(probabilities) #normalize the dictionary only after it is completely costructed
    return WeightedDie(probabilities)

    # first Pr, Normalize, and WeightedDie below this line