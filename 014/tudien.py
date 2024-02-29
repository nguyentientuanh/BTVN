dictionary={
    'cat' : 'meo',
    'dog' : 'cho',
    'turtle':'rua',
    'monkey':'khi',
    'dragon':'rong',
    'human':'connguoi'
}

def find(dictionary,word):
    for i in dictionary:
        if dictionary[i]==word:
            return dictionary[i]
    return
word=input("nhap tu can tra cuu:")
if find(dictionary,word)!=None:
    print(find(dictionary,word))
else:
    print("khong co trong tu diwn")
    