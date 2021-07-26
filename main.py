from selenium import webdriver
from time import sleep, strftime
from random import randint
import pandas as pd
import idpsw
import selenium

path_chromedriver = 'chromedriver'
webdriver = webdriver.Chrome(executable_path=path_chromedriver)
webdriver.get('https://www.instagram.com/accounts/login/')
sleep(3)

uname = webdriver.find_element_by_name('username')
pswd = webdriver.find_element_by_name('password')
uname.send_keys(idpsw.id)
sleep(randint(1,2))
pswd.send_keys(idpsw.psw)
sleep(randint(1,2))
login = webdriver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button')
login.click()
sleep(randint(2,3))

# verif = webdriver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')
# verif.click()
# sleep(randint(1,2))
# verif2 = webdriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
# verif2.click()

list_comment = [ 
    'Nice!', 
    'Really cool stuff!', 
    'Nice Sharing', 
    'Great Content! <3', 
    'Really Enlightening', 
    'Thanks for sharing this post!'
]

list_hash = [
    'abcdefghijklmnopqrstuvwxyz'
    ]

list_already_followed = []

# for continous usage 
# list_already_followed = pd.read_csv('',delimiter=',').iloc[:,1:2]
# list_already_followed = list(list_already_followed['0']) 

new_user = []
followed = 0
like = 0
comments = 0
x = 0

while x < 5:
    for hashtag in list_hash: 
        try:
            webdriver.get('https://www.instagram.com/explore/tags/'+hashtag[randint(0,25)]+'/')
            sleep(randint(5,6))
            firstpost = webdriver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')
            firstpost.click()
            sleep(randint(1,2))
            uname = webdriver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div/span/a')
            if uname.text not in list_already_followed:
                new_user.append(uname.text)
                try:
                    # comments += 1
                    # webdriver.find_element_by_class_name("RxpZH").click()
                    # sleep(1)
                    # webdriver.find_element_by_xpath("//textarea[@placeholder='Add a comment…']").send_keys(list_comment[randint(0,5)])
                    # sleep(1)
                    # webdriver.find_element_by_xpath("//button[@type='submit']").click()
                    # print("Sudah Terkomen")
                    # sleep(randint(10,11))
                    
                    like += 1
                    button_like = webdriver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button')
                    button_like.click()
                    print("Sudah Terlike")
                
                    webdriver.get('https://www.instagram.com/'+uname.text+'/')
                    button_follow = webdriver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button')
                    if button_follow.text == 'Follow':
                        button_follow.click()
                        followed += 1
                    print("Sudah Terfollow")
                    sleep(randint(10,11))
                except (selenium.common.exceptions.NoSuchElementException, 
                        selenium.common.exceptions.StaleElementReferenceException):
                    continue
            else:
                continue
        except (selenium.common.exceptions.NoSuchElementException, 
                selenium.common.exceptions.StaleElementReferenceException):
            continue
    x += 1

for n in range(0,len(new_user)):
    list_already_followed.append(new_user[n])

csv_already_followed = pd.DataFrame(list_already_followed)
csv_already_followed.to_csv('list_{}_instagram_already_followed.csv'.format(strftime("%d%m%Y-%H%M%S")))

print(f'Sudah {like} like yang dilakukan oleh bot')
print(f'Sudah {comments} komentar yang dilakukan oleh bot')
print(f'Sudah {followed} akun yang diikuti oleh bot')

