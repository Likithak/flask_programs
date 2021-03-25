class EvenNumber(Exception):
    pass
while True:
    try:
        n=10
        if n%2==0:
            raise EvenNumber("given number is even number")
        else:
            a=n+1
            print(a)
    
    except EvenNumber as e:
        print(e)
        
       
            


    
   
    
    
        

    
