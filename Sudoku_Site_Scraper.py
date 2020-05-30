from Sudoku_Url import selected_url
from selenium import webdriver
from time import sleep
import re


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")   
chrome_options.add_argument('--ignore-certificate-errors') # This is to prevent the "Allow notification" dialog box which interferes with the code
chrome_options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(chrome_options=chrome_options)


def go_to_site():
    
    driver.get(selected_url())
    
    sleep(2)
    

def get_cord_list():

    list_of_cords = []

    for i in range(0,89):
        if len(str(i)) == 1:
            list_of_cords.append('f0'+ str(i))
        else:
            list_of_cords.append('f'+ str(i))

    return list_of_cords

def get_sudoku_board(cord_list):

    for cord in cord_list:

        found_cord = driver.find_element_by_xpath("//input[@id = \'"+ cord +"\']")
        
        if found_cord.get_attribute('@class') == 's0':
            print('filled')
        elif found_cord.get_attribute('@class') == 'd0':
            print('empty')


go_to_site()

# https://www.livesudoku.com/en/sudoku/easy/
# //td//span[@class = "fixedcell"]