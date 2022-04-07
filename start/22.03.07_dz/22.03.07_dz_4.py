text = """Call me Ishmael. Some years ago - never mind how long precisely - having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen, and regulating
the circulation. - Moby Dick"""
text_split=[]
text_new=[]
text_done=[]
text=text.split("\n")
for i in text:
    text_split=text_split+[i.split()]
for i in text_split:
    text_new = text_new+[' '.join(word for word in i if len(word)>3)]
for i in text_new:
    text_done=text_done+[i.split()]
print(text_done)
