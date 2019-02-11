import  requests
from bs4 import BeautifulSoup
import operator

def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "html.parser")

    for post_text in soup.findAll('a', {'class': 'title text-semibold'}):
        content = post_text.string       # Get only the text
        words = content.lower().split()  # covert all words to lowercase. split() returns a list of the woords seperated by whitespaces

        for each_word in words:
            word_list.append(each_word)
    clean_up_list(word_list)


def clean_up_list(mylist):
    clean_list = []
    for word in mylist:
        symbols = "0123456789!\"£$%^&*(){}_-:@~<>?[];'#,./'"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            #print(word)
            clean_list.append(word)
    create_dictionary(clean_list)


def create_dictionary(clean_list):
    word_count = {}

    # The word is the key each time you find a word that is not in the dictinary.
    for word in clean_list:
        if word in word_count:
            word_count[word] += 1   # using the word as the key, increments the value stored
        else:
            word_count[word] = 1    # stores the value one with the wword as its key
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):       # 1 is sort by value. O is sort by key
        print(key, value)





start('https://thenewboston.com/forum/category.php?id=15')


