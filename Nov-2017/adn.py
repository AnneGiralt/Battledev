
#*******
#* Read input from STDIN
#* Use echo or print to output your result, use the /n constant at the end of each result line.
#* Use:
#*      local_print (variable ); 
#* to display simple variables in a dedicated area.
#* ***/
import sys
import itertools

lines = ['5', 'ATTGC', 'CG', 'CGC', 'TAA', 'GCG']


tab = lines[1:]
long = 0

# Calcul de la longueur l des brins brin :
for frag in tab:
    long+= len(frag)
l = int(long/2)


# Calcul de tous les arrangement possibles de fragments :  [("ATTGC","CG","CGC", "TAA", "GCG")]
possibles = itertools.permutations(tab)
liste_poss = list(possibles)
 

# Prends un nuple type ("ATTGC","CG","CGC", "TAA", "GCG") et renvoie les brins de la forme ['ATTGC','CGC'] si possible, False sinon.
def evaluate1(nuple):
    i=0
    long=0
    brin1 = []
    brin2 =[]
    
    while long < l:
        brin1.append(nuple[i])
        long+=len(nuple[i])
        i+=1
        if long >l:
            return False
        
    while i <len(nuple):
        brin2.append(nuple[i])
        i+=1
    return brin1,brin2

#liste de liste à deux élts  
corrects1=[]    
  
# On remplis le tableaux corrects1 de possibilités après un premier tri 
for poss in liste_poss:
    result = evaluate1(poss)
    if result!= False:
        corrects1.append(result)



def testons(a,b):
    if a == 'T' and b != 'A':
        return False
    if a== 'C' and b!='G':
        return False
    if a== 'A' and b!='T':
        return False
    if a== 'G' and b!='C':
        return False
        
    return True



# prend un coupe de brin sous le forme (['ATTGC','CGC'], ['ATTGC','CGC'])   et regarde si ils sont bien compatible au sens de l'adn (ATCG):
def evaluate2(couple):
    b1 = "".join(couple[0])
    b2 = "".join(couple[1])
    return all(testons(b1[j],b2[j]) for j in range(l))


for j in range(len(corrects1)):
    if evaluate2(corrects1[j]):
        result = corrects1[j]
        break

result

resultat = " ".join(result[0])
resultat+="#"
resultat+= " ".join(result[1])

print(resultat)

