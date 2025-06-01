for n in range(100,200):
   for i in range(2,n):
      if n%i==0:
         break;
   if i==n-1:
      print(n,end=" ")