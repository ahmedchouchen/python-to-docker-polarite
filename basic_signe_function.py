def basic_signe(a):


if (a.isnumeric()):
       a = float(a)
       if a > 0:
         result = "positive number "
       elif a == 0:
         result = "null  number"


else:
      try:
          a= int(a)
          if a < 0 :
            result = "negative number"
      except ValueError:
         result = "Please enter a valid number "

print (result)
