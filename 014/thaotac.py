text ="Khai bao ham dem dem dem do do  mot mot "
def count(text):
    dem=0
    text_list=text.split()
    for i in text_list:
        i.lower()
        i.strip()
        if i==word:
            dem=dem+1
    num_words={word:dem}
    print(num_words)
word=input("nhap tu ban muon kiem tra:")
count(text)