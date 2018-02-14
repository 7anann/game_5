array1 = ['0','1','2','3','4','5','6','7','8','9']
array2 =  ['0','1','2','3','4','5','6','7','8','9']
list = ['A','B','C','D','E','F','G','H','I','J']
list2 = ['J','H','F','D','B','I','G','E','C','A']
array3 = ['0','1','2','3','4','5','6','7','8','9']
array4 = ['9','7','5','3','1','8','6','4','2','0']
for i in array1:
    i = list[0:10]
for j in array2:
    j = list2[0:10]
print(array1)
print(array2)
player1 = 0
player2 = 0
count = 0
count += 1
z = int()
a = int()
while (array1[0]!= '*') or (array1[1]!= '*') or (array1[2]!= '*') or  (array1[3] != '*') or (array1[4] != '*') or (array1[5] != '*') or (array1[6] != '*') or (array1[7] != '*') or (array1[8] != '*') or (array1[9] != '*'):
  print(" first player choose 2 numbers")
  for x in array3:
    x = int(input())
    break
  for y in array4:
    y = int(input())
    break

  
  if (x == z and y == a):
       print("Numbers are already chosen")
  if (array1[x] == '*' and array2[y] == '*'):
        print("Choose another numbers")
        
  elif array3[x] == array4[y]:
     array1[x] = '*'
     array2[y] = '*'
     player1 += count
     print " new array is", array1 , array2
     print" player 1 scores", player1
  while (array1[0:10] == '*'):
         break
     
  if array3[x] != array4[y]:
    print(" Two characters are not equal")    
 
     
  print(" second player choose 2 numbers")
  for z in array3:
    z = int(input())
    break
  for a in array4:
    a = int(input())
    break
  
  
  if (z == x and a == y):
     print("Numbers are already chosen")
     
  if (array1[z] == '*' and array2[a] == '*'):
        print("Choose another numbers")
          
  
  elif array3[z] == array4[a]:
     array1[z] = '*'
     array2[a] = '*'
     player2 += count
     print " new array is", array1 , array2
     print" player 2 scores", player2
     
  
  while (array1[0:10] == '*'):
         break
  if array3[z] != array4[a]:
    print(" Two characters are not equal")
  
         
if player1 > player2:
    print("player 1 wins")
elif player1 < player2:
    print("player 2 wins")
else:
    print ("Both players are equal")
    


 
  

  




 






    
