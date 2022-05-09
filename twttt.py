from numpy import append
import pandas as pd
import tweepy
import time
import json
from tqdm import tqdm
auth = tweepy.OAuth2BearerHandler("insert api key")
api = tweepy.API(auth)

def filter_via_keywords(user_obj,query):
    query_keywords = query.lower().split()
    d = user_obj.description.lower().split()
    descriptive_words = ['researcher','professor','prof','scientist','faculty','cs','ml','ai','nlp','cv',\
        'computer','vision','natural','language','machine','learning','artificial','intelligence','neural'
        'fair','google','meta','apple','microsoft','research','data','science','technology']
    #descriptive_words.extend(iter(place.lower().split()))
    origin = user_obj.location
    name = user_obj.name
    name_keywords = name.lower().split()
    if set(name_keywords).intersection(set(query_keywords)) and set(descriptive_words).intersection(set(d)):
        return user_obj.id,user_obj.screen_name,name,True

    screen_name = user_obj.screen_name
    screen_name_keywords = screen_name.lower().split()

    return '','','',False
    # followers_count = user_obj.followers_count
    # if followers_count > 100 or 
    #     return True
def get_profs():
    df = pd.read_csv('depts.csv')
    profs = df[ (df['area']=='aaai') | (df['area']=='cvpr') | (df['area']=='iccv') | (df['area']=='icml') | (df['area']=='chiconf') | (df['area']=='mlmining')\
            | (df['area']=="kdd") | (df['area']=="emnlp") | (df['area']=="acl") | (df['area']=="ubicomp") | (df['area']=="chi") | (df['area']=="robotics")]

    profs = profs['name'].unique().tolist()
    return profs

prof_dict=[]
def search_people(query):
    user_objects:list = api.search_users(q=query,page=1,count=10)
    for user in user_objects:
        user_id,user_name,actual_name,flag = filter_via_keywords(user,query)
        if flag is True:
            prof_dict.append({'user_id':user_id,'user_name':user_name,'actual_name':actual_name})
            break

prof_list=get_profs()
try:
    for prof in tqdm(range(6001,7000)):
        search_people(prof_list[prof])
        time.sleep(1.1)
except:
    print("erororr")

with open('test6.json', 'w') as fout:
    json.dump(prof_dict, fout)
#json.dumps(prof_dict)
print(prof_dict)