import json

def main():
    text = open("news.txt", "r").read().lower()
    sub_fptr = open("subs.json", "r")
    subs = json.load(sub_fptr)

    print (subs,type(subs))

    for k,v in subs.items(): #takes {k:v} and transforms to (k,v)
        text = text.replace(k,v)

    fptr = open("betternews.txt", "w")
    fptr.write(text)
    fptr.close()

main()

#file_opener = open("ch06/exercises/news.txt", "r")
#article = str(file_opener.read())
#file_opener.close()

#fptr = open("ch06/exercises/subs.json", "r")
#subs = json.load(fptr)
#fptr.close()
#better_news = article
#for k, v in subs.items():
#    better_news = article.replace(k,v)
#    print (k,v)
#file3 = open("ch06/exercises/ betternews.txt", "w")
#file3.write(better_news)
#file3.close()






