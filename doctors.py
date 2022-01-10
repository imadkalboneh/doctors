import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

#signing in
dr = webdriver.Chrome()
dr.get('https://www.thestar.com/sign-in')

time.sleep(2)

dr.find_element_by_id('capture_signIn_signInEmailAddress').send_keys('????????')
dr.find_element_by_id('capture_signIn_currentPassword').send_keys('????????')
dr.find_element_by_id('sign-in-btn').click()

time.sleep(5)

#the main bit
dr.get('https://www.thestar.com/ontario-doctor-list')

time.sleep(5)

#selects 'by specialty'
dr.find_element_by_xpath('//*[@id="body-content"]/div/div[2]/div[2]/label').click()
time.sleep(0.5)
search = dr.find_element_by_css_selector('#body-content > div > div.DoctorSearchInput.active > div > input')
search.send_keys('di' + Keys.DOWN + Keys.ENTER)

f = open('list.txt', 'w')

time.sleep(2)

#117 pages, 10 rows
for i in range(1, 117, 1):

    for j in range(1, 11, 1):
            
        dr.find_element_by_xpath('//*[@id="body-content"]/div/div[3]/div[2]/div[1]/div[3]/div[' + str(j) + ']/div/div[1]').click()
        time.sleep(0.5)

        name = dr.find_element_by_class_name('DoctorDatabaseDoctorPage__name').text
        billed = dr.find_element_by_css_selector('#body-content > div > div.DoctorDatabaseDoctorPage.active > div > div:nth-child(1) > p').text
        days_worked = dr.find_element_by_css_selector('#body-content > div > div.DoctorDatabaseDoctorPage.active > div > div:nth-child(2) > p').text
        bill_rank = dr.find_element_by_css_selector('#body-content > div > div.DoctorDatabaseDoctorPage.active > div > div:nth-child(3) > p').text
        pat_vits = dr.find_element_by_css_selector('#body-content > div > div.DoctorDatabaseDoctorPage.active > div > div:nth-child(4) > p').text

        f.write(name + '\n')
        f.write('-------------------------------\n')
        f.write('Total billed: ' + billed + '\n')
        f.write('Days worked: ' + days_worked + '\n')
        f.write('Billing rank: ' + bill_rank + '\n')
        f.write('Patient visits: ' + pat_vits + '\n\n')
        
        dr.find_element_by_class_name('DoctorDatabaseDoctorPage__backButton').click()
        time.sleep(1)
    
    #next page
    n = dr.find_element_by_xpath('//*[@id="body-content"]/div/div[3]/div[2]/div[2]/div/div[2]/div[2]/button')
    dr.execute_script("arguments[0].click();", n)
    
f.close()