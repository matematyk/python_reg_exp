class Expr:
     pass

class Num(Expr):
    def __init__(self,n):
        self.x=n

    def __repr__(self):
        return f"Num({self.x})"

    def val(self):
        return self.x

class Min(Expr):
    def __init__(self,n):
        self.x=n

    def __repr__(self):
        return f"Min({self.x!r})"

    def val(self):
        return -self.x.val()



class BinOp(Expr):
    def __init__(self, n, m):
        self.left = n
        self.right = m

    def __repr__(self):
        return f"{self.__class__.__name__}({self.left!r},{self.right!r})"
        # return "{}({!r},{!r})".format(self.__class__.__name__,self.left,self.right)
        # return "{0}({1!r},{2!r})".format(self.__class__.__name__,self.left,self.right)
        # return "{0}({1},{2})".format(self.__class__.__name__, repr(self.left), repr(self.right))
        

    def val(self):
        return self.op(self.left.val(), self.right.val())

    
class Add(BinOp):
    def op(self, x, y):
        return x + y
    
class Sub(BinOp):
    def op(self, x, y):
        return x - y
    
class Div(BinOp):
    def op(self, x, y):
        return x / y

class Mul(BinOp):
    def op(self, x, y):
        return x * y



def parse(s):
    s = s + "$"
    i = 0 

    def parseN():
        nonlocal i
        j = i 
        print(i)
        while s[i].isdigit():
            i += 1

        return Num(int(s[j:i]))
    def parseC():
        nonlocal i
        if  s[i] == "-":
            i += 1
            return Min(parseC())
        elif s[i] == "(":
            i += 1
            reg =  parseE()
            i += 1 
            return reg
    
        else: # liczba
            return parseN()
    def parseS():
        nonlocal i
        res = parseC()
        while s[i] == "*" or s[i] == "/":
            if s[i] == "*":
                i += 1
                y = parseC() 
                res =  Mul(res, y)
            elif s[i] == "/":
                i += 1
                y = parseC() 
                res = Div(res, y)
        return res
            
    def parseE():
        nonlocal i
        res = parseS()
        while s[i] == "+" or s[i] == "-":
            if s[i] == "+":
                i += 1
                y = parseS() 
                res =  Add(res, y)
            elif s[i] == "-":
                i += 1
                y = parseS() 
                res = Sub(res, y)
        return res

    '''
    gramatyka:
     E = S (('+'|'-') S)*      # wyrazenie - DONE
     S = C (('*'|'/') C)*      # skladnik  - DONE
     C = N | '-'C | '('E')'    # czynnik   - DONE...
     N = n                     # liczba    - DONE!
    '''

    return parseE()
e = parse("(1+2)*2*3")
print(e)
print(e.val())
e = Sub(Mul(Min(Num(5)), Num(3)),Num(17))
x = input() 
z = parse(x) 
print(z.val())
#print(repr(e))
