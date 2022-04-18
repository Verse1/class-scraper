from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


s= Service('./webdriver/chromedriver.exe')
f=open("classes.json","w")
driver = webdriver.Chrome(service=s)

driver.get('https://sis.nyu.edu/psc/csprod/EMPLOYEE/SA/c/NYU_SR.NYU_CLS_SRCH.GBL')
def scrape(n=99999):
    classes="[\n"
    delay = 10 # seconds
    for x in range(1,n+1):
        try:
            search=driver.find_element(By.ID, 'LINK1$'+str(x))
            search.click()
        except:
            print("no more classes")
            classes=classes[:-2]+"\n]"
            f.write(classes)
            f.close()
            driver.quit()
        try:
            elem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.TAG_NAME, "b")))
            eee=driver.find_elements_by_tag_name("b")

            for i in eee:
                if(i.value_of_css_property('font-size')=='19.2px' and i.text!=''):
                    text=i.text.replace('\"','\\\"')
                    text=text.replace('\n',' ')
                    classs=text.split(" ", 2)
                    print(classs)
                    classes+="{\n\"className\": \""+classs[2]+"\",\n" + "\"classCode\": \""+classs[0]+" "+classs[1]+"\",\n\"university\": \"New York University\",\n\"numEnrolled\": 0\n },\n"
                    
        except TimeoutException:
            print("Took too long to load")
        finally:
            try:
                back=driver.find_element(By.ID, 'NYU_CLS_DERIVED_BACK')
                back.click()

                WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'LINK1$'+str(x))))
            except TimeoutException:
                print("Took too long to load")
    classes=classes[:-2]+"\n]"
    f.write(classes)
    f.close()

scrape()

driver.quit()