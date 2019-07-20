import requests
from selenium import webdriver
import datetime

driver = webdriver.Chrome()
driver.implicitly_wait(0.5)
print('start process')

driver.get('https://passport.jd.com/uc/login')

while True:
    try:
        driver.find_element_by_partial_link_text('迪兰sp')#查找自己的名字？
        print('已登录')
        driver.get('https://item.jd.com/27312039878.html')
        buy_time = '2019-06-16 22:35:50'
        print('buytime:{}等待时间到达'.format(buy_time))
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        while True:
            if now == buy_time:
                driver.find_element_by_xpath('//*[@id="choose-attr-2"]/div[2]/div[1]/a').click()#选中的物品
                driver.find_element_by_xpath('//*[@id="choose-baitiao"]/div[2]/div[1]/div[1]/a/strong').click()
                driver.find_element_by_xpath('//*[@id="btn-onkeybuy"]').click()
                print('————————————————已提交订单——————————————————')
                break
            else:
                print(now)
        break
    except:
        print('等待登陆。。。')