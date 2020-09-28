import folium
import webbrowser
from bs4 import BeautifulSoup as bs
import requests

place=input("Enter the place you Want to search : ")

url="https://google.com/search?query="+place+"+latitude+longitude"

headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0"}

response=requests.get(url,headers=headers)

soup=bs(response.text,"html.parser")

locationFind=soup.find("div",class_="Z0LcW XcVN5d")

locationSpilit=locationFind.text

locationSpilit=locationSpilit.split(",")

latitute=locationSpilit[0]

latitute=latitute.replace("° N","")

longitude=locationSpilit[1]

longitude=longitude.replace("° E","")

mapFind=folium.Map(location=[latitute,longitude],zoom_start=14)

mapName=place+".html"

a=mapFind.save(mapName)

webbrowser.open(mapName)
