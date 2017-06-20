class NewStack:    
    
    def __init__(self,siz):
        self.top1 = 0
        self.top2 = siz-1
        self.siz = siz
        self.stck = [None]*siz

    def NewPush1(self,element):
        if self.top1<self.top2:
            self.stck[self.top1] = element
            self.top1 += 1
            print("Item pushed")
        else:
            print("Stack Overflow")

    def NewPop1(self):
        if self.top1 > -1:
            self.top1 -= 1
            return self.stck[self.top1]
        else:
            return "Stack Underflow"

    def NewPush2(self,element):
        if self.top1<=self.top2:
            self.stck[self.top2] = element
            self.top2 -= 1
            print("Item pushed")
        else:
            print("Stack Overflow")

    def NewPop2(self):
        if self.top2 < self.siz:
            self.top2 += 1
            return self.stck[self.top2]
        else:
            return "Stack Underflow"


 st = NewStack(5)
 st.NewPush1(1)
 st.NewPush2(3)
 st.NewPush1(2)
 st.NewPop1()
 st.NewPop2()