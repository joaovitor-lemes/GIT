
def parouimpar(number):

    if number % 2 == 0:
        return "O numero é par"
    
    return "O numero não é par"
    
parouimpar(25)



def mult(*args):
    total = 0
    for i in args:
        total += i
        
    return total

#print(mult(1,2,3,5,9))
        
