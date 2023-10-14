"""
File: webcrawler.py
Name: Sunny
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male number: 10895302
Female number: 7942376
---------------------------
2000s
Male number: 12976700
Female number: 9208284
---------------------------
1990s
Male number: 14145953
Female number: 10644323
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")

        # ----- Write your code below this line ----- #

        tags = soup.find_all('table', {'class': 't-stripe'})
        male_total = 0
        female_total = 0

        # Method1
        for tag in tags:
            text = tag.tbody.text.split()
            for i in range(len(text)):
                if i < 1000: # Filter the redundant info
                    if i % 5 == 2: # Boy
                        male_total += int(text[i].replace(',', ''))
                    if i % 5 == 4: # Girl
                        female_total += int(text[i].replace(',', ''))

        # Method2

        # table_body = soup.find('tbody')
        # rows = table_body.find_all('tr')
        # # print(table_body)
        # # print(rows)
        # data = []
        # for row in rows:
        #     cols = row.find_all('td')
        #     lists_cols = []
        #     for ele in cols:
        #         lists_cols.append(ele.text.strip())
        #     data.append(lists_cols)
        #     # print(data)
        #
        # list_male_num = []
        # list_female_num = []
        # for a in data:
        #     if len(a) > 2:
        #         list_male_num.append(a[2])
        #         list_female_num.append(a[4])
        #
        # for item in list_male_num:
        #     i = list_male_num.index(item)
        #     male_total = male_total + int(list_male_num[i].replace(',', ""))
        #     female_total = female_total + int(list_female_num[i].replace(',', ""))
        print('Male Number: ' + str(male_total))
        print('Female Number: ' + str(female_total))


if __name__ == '__main__':
    main()
