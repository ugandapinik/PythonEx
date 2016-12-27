import requests
from bs4 import BeautifulSoup
import operator


def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "html.parser")

    for post_text in soup.findAll('p', {'class': 'edgtf-post-excerpt'}):
        content = post_text.string
        words = content.lower().split()

        for each_word in words:
            #store to wordlist
            word_list.append(each_word)
        
    
    cleanup_list(word_list)


def cleanup_list(word_list):
    clean_word_list = []
    for word in word_list:
        #clean the worlds
        #remove the symbols
        symbols = '!@#$%^&*()_+./[]\=-?<>":,'
        for i in range(0, len(symbols)):
            #replace symbol with empty string
            word = word.replace(symbols[i], "")
        
        # if word length is > 0
        if len(word) > 0:
            clean_word_list.append(word)
    
    create_dictionary(clean_word_list)


def create_dictionary(clean_word_list):
    #create a dictionary
    word_count = {}
    for word in clean_word_list:
        if(word in word_count):
            word_count[word] += 1

        else:
            word_count[word] = 1
    
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1), reverse=True):
        print(key, value)
        
            


start('http://www.jewel-mahmud.com/blogs/')