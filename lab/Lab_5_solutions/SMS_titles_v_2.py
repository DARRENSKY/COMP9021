# Written by Eric Martin for COMP9021


'''
Extracts titles from a front page of the Sydney Morning Herald.
Solution with beautifulsoup.

Note that some nonASCII characters do not display properly
when the program is run from from Idle, but do display properly
when the program is run from the command line.
'''


import bs4


with open('SMH.txt') as file:
    SMH_page = bs4.BeautifulSoup(file, 'html.parser')
    for selection in SMH_page.select('h3 > a'):
        title = selection.get('title')
        if title:
            print(title.strip())

