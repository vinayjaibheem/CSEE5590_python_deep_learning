from bs4 import BeautifulSoup
import urllib.request
import os

def parseTable():
    url = "https://www.fantasypros.com/nfl/reports/leaders/qb.php?year=2015"
    source_code = urllib.request.urlopen(url)
    plain_text = source_code
    soup = BeautifulSoup(plain_text, "html.parser")    #parsing the html page into plain text

    table = soup.find("table")   #find 'table' tag from the parsed html page
    table_headers = table.find_all('th')  #find table headers from the table
    th = [i.text for i in table_headers]  #iterate through the table headers and display in text format
    print(th)

    f = open("table.txt", "w")    #open table.txt file in write mode and write to file object
    f.write(str(th))   #write the table headers into the file
    table_rows = table.find_all("tr")   #find all the table rows in the table
    for tr in table_rows:   #for every row
        td = tr.find_all('td')   #find all table cell
        row = [i.text for i in td]   #for every table cell, display the row in text format
        f.write("\n")
        print(row)
        f.write(str(row)) #write the row in table.txt file

parseTable()