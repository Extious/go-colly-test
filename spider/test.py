from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time
import math
import base64
import requests
import json


user = "admin"
password = "Complexpass#123"
bas64encoded_creds = base64.b64encode(bytes(user + ":" + password, "utf-8")).decode("utf-8")

# 创建一个Service对象
service = Service(ChromeDriverManager().install())
#配置参数
opt = Options()
opt.add_experimental_option('useAutomationExtension', False)
opt.add_experimental_option('excludeSwitches', ['enable-automation'])
opt.add_argument("--disable-blink-features=AutomationControlled")
driver = Chrome(service=service, options=opt)
# 即可解决问题
driver.get("https://www.chictr.org.cn/searchproj.html")
driver.implicitly_wait(3)
hrefs = []
my_dic = {}
try:
    slider = driver.find_element(By.ID,"nc_1__bg")
    # 创建操作链
    action_chains = ActionChains(driver)
    # 将鼠标移动到滑块上
    action_chains.move_to_element(slider)
    # 模拟按下鼠标左键并保持不松开
    action_chains.click_and_hold()
    # 移动鼠标使滑块达到目标位置
    action_chains.move_by_offset(300, 0)
    # 松开鼠标左键
    action_chains.release()
    # 执行操作链
    action_chains.perform()
    time.sleep(2)
except NoSuchElementException:
    print("no check")

topic = driver.find_element(By.ID,"topic")
topic.send_keys("卵巢癌")
button = driver.find_element(By.ID,"handle-search")
button.click()
total = driver.find_element(By.ID,"data-total").text
float, page = math.modf(int(total)/10)  
if float > 0:
    page=page+1
print(page)
for i in range(int(page)):
    links = driver.find_elements(By.PARTIAL_LINK_TEXT,"卵巢癌")
    for element in links:
        print("page:"+str(i+1))
        print("题目："+element.text)
        print("链接："+element.get_attribute("href"))
        my_dic[element.get_attribute("href")]=element.text
        hrefs.append(element.get_attribute("href"))
    button = driver.find_element(By.XPATH,'//*[@id="pagination"]/ul/li[13]')
    button.click()
time.sleep(5)

for href in hrefs:
    driver.get(href)
    driver.implicitly_wait(3)
    try:
        slider = driver.find_element(By.ID,"nc_1__bg")
        # 创建操作链
        action_chains = ActionChains(driver)
        # 将鼠标移动到滑块上
        action_chains.move_to_element(slider)
        # 模拟按下鼠标左键并保持不松开
        action_chains.click_and_hold()
        # 移动鼠标使滑块达到目标位置
        action_chains.move_by_offset(300, 0)
        # 松开鼠标左键
        action_chains.release()
        # 执行操作链
        action_chains.perform()
        time.sleep(2)
    except NoSuchElementException:
        print("no check")
    data = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[6]/table[1]/tbody/tr[22]/td[2]/p')
    print("纳入标准："+data.text)
    params = {
        "index": "test",
        "records":[
            {
                "link": href,
                "title":my_dic[href],
                "standard": data.text
            }
        ]
    }
    # headers = {"Content-type": "application/json",  "Authorization": "Basic " + bas64encoded_creds}
    # zinc_url= "http://localhost:4080/api/_bulkv2"
    # res = requests.post(zinc_url, headers=headers, data=json.dumps(params))
    # print(res.text)