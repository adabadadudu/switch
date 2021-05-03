try:
   import switch
except:
    try:
      from switch import *
    except:
        try:
           from . import switch
        except:
            try:
               from .switch import *
            except:
              print("Program don't can load this function")
              quit()
              exit()
              
              
try:
   switch = switch
except:
   try:
      switch switch.switch
   except:
    print("Program don't can rename function switch")
