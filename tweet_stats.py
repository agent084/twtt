import json
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm
import math
import statistics
import numpy as np
# df=pd.read_csv('profs_for_graph.csv')
# tdf = df.loc[df["user_verified"] == '1']
# print(tdf)
# print(tdf['user_screen_name'].unique())
count=0
followerscount=0
retweets=[]
likes=[]
quotes=[]
replies=[]
# for i in tqdm(range(467)):
#     d = []
#     with open(f"{i}.json", 'r') as f:
#         try:
#             d.extend(json.loads(line) for line in f)
#             # if d[0]['user']['verified'] is True:
#             #     print(d[0]['user']['username'])
#             # followerscount += d[0]['user']['followersCount']
#             for e in d:
#                 retweets.append(e["retweetCount"])
#                 likes.append(e["likeCount"])
#                 replies.append(e["replyCount"])
#                 quotes.append(e["quoteCount"])
            
#         except:
#             continue
# for i in tqdm(range(1000,1211)):
#     d = []
#     with open(f"{i}.json", 'r') as f:
#         try:
#             d.extend(json.loads(line) for line in f)
#             # if d[0]['user']['verified'] is True:
#             #     print(d[0]['user']['username'])
#             # followerscount += d[0]['user']['followersCount']
#             for e in d:
#                 retweets.append(e["retweetCount"])
#                 likes.append(e["likeCount"])
#                 replies.append(e["replyCount"])
#                 quotes.append(e["quoteCount"])
#             # print(len(retweets), len(likes), len(replies), len(quotes))
#         except:
#             continue
# for i in tqdm(range(2000,2229)):
#     d = []
#     with open(f"{i}.json", 'r') as f:
#         try:
#             d.extend(json.loads(line) for line in f)
#             # if d[0]['user']['verified'] is True:
#             #     print(d[0]['user']['username'])
#             # followerscount += d[0]['user']['followersCount']
#             for e in d:
#                 retweets.append(e["retweetCount"])
#                 likes.append(e["likeCount"])
#                 replies.append(e["replyCount"])
#                 quotes.append(e["quoteCount"])
#             # print(len(retweets),len(likes),len(replies),len(quotes))
#         except:
#             continue
for i in tqdm(range(487)):
    d = []
    with open(f"newphd_data{i}.json", 'r') as f:
        try:
            d.extend(json.loads(line) for line in f)
            # if d[0]['user']['verified'] is True:
            #     print(d[0]['user']['username'])
            # followerscount += d[0]['user']['followersCount']
            for e in d:
                retweets.append(e["retweetCount"])
                likes.append(e["likeCount"])
                replies.append(e["replyCount"])
                quotes.append(e["quoteCount"])
            # print(len(retweets),len(likes),len(replies),len(quotes))
        except:
            continue
# print(len(retweets),len(likes),len(replies),len(quotes))
retweets=np.array(retweets)
likes=np.array(likes)
replies=np.array(replies)
quotes = np.array(quotes)
print(f'retweets: stdev-{np.std(retweets)},max-{max(retweets)},min-{min(retweets)},avg-{np.mean(retweets)},median-{np.median(retweets)}')
print(f'likes: stdev-{np.std(likes)},max-{max(likes)},min-{min(likes)},avg-{np.mean(likes)},median-{np.median(likes)}')
print(f'replies: stdev-{np.std(replies)},max-{max(replies)},min-{min(replies)},avg-{np.mean(replies)},median-{np.median(replies)}')
print(f'quotes: stdev-{np.std(quotes)},max-{max(quotes)},min-{min(quotes)},avg-{np.mean(quotes)},median-{np.median(quotes)}')
print(len(retweets),len(likes),len(replies),len(quotes))
