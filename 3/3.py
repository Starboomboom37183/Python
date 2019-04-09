
from selenium import webdriver
from bs4 import BeautifulSoup
import time
'''
def get_all_article(uid):
    tar_url = 'http://www.jianshu.com/u/' + uid
    browser.get(tar_url)
    html = browser.page_source
    print(html)
    bsObj = BeautifulSoup(html, "html.parser")
    note_list = bsObj.find("ul", {"class": "note-list"})
    article_list = note_list.find_all("li")
    all_article = []
    for i in article_list:
        href = i.find('a', {"class": "title"})['href']
        times = i.find('div', {"class": "meta"}).a.get_text().strip('\n').strip()
        all_article.append({'href': href, 'times': times})
    return all_article

browser = webdriver.Chrome()
browser.set_page_load_timeout(5)
uid = '55672ec82fcd'
all_article = get_all_article(uid=uid)
print(all_article)
for article in all_article:
    times = int(article['times'])
    if times < 10:
        for j in range(10-times):
            try:
                browser.get('http://www.jianshu.com'+article['href'])
                time.sleep(0.2)
            except Exception as e:
                continue
browser.quit()
'''
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
br = webdriver.Chrome(options=chrome_options)
br.set_page_load_timeout(5)
br.get('https://music.163.com/#/discover/playlist/')
br.switch_to.frame('contentFrame')
li_list = br.find_element_by_xpath('//ul[@id="m-pl-container"]/li')
print(li_list)

#print(html)
#bsobj = BeautifulSoup(html,"html.parser")
#note_list = bsobj.find("ul",{"class:m-cvrlst f-cb"})
#print(note_list)
