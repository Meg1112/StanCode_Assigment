"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
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
        soup = BeautifulSoup(html)

        tags = soup.find_all('tbody')
        total_b = 0
        total_g = 0
        for tag in tags:
            text = tag.text
            text = text.split()
            # Get all male and female number in list
            d = []
            for i in range(len(text)):
                token = text[i]
                if ',' in token:
                    num = token.replace(',', '')  # get clean number
                    d.append(num)
            # Count male and female total number
            for j in range(len(d)):
                if (j % 2) == 0:
                    total_b += int(d[j])
                else:
                    total_g += int(d[j])
        print("Male Number: "+str(total_b))
        print("Female Number: " + str(total_g))


if __name__ == '__main__':
    main()
