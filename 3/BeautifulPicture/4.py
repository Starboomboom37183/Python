import time
from selenium import webdriver


class Yunmusic(object):
    def __init__(self):
        self.base_url = "https://music.163.com/#/discover/playlist/"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver = driver

    def get_content_list(self):
        self.driver.switch_to.frame('contentFrame')
        li_list = self.driver.find_elements_by_xpath('//ul[@id="m-pl-container"]/li')
        content_list = []
        print(len(li_list), '列')
        for i in li_list:
            item = {}
            try:
                item['title'] = i.find_element_by_xpath('./p[@class="dec"]/a').get_attribute('title')
                item['song_url'] = i.find_element_by_xpath('./p[@class="dec"]/a').get_attribute('href')
                item['author'] = i.find_element_by_xpath('./p[2]/a').get_attribute('title')
                item['author_home_page'] = i.find_element_by_xpath('./p/a').get_attribute('href')
                item['click'] = i.find_element_by_xpath('./div/div/span[@class="nb"]').text
                print(item)
            except AttributeError:
                continue
            content_list.append(item)
            self.save_content(content_list)
        try:
            self.next_url = self.driver.find_element_by_xpath('//*[@id="m-pl-pager"]/div/a[contains(text(), "下一页")]')
        except Exception as e:
            print(e)
            return None
        print('next_page:', self.next_url.get_attribute('href'))
        return self.next_url.get_attribute('href')

    def save_content(self, content_list):
        with open('music.txt', 'a+') as f:
            for i in content_list:
                f.write(str(i) + '\n')

    def get_catrgory_url(self):
        self.driver.get(self.base_url)
        self.driver.switch_to.frame("contentFrame")
        category_el_list = self.driver.find_elements_by_xpath('//*[@id="cateListBox"]/div/dl/dd/a')
        category_url_list = []
        for category in category_el_list:
            url = category.get_attribute('href')
            category_url_list.append(url)
            print(url)
        return category_url_list

    def run(self):
        category_url_list = self.get_catrgory_url()
        for url in category_url_list:
            self.next_url = url
            while self.next_url:
                self.driver.get(self.next_url)
                self.next_url = self.get_content_list()
                time.sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    douyu = Yunmusic()
    douyu.run()
