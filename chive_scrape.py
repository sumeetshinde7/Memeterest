from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


def get_chive_data():
    '''
    

    Returns
    -------
    meme_data : TYPE-dataframe
        DESCRIPTION.  returns dataframe containing memes from chive

    '''

    html = urlopen('https://thechive.com/')
    
    
    tc_table_list = []
    
    content = html.read()
    content = BeautifulSoup(content, 'html.parser')
    
    
    #print(content)
    
    tc_table_list = content.findAll('h1',attrs = {'class': 'post-title entry-title card-title'})
    

    topic_list = []
    
    for row in tc_table_list:
        topic_list.append(row.text.split("\n\n\t\t\t\t")[1].split("\t\t\t\n")[0])
        
    #print(len(topic_list))
    
    downvotes = []
    upvotes = []
    
    tc_vote_list = content.findAll('span',attrs = {'class': 'card-count icon-card-up upvotes-count'})
    for rows in tc_vote_list:
        upvotes.append(rows.text.split("\t\t\t\t")[1])
                       
        
    tc_vote_list2 = content.findAll('span',attrs = {'class': 'card-count icon-card-down downvotes-count'})
    for rows in tc_vote_list2:
        downvotes.append(rows.text.split("\t\t\t\t")[1])
    
    scores = [int(a) -int(b) for a,b in zip(upvotes,downvotes)]
    
    total_votes = [int(a) + int(b) for a,b in zip(upvotes,downvotes)]
    
    
    url = []
    url_list = content.findAll('a',attrs = {'class': 'card-img-link'})
    
    for rows in url_list:
        image = content.find('img')
        url.append(image['src'])
    
    
    meme_data = pd.DataFrame(
        {'title': topic_list,,
         'scores' : scores
         'url': url,
         'total_votes': total_votes,
         'upvotes': upvotes,
         'downvotes': downvotes
        })
    
    # pd.set_option('display.max_rows', None)
    # pd.set_option('display.max_columns', None)
    # pd.set_option('display.width', None)
    # pd.set_option('display.max_colwidth', -1)
    
    return meme_data
    


    