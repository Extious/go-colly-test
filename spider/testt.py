
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
import time

import base64


# 创建一个Service对象
service = Service(ChromeDriverManager().install())
#配置参数
opt = Options()
# opt.add_experimental_option('useAutomationExtension', False)
# opt.add_experimental_option('excludeSwitches', ['enable-automation'])
# opt.add_argument("--disable-blink-features=AutomationControlled")
driver = Chrome(service=service, options=opt)
# 即可解决问题
i=0
while i <10:
    driver.get("https://www.chictr.org.cn/searchproj.html")
    i=i+1
    time.sleep(2)