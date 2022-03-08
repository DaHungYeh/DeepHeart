import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import requests
from bs4 import BeautifulSoup

url = f'http://192.168.156.225:5000/TextCloud/Sample_Collection'
response = requests.get(url)
all_text = BeautifulSoup(response.text, 'html.parser')
# print(all_text)
cut_word = " ".join(jieba.cut(all_text))
stopwords = set()
content = [line.strip() for line in open('/Users/koumizubun/Desktop/stop_words.txt', 'r').readlines()]
stopwords.update(content)

# get the word cloud (scale = 5,數值越大越清晰)
word_cloud = WordCloud(
    scale=5,
    background_color='white',
    stopwords=content,
    # mask=mask_image,
    font_path='/Users/koumizubun/Desktop/desktop/Document/Python/test/TaipeiSansTCBeta-Regular.ttf',
    max_words=200,
    width=1000,
    height=1000)

word_cloud.generate(cut_word)
plt.imshow(word_cloud, interpolation='bilinear')
plt.axis("off")
plt.show()