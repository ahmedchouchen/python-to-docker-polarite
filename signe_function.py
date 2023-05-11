def signe(a):
 if (a.isnumeric()):
       a = float(a)
       if a > 0:
         Resultat = "nombre positive  "
       elif a == 0:
         Resultat = "nombre null "
 else:
       try:
          a= int(a)
          if a < 0 :
            Resultat = "nombre negative"
       except ValueError:
            Resultat = "SVP donner un nombre entier"
 print (Resultat)
