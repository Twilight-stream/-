import re

with open("secret.daz",'r',encoding='utf-8') as f:
    with open("interpretation.txt",'w',encoding='utf-8') as w:
        data = f.read()
        num = re.findall(r'[^X]+',data)
        lis = []
        for i in num:
            lis.append(chr(int(i,16)))
        inter = ''.join(lis)
        w.write(inter+'\n')
        w.write("<解密人>2023090903017<情报总字数>"+str(len(lis)))