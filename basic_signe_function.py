def basic_signe(a):


    if (a.isnumeric()):
      a=int(a)
    
      if a>0 :
       result = "positive number "
      elif a == 0:
       result = "null  number"
      else :
       result = "negative number"
   
   
    
    else:
     result = "Please enter a valid number "
    

    return result
