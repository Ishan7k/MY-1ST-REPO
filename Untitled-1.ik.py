class ik:
    def _add(self,a,b):
     self.a=a
     self.b=b
     sum=a+b
     print("addition=",sum)
class ab(ik):
    def _subs(self,a,b):
      self.a=a
      self.b=b
      dif=a-b
      print("difference=",dif)
class rk(ab):
    def _multiplication(self,a,b):
       self.a=a
       self.b=b
       multi=a*b
       print("product=",multi)
A1=rk()
A1._add(5,6)
A1._subs(7,9)
A1._multiplication(11,9) #did on own ,multilevel inheritance pg


