import jieba
from flask import Flask
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
content = [line.strip() for line in open('/Users/koumizubun/Desktop/stop_words.txt', 'r').readlines()]


@app.route('/TextCloud/<userId>', method='POST')
def textcloud(url):
    response = requests.get(url)
    all_text = BeautifulSoup(response.text, 'html.parser')

    cut_word = " ".join(jieba.cut(all_text))
    stopwords = set()
    stopwords.update(content)

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

    return plt.show()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

crawler('http://192.168.156.225:5000/TextCloud/Sample_Collection')


