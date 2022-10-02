from selenium import webdriver
import os
import time
from urllib.request import urlopen
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib.request

def crawling(arg):
    driver = webdriver.Chrome(executable_path='C:/Users/koust/PNU/chromedriver_win32/chromedriver.exe')
    driver.implicitly_wait(3)

    driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
    if not os.path.isdir("C:/Users/koust/PNU/sample/" + arg):
        os.makedirs("C:/Users/koust/PNU/sample/"+ arg)
    search = arg
    element = driver.find_element('name', 'q')
    element.send_keys(search)
    element.send_keys(Keys.RETURN)

    SCROLL_PAUSE_TIME = 1

    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            try:
                driver.find_element_by_css_selector(".mye4qd").click()
            except:
                break
        last_height = new_height

    images = driver.find_elements(By.CSS_SELECTOR,".rg_i.Q4LuWd")
    count = 1

    print("length of images: ", len(images))

    for image in images:
        try:
            image.click()
            time.sleep(1)
            imgUrl = driver.find_element(By.XPATH,'//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img').get_attribute('src')
            path = "C:\\Users\\koust\\PNU\\sample\\" + arg + "\\"
            urllib.request.urlretrieve(imgUrl, path + search + "_" + str(count) + ".jpg")
            print("Image saved: " + arg + "_{}.jpg".format(count))
            count += 1
        except:
            pass

    driver.close()



crawling("keyword")
