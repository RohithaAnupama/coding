class Convert_int:
   def solve(self, n):
      sign = '-' if n<0 else ''
      n = abs(n)
      if n < 3:
         return str(n)
         s = ''
      while n != 0:
         s = str(n%3) + s
         n = n//3
      return sign+s
n=input()
ob = Convert_int()
print(ob.solve(n))
