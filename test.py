'''
    功能，素材爬虫提取
'''
import requests
from bs4 import BeautifulSoup


# 《易经·序卦传》64卦卦象 1阳 0阴
gua = ['111111','000000','100010','010001','111010','010111','010000','000010','111011','110111','111000','000111','101111','111101','001000','000100','100110','011001','110000','000011','100101','101001','000011','100000','100111','111001','100001','011110','010010','101101','001110','011100','001111','111100','000101','101000','101011','110101','001010','010100','110001','100011','111110','011111','000110','011000','010110','011010','101110','011101','100100','001001','001011','110100','101100','001101','011011','110110','010011','110010','110011','001100','101010','010101']

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def get_name_ci():# 获取卦名卦辞
    url = "https://zhuanlan.zhihu.com/p/377091070"
    response = requests.get(url, headers=headers)
    html_content = response.text

    soup = BeautifulSoup(html_content, "lxml")
    paragraphs = []
    for h2 in soup.find_all("h2"):
        next_p = h2.find_next("p")
        if next_p:
            paragraphs.append(str(next_p.text.split()[0]))
    with open(file='test.txt',mode='a',encoding='utf-8') as test:
        test.write("\n".join(paragraphs))
    print("\n".join(paragraphs))


def get_ci_explanation():#获取卦辞白话文解释
    url = 'https://yijing.5000yan.com/64gua/'
    response = requests.get(url, headers=headers)
    html_content = response.content

    # parse the html content using beautiful soup
    soup = BeautifulSoup(html_content, 'lxml')

    links = [a['href'] for a in soup.find('main', class_='main-content container').find_all('a')]

    results = []
    for l in links:
        url = f'{l}'
        response = requests.get(url, headers=headers)
        html_content = response.content
        # parse the html content using beautiful soup
        soup = BeautifulSoup(html_content, 'lxml')
        section=soup.find('section',class_='section-body').find_all('p')
        results.append(section[0].text.split()[0] + section[1].text.split()[0])
    with open(file='test.txt',mode='a',encoding='utf-8') as test:
        test.write("\n".join(results))
    print("\n".join(results))

# 定义主函数
def main():
    get_name_ci()# 获取卦名卦辞
    get_ci_explanation()#获取卦辞白话文解释

# 执行
if __name__ == '__main__':
    main()
