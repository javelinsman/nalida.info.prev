import re

f = open('data', 'r')
l = []
for line in f:
    if line[0] == '#':
        l.append([line])
    else:
        l[-1].append(line);
"""
print(l[0])
print(l[1])
print(l[2])
"""

d = {}
for i in range(len(l)):
    d[l[i][0].split('\t')[0]] = i;
    
#print(d);

res = []
for elem in l:
    try:
        obj = "{id:%d, text:%s, buttons:[%s]}"
        s_id = d[elem[0].split('\t')[0]]
        s_text = "'%s'" % elem[0].split('\t')[1].strip()
        buttons = []
        for e in elem[1:]:
            try:
                m = re.compile('(.*)\((.*)\)')
                txt = "'%s'" % m.match(e).group(1).strip()
                dst = d[m.match(e).group(2)]
                buttons.append("{dst: %d, text: %s}" % (dst, txt))
            except Exception as k:
                print('|-----------|')
                print(e)
                print(k)
                print('-----------')
        res.append(obj % (s_id, s_text, ','.join(buttons)))
    except Exception as e:
        print('*-----------*')
        print(elem);
        print(e)
        print('-----------')


print(res[0])

g = open('data.js', 'w')
g.write('datas = [%s]' % ',\n'.join(res));
g.close();

print("parsing complete")

