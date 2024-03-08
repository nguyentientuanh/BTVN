class car:
    def __init__(self) :
        self.animals={
            'mau sac':'do',
            'chat lieu':'nhom',
            'kieu dang':'the thao',
            'cho ngoi':'4 cho',
            'gia tien':'400',
            'thuong hieu':'honda'
        }

    def phanh(self):
        print("stop")

    def chay(self):
        print("run")
    
class hcn:
    def __init__(self,cd,cr):
        self.cd=cd
        self.cr=cr

    def area(self):
        return self.cd*self.cr
    
    def p(self):
        return (self.cd+self.cr)*2
    
hcn1=hcn(100,50)
print(hcn1.area())
print(hcn1.p())

class human:
    name=''
    age=0

    def say(self):
        print("say something")
    def move(self):
        print("move to that place")

