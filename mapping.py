import folium
import webbrowser
from bs4 import BeautifulSoup as bs
import requests
place=input("Enter the Location : ")
url="https://google.com/search?query="+place+"+latitude+longitute"
#print(url)
headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0"}

response=requests.get(url,headers=headers)
soup=bs(response.text,"html.parser")
loc=soup.find("div",class_="Z0LcW XcVN5d")
print(loc.text)


lat=loc.text
lat=lat.split(",")
lat1=lat[0]
lat1=lat1.replace("° N","")
print(lat1)
lat2=lat[1]
lat2=lat2.replace("° E","")
print(lat2)

m=folium.Map(location=[lat1,lat2],zoom_start=14)
m1=input("Enter the File Name : ")
m2=m1+".html"
a=m.save(m2)
webbrowser.open(m2)
