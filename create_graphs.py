import json
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

###############################################################
# with open('h-index-sco.json', 'r') as fout:
#     data = json.load(fout)
# df_list = [{'hindex': "1-20", 'count_of_profs': 0},
#            {'hindex': "21-40", 'count_of_profs': 0},
#            {'hindex': "41-60", 'count_of_profs': 0},
#            {'hindex': "61-80", 'count_of_profs': 0},
#            {'hindex': "81-100", 'count_of_profs': 0},
#            {'hindex': "101-120", 'count_of_profs': 0},
#            {'hindex': ">120", 'count_of_profs': 0}]
# data_dict = {}
# for d in data:
#     if int(data[d])>=1 and int(data[d])<=20:
#         df_list[0]['count_of_profs']+=1
#     elif int(data[d])>=21 and int(data[d])<=40:
#         df_list[1]['count_of_profs']+=1
#     elif int(data[d])>=41 and int(data[d])<=60:
#         df_list[2]['count_of_profs']+=1
#     elif int(data[d])>=61 and int(data[d])<=80:
#         df_list[3]['count_of_profs']+=1
#     elif int(data[d])>=81 and int(data[d])<=100:
#         df_list[4]['count_of_profs']+=1
#     elif int(data[d])>=101 and int(data[d])<=120:
#         df_list[5]['count_of_profs']+=1
#     elif int(data[d])>120:
#         df_list[6]['count_of_profs']+=1


# pdata=pd.DataFrame(df_list)
# print(pdata)
# plt.figure(figsize=(16, 9))  # figure size with ratio 16:9
# #sns.set(style='darkgrid',)
# plt.style.use('ggplot')
# sns.barplot(x="hindex", y="count_of_profs", data=pdata)
# plt.xlabel("h-index range")
# plt.title('Professors who actively tweet')
# plt.ylabel("No. of professors")
# #pdata=pdata.sort_values('count_of_profs')
# plt.show()
#####################################################################################
# t_dict={}
# #for i in range(1,5):
# with open(f'phdarxiv.json', 'r') as fout:
#     data = json.load(fout)
#     for d in data:
#         if len(data[d])!=0:
#             for e in data[d]:
#                 if e in t_dict:
#                     t_dict[e]+=1
#                 else:
#                     t_dict[e]=1
# print(t_dict)
# print(sorted(t_dict, key=t_dict.get))

# categ_list={'Machine Learning':370,'Artificial Intelligence':153,'Computer Vision':112,
# 'Computation & Language':111,'Computation & Society':59, 'Neural & Evolutionary Computing':43,'Human Computer Interaction':36}
categ_list={'Machine Learning':288,'Artificial Intelligence':79,'Computer Vision':83,
'Computation & Language':51,'Computation & Society':22, 'Neural & Evolutionary Computing':39,'Human Computer Interaction':9}
plt.figure(figsize=(16, 9))  # figure size with ratio 16:9
# sns.set(style='darkgrid',)
plt.style.use('ggplot')
sns.barplot(x=['Machine Learning', 'Computer Vision', 'Artificial Intelligence', 'Comp./Language',
               'Neural Computing', 'Comp./Society', 'HCI'],
            y=[288,83,79,51,39,22,9])
plt.xlabel("Machine Learning Domain")
plt.ylabel("No. of Arxiv papers posted")
plt.title('Arxiv papers posted by Phd students')
plt.show()
#######################################################################################################
# h_list = [{'hindex': "1-20", 'ML': 0, 'AI': 0, 'CV': 0, 'CL': 0, 'CY': 0, 'NE': 0, 'HC': 0},
#           {'hindex': "21-40", 'ML': 0, 'AI': 0, 'CV': 0,
#               'CL': 0, 'CY': 0, 'NE': 0, 'HC': 0},
#           {'hindex': "41-60", 'ML': 0, 'AI': 0, 'CV': 0,
#               'CL': 0, 'CY': 0, 'NE': 0, 'HC': 0},
#           {'hindex': "61-80", 'ML': 0, 'AI': 0, 'CV': 0,
#               'CL': 0, 'CY': 0, 'NE': 0, 'HC': 0},
#           {'hindex': "81-100", 'ML': 0, 'AI': 0, 'CV': 0,
#               'CL': 0, 'CY': 0, 'NE': 0, 'HC': 0},
#           {'hindex': "101-120", 'ML': 0, 'AI': 0, 'CV': 0,
#               'CL': 0, 'CY': 0, 'NE': 0, 'HC': 0},
#           {'hindex': ">120", 'ML': 0, 'AI': 0, 'CV': 0,
#               'CL': 0, 'CY': 0, 'NE': 0, 'HC': 0}]
# with open('h-index-sco.json', 'r') as fout:
#     hindex = json.load(fout)
# for i in range(1, 5):
#     with open(f'phd{i}.json', 'r') as fout:
#         data = json.load(fout)
#         for d in data:
#             if len(data[d]) != 0 and d in hindex:
#                 for e in data[d]:
#                     if e in ['cs.LG', 'stat.ML']:
#                         if int(hindex[d]) >= 1 and int(hindex[d]) <= 20:
#                             h_list[0]['ML'] += 1
#                         elif int(hindex[d]) >= 21 and int(hindex[d]) <= 40:
#                             h_list[1]['ML'] += 1
#                         elif int(hindex[d]) >= 41 and int(hindex[d]) <= 60:
#                             h_list[2]['ML'] += 1
#                         elif int(hindex[d]) >= 61 and int(hindex[d]) <= 80:
#                             h_list[3]['ML'] += 1
#                         elif int(hindex[d]) >= 81 and int(hindex[d]) <= 100:
#                             h_list[4]['ML'] += 1
#                         elif int(hindex[d]) >= 101 and int(hindex[d]) <= 120:
#                             h_list[5]['ML'] += 1
#                         elif int(hindex[d]) > 120:
#                             h_list[6]['ML'] += 1
#                     elif e == 'cs.AI':
#                         if int(hindex[d]) >= 1 and int(hindex[d]) <= 20:
#                             h_list[0]['AI'] += 1
#                         elif int(hindex[d]) >= 21 and int(hindex[d]) <= 40:
#                             h_list[1]['AI'] += 1
#                         elif int(hindex[d]) >= 41 and int(hindex[d]) <= 60:
#                             h_list[2]['AI'] += 1
#                         elif int(hindex[d]) >= 61 and int(hindex[d]) <= 80:
#                             h_list[3]['AI'] += 1
#                         elif int(hindex[d]) >= 81 and int(hindex[d]) <= 100:
#                             h_list[4]['AI'] += 1
#                         elif int(hindex[d]) >= 101 and int(hindex[d]) <= 120:
#                             h_list[5]['AI'] += 1
#                         elif int(hindex[d]) > 120:
#                             h_list[6]['AI'] += 1
#                     elif e == 'cs.CV':
#                         if int(hindex[d]) >= 1 and int(hindex[d]) <= 20:
#                             h_list[0]['CV'] += 1
#                         elif int(hindex[d]) >= 21 and int(hindex[d]) <= 40:
#                             h_list[1]['CV'] += 1
#                         elif int(hindex[d]) >= 41 and int(hindex[d]) <= 60:
#                             h_list[2]['CV'] += 1
#                         elif int(hindex[d]) >= 61 and int(hindex[d]) <= 80:
#                             h_list[3]['CV'] += 1
#                         elif int(hindex[d]) >= 81 and int(hindex[d]) <= 100:
#                             h_list[4]['CV'] += 1
#                         elif int(hindex[d]) >= 101 and int(hindex[d]) <= 120:
#                             h_list[5]['CV'] += 1
#                         elif int(hindex[d]) > 120:
#                             h_list[6]['CV'] += 1
#                     elif e == 'cs.CL':
#                         if int(hindex[d]) >= 1 and int(hindex[d]) <= 20:
#                             h_list[0]['CL'] += 1
#                         elif int(hindex[d]) >= 21 and int(hindex[d]) <= 40:
#                             h_list[1]['CL'] += 1
#                         elif int(hindex[d]) >= 41 and int(hindex[d]) <= 60:
#                             h_list[2]['CL'] += 1
#                         elif int(hindex[d]) >= 61 and int(hindex[d]) <= 80:
#                             h_list[3]['CL'] += 1
#                         elif int(hindex[d]) >= 81 and int(hindex[d]) <= 100:
#                             h_list[4]['CL'] += 1
#                         elif int(hindex[d]) >= 101 and int(hindex[d]) <= 120:
#                             h_list[5]['CL'] += 1
#                         elif int(hindex[d]) > 120:
#                             h_list[6]['CL'] += 1
#                     elif e == 'cs.NE':
#                         if int(hindex[d]) >= 1 and int(hindex[d]) <= 20:
#                             h_list[0]['NE'] += 1
#                         elif int(hindex[d]) >= 21 and int(hindex[d]) <= 40:
#                             h_list[1]['NE'] += 1
#                         elif int(hindex[d]) >= 41 and int(hindex[d]) <= 60:
#                             h_list[2]['NE'] += 1
#                         elif int(hindex[d]) >= 61 and int(hindex[d]) <= 80:
#                             h_list[3]['NE'] += 1
#                         elif int(hindex[d]) >= 81 and int(hindex[d]) <= 100:
#                             h_list[4]['NE'] += 1
#                         elif int(hindex[d]) >= 101 and int(hindex[d]) <= 120:
#                             h_list[5]['NE'] += 1
#                         elif int(hindex[d]) > 120:
#                             h_list[6]['NE'] += 1
#                     elif e == 'cs.CY':
#                         if int(hindex[d]) >= 1 and int(hindex[d]) <= 20:
#                             h_list[0]['CY'] += 1
#                         elif int(hindex[d]) >= 21 and int(hindex[d]) <= 40:
#                             h_list[1]['CY'] += 1
#                         elif int(hindex[d]) >= 41 and int(hindex[d]) <= 60:
#                             h_list[2]['CY'] += 1
#                         elif int(hindex[d]) >= 61 and int(hindex[d]) <= 80:
#                             h_list[3]['CY'] += 1
#                         elif int(hindex[d]) >= 81 and int(hindex[d]) <= 100:
#                             h_list[4]['CY'] += 1
#                         elif int(hindex[d]) >= 101 and int(hindex[d]) <= 120:
#                             h_list[5]['CY'] += 1
#                         elif int(hindex[d]) > 120:
#                             h_list[6]['CY'] += 1
#                     elif e == 'cs.HC':
#                         if int(hindex[d]) >= 1 and int(hindex[d]) <= 20:
#                             h_list[0]['HC'] += 1
#                         elif int(hindex[d]) >= 21 and int(hindex[d]) <= 40:
#                             h_list[1]['HC'] += 1
#                         elif int(hindex[d]) >= 41 and int(hindex[d]) <= 60:
#                             h_list[2]['HC'] += 1
#                         elif int(hindex[d]) >= 61 and int(hindex[d]) <= 80:
#                             h_list[3]['HC'] += 1
#                         elif int(hindex[d]) >= 81 and int(hindex[d]) <= 100:
#                             h_list[4]['HC'] += 1
#                         elif int(hindex[d]) >= 101 and int(hindex[d]) <= 120:
#                             h_list[5]['HC'] += 1
#                         elif int(hindex[d]) > 120:
#                             h_list[6]['HC'] += 1

# pdata = pd.DataFrame(h_list)
# # pdata=pdata.drop('hindex',axis=1)
# plt.figure(figsize=(16, 9))  # figure size with ratio 16:9
# # sns.set(style='darkgrid',)
# plt.style.use('ggplot')
# # sns.lineplot(data=pdata,dashes=False)
# plt.plot(pdata['hindex'], pdata['ML'], label='Machine Learning')
# plt.plot(pdata['hindex'], pdata['AI'], label='Artificial Intelligence')
# plt.plot(pdata['hindex'], pdata['CV'], label='Computer Vision')
# plt.plot(pdata['hindex'], pdata['CL'], label='Comp./Language')
# plt.plot(pdata['hindex'], pdata['CY'],label='Comp./Society')
# plt.plot(pdata['hindex'], pdata['NE'],label='Neural Computing')
# plt.plot(pdata['hindex'], pdata['HC'], label='HCI')



# plt.xlabel("h-index range")
# plt.ylabel("No. of Arxiv papers posted")
# plt.title("Arxiv papers posted by professors")
# plt.legend()
# plt.show()

#############################################################################################
# g=[]
# for j in range(2018,2023):
#     print(f'----{j}-----')
#     t_dict = {}
#     for i in range(1,5):
#         with open(f'phd{i}_{j}.json', 'r') as fout:
#             data = json.load(fout)
#             for d in data:
#                 if len(data[d])!=0:
#                     for e in data[d]:
#                         if e in t_dict:
#                             t_dict[e]+=1
#                         else:
#                             t_dict[e]=1
#     g.append({'year':j,'count':t_dict['cs.LG'],'categ':'ML'})
#     g.append({'year':j,'count':t_dict['stat.ML'],'categ':'ML'})
#     g.append({'year':j,'count':t_dict['cs.AI'],'categ':'AI'})
#     g.append({'year':j,'count':t_dict['cs.CL'],'categ':'CL'})
#     g.append({'year':j,'count':t_dict['cs.CV'],'categ':'CV'})
#     g.append({'year':j,'count':t_dict['cs.CY'],'categ':'CY'})
#     g.append({'year': j, 'count': t_dict['cs.HC'], 'categ': 'HC'})
#     g.append({'year': j, 'count': t_dict['cs.NE'], 'categ': 'NE'})

# df=pd.DataFrame(g)
# #plt.figure(figsize=(16, 9))  # figure size with ratio 16:9
# #plt.style.use('ggplot')
# sns.set(style='darkgrid',)
# #sns.color_palette('rocket', as_cmap=True)
# sns.catplot(
#     data=df, kind="bar",
#     x="year", y="count", hue="categ",
#     ci="sd",palette='rocket', alpha=.6, height=6, aspect=16/9
# )

# plt.xlabel("Year")
# plt.ylabel("No. of Arxiv papers posted in each category")
# #plt.title("Arxiv papers posted by category")
# plt.show()
# # #h.legend.set_title("")
