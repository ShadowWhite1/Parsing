import requests
from fake_headers import Headers
from bs4 import BeautifulSoup
import json
from pprint import pprint 

HOST = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'
headers = Headers(browser = 'chrome', os = 'mac').generate()

hh_ru = requests.get(HOST, headers=headers).text
soup = BeautifulSoup(hh_ru, features = 'lxml')
vacancies = soup.find('div', id = "a11y-main-content")

def Head_Hunter():
    vacancies_list = []
    for article in vacancies:
        article1 = article.find('div', class_ = 'g-user-content')
        if article1 != None:
            x = article1.text
            if "Django" in x or 'django' in x or 'Flask' in x or 'flask' in x:
                article2 = article.find('div', class_ = 'vacancy-serp-item-body__main-info')
                if article2 != None:
                    info = article2.find('a', class_ = 'serp-item__title')
                    name = info.text
                    link = info.get("href")
                article3 = article.find('span', class_ = 'bloko-header-section-3')
                if article3 != None:
                    salary = ((article3.text).replace('\u202f', ''))
                article4 = article.find('a', class_ = 'bloko-link bloko-link_kind-tertiary')
                if article4 != None:
                    company = ((article4.text).replace('\xa0', ' '))
                article5 = article.find('div', class_ = 'vacancy-serp-item__info')
                if article5 != None:
                    place = (article5.text).replace((article4.text),'').replace('\xa0', ' ')
                   
                vacancies_list.append({
                    "Название": name,
                    "Компания": company,
                    "Зарплата": salary,
                    "Местоположение": place,
                    "Ссылка": link
                })
                with open ('vacancies.json','w', encoding = 'utf=8') as f:
                    json.dump(vacancies_list, f, sort_keys = False, ensure_ascii = False, indent = 2)
    if vacancies_list == []:
        return pprint('Нет информации по данной вакансии ¯\_(ツ)_/¯')
    else:
        return pprint('Готово!')

def Head_Hunter_Bucks():
    vacancies_bucks_list = []
    for article in vacancies:
        article1 = article.find('div', class_ = 'g-user-content')
        if article1 != None:
            x = article1.text
            if "Django" in x or 'django' in x or 'Flask' in x or 'flask' in x:
                article_salary = article.find('span', class_ = 'bloko-header-section-3')
                if article_salary != None:
                    salary = ((article_salary.text).replace('\u202f', ''))
                    if 'USD' in salary:
                        article2 = article.find('div', class_ = 'vacancy-serp-item-body__main-info')
                        if article2 != None:
                            main_info = article2.find('a', class_ = 'serp-item__title')
                            name = main_info.text
                            link = main_info.get("href")
                        article3 = article.find('a', class_ = 'bloko-link bloko-link_kind-tertiary')
                        if article3 != None:
                            company = ((article3.text).replace('\xa0', ' '))
                        article4 = article.find('div', class_ = 'vacancy-serp-item__info')
                        if article4 != None:
                            place = (article4.text).replace((article3.text),'').replace('\xa0', ' ')
                            
                        vacancies_bucks_list.append({
                            "Название": name,
                            "Компания": company,
                            "Зарплата": salary,
                            "Местоположение": place,
                            "Ссылка": link
                        })
                        with open ('vacancies_bucks.json','w', encoding = 'utf=8') as f:
                           json.dump(vacancies_bucks_list, f, sort_keys = False, ensure_ascii = False, indent = 2)
    if vacancies_bucks_list == []:
        return pprint('Нет информации по данной вакансии ¯\_(ツ)_/¯')
    else:
        return pprint('Готово!')

if __name__ == '__main__':
    Head_Hunter() 
    Head_Hunter_Bucks()