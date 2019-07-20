from selenium import webdriver
from selenium.webdriver.common.by import By   #按照什么方式查找，By.ID,By.CSS_SELECTOR
from selenium.webdriver.common.keys import Keys   #键盘按键操作
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait  #等待页面加载某些元素
import pyautogui       #鼠标操作
from bs4 import BeautifulSoup
import time
from PIL import ImageGrab     #截图操作
from PIL import Image
import aircv as ac     
 
#截取原图
def jieping():
    size = (0,0,1600,900)
    img = ImageGrab.grab(size)
    img.save('jianshu.jpg')
 
#匹配图片，获取坐标
def complice():
    imsrc = ac.imread(r'D:\Python\python_exmple\pachong05\jianshu.jpg')
    imobj = ac.imread(r'D:\Python\python_exmple\pachong05\jiantu.jpg')
    match_result = ac.find_template(imsrc, imobj, 0.5)
    try:
        return match_result['result']
    except TypeError:
        print("匹配失败！！！")
        return None
 
browser = webdriver.Chrome("D:\software（sth）\Google\Chrome\Application\chromedriver.exe")#初始化浏览器
browser.get('https://www.baidu.com')     #get()方法请求URL：百度
input = browser.find_element_by_id('kw')   #寻找‘kw’节点
input.send_keys('简书')        #输入关键字
input.send_keys(Keys.ENTER)    #按下回车键
wait = WebDriverWait(browser, 20)    #浏览器等待20ms
wait.until(EC.presence_of_element_located((By.ID,'content_left')))  #等到id为content_left的元素加载完毕,最多等20秒
pyautogui.moveTo(213,282,duration=0.25)    #移动鼠标
time.sleep(1)
pyautogui.doubleClick()   #双击鼠标右键
print("页面已打开！")
browser.maximize_window()  #浏览器窗口最大化
time.sleep(10)
jieping()     #截取原图
time.sleep(10)
distication = complice()     #获取坐标
print(distication)
time.sleep(1)
pyautogui.moveTo(distication[0],distication[1],duration=0.25)   #移动鼠标
time.sleep(3)
pyautogui.doubleClick()   #双击鼠标右键
time.sleep(99999)
