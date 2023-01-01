import os
import platform


username=os.getlogin() #to get username
detail=platform.uname() # ('Windows', 'name', 'XP', '5.1.2600', 'x86', 'x86 Family 6 Model 15 Stepping 6, GenuineIntel')
print(username+' '+details)
