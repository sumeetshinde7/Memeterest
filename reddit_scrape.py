# -*- coding: utf-8 -*-
"""

@author: Sumeet Shinde (sshinde@andrew.cmu.edu)
"""

import pandas as pd
import praw


def get_reddit_data(limit=25, post_type='hot', subreddit=None):
    '''
    Parameters
    ----------
    limit : TYPE-int, optional
        DESCRIPTION. The default is 25.
    post_type : TYPE-str (can be 'hot' or 'top'), optional
        DESCRIPTION. The default is 'hot'.
    subreddits : TYPE-str default is None
        DESCRIPTION. string containing subreddit name to scrape

    Returns
    -------
    df : TYPE-dataframe
        DESCRIPTION - returns dataframe containing posts from reddit
                      Posts have limit on number and are either hot or top posts
    '''
    

    # authentication for reddit 
    #--- please use own authentication if this does not work or contact the author
    my_client_id = '*****' # enter ID
    my_client_secret = '*****' #enter Secret Key
    my_user_agent = 'dfp_meme' 
    
    reddit = praw.Reddit(client_id = my_client_id, 
                         client_secret = my_client_secret,
                         user_agent = my_user_agent)
    
    if subreddit is not None:
        if post_type == 'hot':
            all_posts = reddit.subreddit(subreddit).hot(limit=limit)
        elif post_type =='top':
            all_posts = reddit.subreddit(subreddit).top(limit=limit)
        
    posts = []
          
    for post in all_posts:
        # posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
        posts.append([post.title, post.score, post.url])
        
    df = pd.DataFrame(posts,columns=['title', 'score', 'url'],index=range(limit))

    return df
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    