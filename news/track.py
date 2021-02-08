
articles = []

def not_sent(article): 
    if article in articles: 
        return False 
    else: 
        articles.append(article)
    return True