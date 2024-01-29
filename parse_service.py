import requests
from bs4 import BeautifulSoup as bs

titles_lst = []
info_lst = []


def get_info(url, search_title, day):
    src = requests.get(url).text
    soup = bs(src, "html.parser")
    for div in soup.find_all("div", class_="viewnews"):
        title = div.h1.text
        if day:
            if div.h2.text == "Где посмотреть сегодня":
                for table in div.find_all("table", class_="showfilm"):
                    if table.a and title[:10].lower() == search_title[:10].lower():
                        nobr_lst = table.find_all("nobr")
                        info_lst.append([table.tr.td.text, table.a.text, nobr_lst[0].text, nobr_lst[1].text])
        else:
            print(div)
            if div.h2.text == "Где посмотреть завтра":
                for table in div.find_all("table", class_="showfilm"):
                    if table.a and title[:10].lower() == search_title[:10].lower():
                        nobr_lst = table.find_all("nobr")
                        info_lst.append([table.tr.td.text, table.a.text, nobr_lst[0].text, nobr_lst[1].text])


def get_title_date(url):
    src = requests.get(url).text
    soup = bs(src, "html.parser")
    for div in soup.find_all("div", class_="viewnews"):
        title = div.h1.text
        if title.lower() != "текст" and title not in titles_lst:
            titles_lst.append(title)


def get_all_titles(url):
    src = requests.get(url).text
    soup = bs(src, "html.parser")
    for tr in soup.find_all('tr', class_="even"):
        get_title_date("https:" + tr.a["href"])
    print("Success!")
    return titles_lst


def get_all_info(url, search_title, day):
    src = requests.get(url).text
    soup = bs(src, "html.parser")
    for tr in soup.find_all('tr', class_="even"):
        get_info("https:" + tr.a["href"], search_title, day)
    print("Success!")
    return info_lst

