from selenium import webdriver
import datetime
import time
import sys
import os


track=sys.argv[1]
now = datetime.datetime.now()
datetoday=now.strftime("%Y%m%d")
foundrider="0"

database=sys.argv[2]+datetoday+".csv"
rider=sys.argv[2]
url="http://www.cronolaps.es/tiempos"



if not os.path.isfile(database):
  f=open(database,'w')
  f.write("0\n")
  f.close()

driver = webdriver.Firefox()
a=driver.get(url)
time.sleep(2)

tracks=driver.find_element("xpath",'//*[@id="list-circuits"]').text.split("\n")
tracknl= [tracks.index(i) for i in tracks if track in i]
trackn=str(tracknl[0])
driver.find_element("xpath",'//*[@id="item'+trackn+'"]').click()
time.sleep(5)

while True:
  try:
    if foundrider=="0":
      riders=driver.find_element("xpath",'//*[@id="tableResultados"]').text.split("\n")
      ridernl= [riders.index(i) for i in riders if rider in i]
      ridern=str(ridernl[0])
      driver.find_element("xpath",'//*[@id="tableResultados"]/tbody/tr['+ridern+']/td[3]/a').click()
      time.sleep(2)
      foundrider="1"
    try:
      lastlapfull=driver.find_element("xpath",'//*[@id="tableTiempos"]/tbody/tr[1]').text.split(")")[1].strip().replace(' META','').replace(' ',';')
      lastlap=lastlapfull.split(";")[0]
      lap=open(database,"r").readlines()[-1].split(";")[0]
      if lastlap > lap:
        f = open(database,"a")
        f.write(lastlapfull+"\n")
        f.close()
    except:
      pass
  except:
    pass
  time.sleep(3)
