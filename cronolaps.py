from selenium import webdriver
import datetime
import time
import sys
import os


track=sys.argv[1]
now = datetime.datetime.now()
datetoday=now.strftime("%Y%m%d")

database=sys.argv[2]+datetoday+".csv"
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
  lastlapfull=driver.find_element("xpath",'//*[@id="tableTiempos"]/tbody/tr[1]').text.split(")")[1].strip().replace(' META','').replace(' ',';')
  lastlap=lastlapfull.split(";")[0]
  lap=open(database,"r").readlines()[-1].split(";")[0]
  if lastlap > lap:
    f = open(database,"a")
    f.write(lastlapfull+"\n")
    f.close()
  time.sleep(3)
