from numpy import append
import pandas as pd
import tweepy
import time
import json
from tqdm import tqdm
from scholarly import scholarly

# def get_profs():
#     df = pd.read_csv('depts.csv')
#     profs = df[(df['area'] == 'aaai') | (df['area'] == 'cvpr') | (df['area'] == 'iccv') | (df['area'] == 'icml') | (df['area'] == 'chiconf') | (df['area'] == 'mlmining')
#                | (df['area'] == "kdd") | (df['area'] == "emnlp") | (df['area'] == "acl") | (df['area'] == "ubicomp") | (df['area'] == "chi") | (df['area'] == "robotics")]

#     profs = profs['name'].unique().tolist()
#     return profs

# hindex={}
# prof_list = get_profs()
# for prof in tqdm(range(1000)):
#     search_query = scholarly.search_author(prof_list[prof])
#     author = next(search_query,None)
#     if author is not None:
#         hindex[prof_list[prof]] = scholarly.fill(author, sections=['indices'])['hindex']

with open('h-index-sco.json', 'r') as fout:
    data =json.load(fout)
print(len(data))
sorted_list = sorted(data, key=data.get)
print(data[sorted_list[len(sorted_list)-1]])
print(sorted_list)