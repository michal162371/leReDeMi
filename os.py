import os
from datetime import datetime
print(os.stat('ty.txt').st_size)
# time=os.stat('ty.txt').st_mtime
# os.rename('ty.txt','ty.txt'+str(time))
print(os.path.exists('./מוזיקה/בנות'))
things = os.listdir()
for th in things:
   if th.endswith('mp3'):
     os.rename(th,'sing//' + th)


for dirpath, dirnames, filenames in os.walk('.\sing'):
  if len(dirnames)==0 and len(filenames)==0:
            os.rmdir(dirpath)
            # הערה: באם יש תיקיה
            #  ריקה בתוך תקיה ריקה צריך 
            # להפעיל את הפונקציה כמה פעמים

 
mod_time = os.stat('./sing/lo levad.mp3').st_mtime
print(datetime.fromtimestamp(mod_time))

<<<<<<< HEAD
#homework at python from techer Malki Zilberberg 
=======
>>>>>>> 79462c694cf1d79c982ffff41df708cd9d31e1b3
