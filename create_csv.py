import os
import time
import json
from tqdm import tqdm
import sys
import pandas as pd
ref_dict = {'id':'', 'timestamp_utc':'', 'local_time':'', 'user_screen_name':'', 'text':'', 'possibly_sensitive':'', 'retweet_count':'', 'like_count':'', 'reply_count':'', 'lang':'', 'to_username':'', 'to_userid':'', 'to_tweetid':'', 'source_name':'', 'source_url':'', 'user_location':'', 'lat':'', 'lng':'', 'user_id':'', 'user_name':'', 'user_verified':'', 'user_description':'', 'user_url':'', 'user_image':'', 'user_tweets':'', 'user_followers':'', 'user_friends':'', 'user_likes':'', 'user_lists':'', 'user_created_at':'',
            'user_timestamp_utc': '', 'collected_via': '', 'match_query': '', 'retweeted_id': '', 'retweeted_user': '', 'retweeted_user_id': '', 'retweeted_timestamp_utc': '', 'quoted_id': '', 'quoted_user': '', 'quoted_user_id': '', 'quoted_timestamp_utc': '', 'collection_time': '', 'url': '', 'place_country_code': '', 'place_name': '', 'place_type': '', 'place_coordinates': '', 'links': '', 'domains': '', 'media_urls': '', 'media_files': '', 'media_types': '', 'mentioned_names': '', 'mentioned_ids': '', 'hashtags': ''}
data = ['Ben Recht', 'Maneesh Agrawala', 'Claire Cardie', 'Jeffrey Heer', 'Jimeng Sun', 'Michael Kearns', 'Nigel Shadbolt', 'Steve Benford', 'Tom Rodden', 'David Jones', 'Kostas Daniilidis', 'Arvind Krishnamurthy', 'Bamshad Mobasher', 'Kwan-Liu Ma', 'Margaret Martonosi', 'Nick Feamster', 'Geoffrey Challen', 'Paul Dourish', 'Danaë Metaxa', 'Dong Zhang', 'Forest Agostinelli', 'Jian Yang', 'Julio Marco', 'Kristen Johnson', 'Laure Thompson', 'Meiyi Ma', 'Michael Albert', 'Steven Holtzen', 'Peter Brusilovsky', 'Rada Mihalcea', 'Somesh Jha', 'Maarten de Rijke', 'Ross Anderson', 'Kyunghyun Cho', 'Carsten Rother', 'Thad Starner', 'Chen Change Loy', 'Mayank Goel', 'Dan Suciu', 'Lothar Thiele', 'Anupam Joshi', 'Noah A. Smith', 'Gregory D. Abowd', 'Silvio Savarese', 'Aishwarya Agrawal', 'Atul Ingle', 'Bapi Chatterjee', 'Edward Chien', 'Elahe Soltanaghai', 'Jie Jiang', 'Jinwoo Choi', 'Madalina Fiterau', 'Natalie Parde', 'Sara Heitlinger', 'Sarah Wiseman', 'Steve Kroon', 'Tongyang Li', 'Anne Rogers', 'Milind Tambe',
        'Jim Hendler', 'Peter Stone', 'Ming C. Lin', 'Maja Pantic', 'Steffen Staab', 'Thomas Brox', 'Chunhua Shen']
final_list = [] #each dict->row

for i in tqdm(range(467)):
    d = []
    with open(f"{i}.json", 'r') as f:
        try:
            d.extend(json.loads(line) for line in f)
        except:
            continue
    
    for tweet in d:
        new_dict={'id': tweet['id'], 'timestamp_utc': '', 'local_time': tweet['date'], 'user_screen_name': tweet['user']['username'], 'text': tweet['content'], 
        'possibly_sensitive': 0, 'retweet_count': tweet['retweetCount'], 'like_count': tweet['likeCount'], 'reply_count': tweet['replyCount'], 
        'lang': 'en', 'to_username': '', 'to_userid': '', 'to_tweetid': '', 'source_name': '', 
        'source_url': '', 'user_location': '', 'lat': '', 'lng': '', 'user_id': tweet['user']['id'], 
         'user_name': tweet['user']['displayname'], 'user_verified': tweet['user']['verified'], 'user_description': tweet['user']['description'], 'user_url': '',
         'user_image': '', 'user_tweets': 0, 'user_followers': tweet['user']['followersCount'], 'user_friends': tweet['user']['friendsCount'], 
                  'user_likes': tweet['user']['favouritesCount'], 'user_lists': tweet['user']['listedCount'], 'user_created_at': tweet['user']['created'],
            'user_timestamp_utc': '', 'collected_via': '', 'match_query': '', 
            'retweeted_id': '', 'retweeted_user': '', 'retweeted_user_id': '', 'retweeted_timestamp_utc': '',
         'quoted_id': '' if tweet['quotedTweet'] is None else tweet['quotedTweet']['id'], 'quoted_user': '' if tweet['quotedTweet'] is None else tweet['quotedTweet']['user']['username'], 'quoted_user_id': '' if tweet['quotedTweet'] is None else tweet['quotedTweet']['user']['id'], 'quoted_timestamp_utc': '',
         'collection_time': '', 'url': '' if tweet['quotedTweet'] is None else tweet['quotedTweet']['url'], 'place_country_code': '', 'place_name': '', 'place_type': '',
              'place_coordinates': '', 'links': '', 'domains': '', 'media_urls': '', 'media_files': '', 
              'media_types': '', 'mentioned_names': '', 'mentioned_ids': '', 'hashtags': ''}
        final_list.append(new_dict)
        final_list.append(ref_dict)


final_csv = pd.DataFrame(final_list)
final_csv.to_csv("profs_for_graph.csv")

phd_int_list = []
for i in tqdm(range(480)):
    d = []
    with open(f"newphd_data{i}.json", 'r') as f:
        try:
            d.extend(json.loads(line) for line in f)
        except:
            continue

    for tweet in d:
        new_dict = {'id': tweet['id'], 'timestamp_utc': '', 'local_time': tweet['date'], 'user_screen_name': tweet['user']['username'], 'text': tweet['content'],
                    'possibly_sensitive': 0, 'retweet_count': tweet['retweetCount'], 'like_count': tweet['likeCount'], 'reply_count': tweet['replyCount'],
                    'lang': 'en', 'to_username': '', 'to_userid': '', 'to_tweetid': '', 'source_name': '',
                    'source_url': '', 'user_location': '', 'lat': '', 'lng': '', 'user_id': tweet['user']['id'],
                    'user_name': tweet['user']['displayname'], 'user_verified': tweet['user']['verified'], 'user_description': tweet['user']['description'], 'user_url': '',
                    'user_image': '', 'user_tweets': 0, 'user_followers': tweet['user']['followersCount'], 'user_friends': tweet['user']['friendsCount'],
                    'user_likes': tweet['user']['favouritesCount'], 'user_lists': tweet['user']['listedCount'], 'user_created_at': tweet['user']['created'],
                    'user_timestamp_utc': '', 'collected_via': '', 'match_query': '',
                    'retweeted_id': '', 'retweeted_user': '', 'retweeted_user_id': '', 'retweeted_timestamp_utc': '',
                    'quoted_id': '' if tweet['quotedTweet'] is None else tweet['quotedTweet']['id'], 'quoted_user': '' if tweet['quotedTweet'] is None else tweet['quotedTweet']['user']['username'], 'quoted_user_id': '' if tweet['quotedTweet'] is None else tweet['quotedTweet']['user']['id'], 'quoted_timestamp_utc': '',
                    'collection_time': '', 'url': '' if tweet['quotedTweet'] is None else tweet['quotedTweet']['url'], 'place_country_code': '', 'place_name': '', 'place_type': '',
                    'place_coordinates': '', 'links': '', 'domains': '', 'media_urls': '', 'media_files': '',
                    'media_types': '', 'mentioned_names': '', 'mentioned_ids': '', 'hashtags': ''}
        phd_int_list.append(new_dict)
        phd_int_list.append(ref_dict)
        final_list.append(new_dict)
        final_list.append(ref_dict)

phd_csv = pd.DataFrame(phd_int_list)
phd_csv.to_csv("phds_for_graph.csv")

final_csv = pd.DataFrame(final_list)
final_csv.to_csv("final_graph.csv")
