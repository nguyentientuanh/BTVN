import random

class flashcard:
    def __init__(self):
        self.animals={
            'con ong':'bee',
            'con tho':'rabbit',
            'con cua':'crab',
            'con meo':'cat',
            'con ngua':'horse',
            'con khi':'monkey',
            'con lua':'donkey'
        }

    def quiz(self):
        while True:

            vn,e=random.choice(list(self.animals.items()))
            print("Tieng Anh cua '{}' la ".format(vn))
            user_answer=input()

            if user_answer.lower()==e:
                print("Dung")
            else:
                print("Sai")
            
            option=int(input("Nhap 0 de tien tuc:"))
            if option:
                break
        print("ket thuc")

fc=flashcard()
fc.quiz()