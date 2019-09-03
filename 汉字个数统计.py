fi=open('天龙八部-网络版.txt','r',encoding='utf-8')
fo=open('天龙八部-汉字统计.txt','w',encoding='utf-8')
txt=fi.read()
d={}
for c in txt:
    d[c]=d.get(c,0)+1
del d[' ']
del d['\n']

ls=[]
for k in d:
    ls.append('{}:{}'.format(k,d[k]))

fo.write(','.join(ls))
fi.close()
fo.close()