from selenium import webdriver
import time
driver = webdriver.Firefox()
url=""
a=driver.get(url)
time.sleep(5)
while True:
  lastlapfull=driver.find_element("xpath",'//*[@id="tableTiempos"]/tbody/tr[1]').text.split(")")[1].strip().replace(' META','').replace(' ',';')
  lastlap=lastlapfull.split(";")[0]
  lap=open("database.csv","r").readlines()[-1].split(";")[0]
  if lastlap > lap:
    f = open("database.csv","a")
    f.write(lastlapfull+"\n")
    f.close()
  time.sleep(3)
