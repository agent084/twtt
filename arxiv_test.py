import os
import time
import json
from tqdm import tqdm
import sys
import re
import arxiv

final_dict = {}
for i in tqdm(range(487)):
    d = []
    with open(f"newphd_data{i}.json", 'r') as f:
        try:
            d.extend(json.loads(line) for line in f)
        except:
            continue
    s = set()
    categ = {}
    for e in d:
        if e['outlinks'] is not None:
            for j in e["outlinks"]:
                if re.match("https://arxiv.org/*", j) and re.match('2019*', e['date']):
                    k = re.findall(r'\d+', j)
                    try:
                        if len(k)==2:
                            s.add(f'{k[0]}.{k[1]}')
                    except:
                        print("eeeeeeeeeeeerror")
    for sh in s:
        paper=0
        try:
            paper = next(arxiv.Search(id_list=[sh]).results(),None)
        except:
            continue
        for c in paper.categories:
            if c in categ:
                categ[c] += 1
            else:
                categ[c] = 1
    try:
        final_dict[e['user']['displayname']] = categ
    except:
        print("error")
print(len(final_dict))

with open('phdarxiv_2019.json', 'w') as fout:
    json.dump(final_dict, fout)


# for i in d:
#     if re.findall(r'recruiting phd|phd position|hiring phd|phd students', str.lower(i['content'])):
#         print(i['content'])
