import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from csv import writer
import re


def fnamefunc():
    return newsoup.find("span", id="_ctl27__ctl1_first_name").text if newsoup.find("span", id="_ctl27__ctl1_first_name") else 'None'

def mnamefunc():
    return newsoup.find("span", id="_ctl27__ctl1_m_name").text if newsoup.find("span", id="_ctl27__ctl1_m_name") else 'None'

def lnamefunc():
    return newsoup.find("span", id="_ctl27__ctl1_last_name").text if newsoup.find("span", id="_ctl27__ctl1_last_name") else 'None'

def lnumfunc():
    if newsoup.find("span", id="_ctl36__ctl1_license_no"):
        return newsoup.find("span", id="_ctl36__ctl1_license_no").text
    elif newsoup.find("span", id="_ctl39__ctl1_license_no"):
        return newsoup.find("span", id="_ctl39__ctl1_license_no").text
    else:
        return "None"
        

def ltypefunc():
    if newsoup.find("span", id="_ctl36__ctl1_license_type"):
        return newsoup.find("span", id="_ctl36__ctl1_license_type").text
    elif newsoup.find("span", id="_ctl39__ctl1_license_type"):
        return newsoup.find("span", id="_ctl39__ctl1_license_type").text
    else:
        return "None"

def statusfunc():
    if newsoup.find("span", id="_ctl36__ctl1_status"):
        return newsoup.find("span", id="_ctl36__ctl1_status").text
    elif newsoup.find("span", id="_ctl39__ctl1_status"):
        return newsoup.find("span", id="_ctl39__ctl1_status").text
    else:
        return "None"
def origfunc():
    if newsoup.find("span", id="_ctl36__ctl1_issue_date"):
        return newsoup.find("span", id="_ctl36__ctl1_issue_date").text
    elif newsoup.find("span", id="_ctl39__ctl1_issue_date"):
        return newsoup.find("span", id="_ctl39__ctl1_issue_date").text
    else:
        return "None"
def expiryfunc():
    if newsoup.find("span", id="_ctl36__ctl1_expiry"):
        return newsoup.find("span", id="_ctl36__ctl1_expiry").text
    elif newsoup.find("span", id="_ctl39__ctl1_expiry"):
        return newsoup.find("span", id="_ctl39__ctl1_expiry").text
    else:
        return "None"
def renewedfunc():
    if newsoup.find("span", id="_ctl36__ctl1_last_ren"):
        return newsoup.find("span", id="_ctl36__ctl1_last_ren").text
    elif newsoup.find("span", id="_ctl39__ctl1_last_ren"):
        return newsoup.find("span", id="_ctl39__ctl1_last_ren").text
    else:
        return "None"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
os.environ["PATH"] += r"C:\\Users\BARIAJB\OneDrive - Reed Elsevier Group ICO Reed Elsevier Inc\\Desktop\\dev"
driver = webdriver.Chrome(options=options)
driver.maximize_window
driver.get("https://idbop.mylicense.com/verification/Search.aspx")
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//input[@id='t_web_lookup__last_name']").send_keys('L*')
driver.find_element(By.XPATH, "//input[@id='sch_button']").click()


PAGE_SOURCE_OVERVIEW = driver.page_source
soup = BeautifulSoup(PAGE_SOURCE_OVERVIEW, features="lxml")

lists = soup.find(id="datagrid_results")

LINKS = []
LINKS2 = []
LINKS3 = []
LINKS4 = []

with open('datascraped.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['FirstName', 'Middle Name', 'Last Name', 'LicenseNum', 'LicenseType', 'Status', 'Orig Issued Date', 'Expiry', 'Renewed']
    thewriter.writerow(header)
    print(header)
     
    for a in lists.find_all("a", id=re.compile("datagrid_results__ct")):
        LINKS.append(a["id"])
        
    for names in LINKS:
        driver.find_element(By.ID, names).click()
        driver.switch_to.window(driver.window_handles[1])
        soup2 = driver.page_source
        newsoup = BeautifulSoup(soup2, features="lxml")
        fName = fnamefunc()
        mName = mnamefunc()
        lName = lnamefunc()
        lNumber = lnumfunc()
        lType = ltypefunc()
        status = statusfunc()
        orig_issued_date = origfunc()
        expiry = expiryfunc()
        renewed = renewedfunc()
        

        # print(fName,mName,lName,lNumber,lType,status, orig_issued_date, expiry,renewed)
        info = [fName,mName,lName,lNumber,lType, status, orig_issued_date, expiry, renewed]
        thewriter.writerow(info)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    print('Successful start..')
    print('Scrapping... part 1/4')
    for i in range(2,41):
        driver.find_element(by=By.LINK_TEXT, value=str(i)).click()
        for a in lists.find_all("a", id=re.compile("datagrid_results__ct")):
            LINKS2.append(a["id"])
            
            for names in LINKS2:
                driver.find_element(By.ID, names).click()
                driver.switch_to.window(driver.window_handles[1])
                soup2 = driver.page_source
                newsoup = BeautifulSoup(soup2, features="lxml")
                
                fName = fnamefunc()
                mName = mnamefunc()
                lName = lnamefunc()
                lNumber = lnumfunc()
                lType = ltypefunc()
                status = statusfunc()
                orig_issued_date = origfunc()
                expiry = expiryfunc()
                renewed = renewedfunc()
                
                # print(fName,mName,lName,lNumber,lType,status, orig_issued_date, expiry,renewed)
                info = [fName,mName,lName,lNumber,lType, status, orig_issued_date, expiry, renewed]
                thewriter.writerow(info)
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                LINKS2.clear()
    print('still crapping...part 2/4' ) 
                
    driver.find_element(by=By.LINK_TEXT, value="...").click()
    
    for a in lists.find_all("a", id=re.compile("datagrid_results__ct")):
        LINKS3.append(a["id"])
        
    for names in LINKS3:
        driver.find_element(By.ID, names).click()
        driver.switch_to.window(driver.window_handles[1])
        soup2 = driver.page_source
        newsoup = BeautifulSoup(soup2, features="lxml")
        fName = fnamefunc()
        mName = mnamefunc()
        lName = lnamefunc()
        lNumber = lnumfunc()
        lType = ltypefunc()
        status = statusfunc()
        orig_issued_date = origfunc()
        expiry = expiryfunc()
        renewed = renewedfunc()
        
        # print(fName,mName,lName,lNumber,lType,status, orig_issued_date, expiry,renewed)
        info = [fName,mName,lName,lNumber,lType, status, orig_issued_date, expiry, renewed]
        thewriter.writerow(info)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
         
    print('almost done scrapping...3/4')    
    for i in range(42,65):
        driver.find_element(by=By.LINK_TEXT, value=str(i)).click()
        for a in lists.find_all("a", id=re.compile("datagrid_results__ct")):
            LINKS4.append(a["id"])
            
            for names in LINKS4:
                driver.find_element(By.ID, names).click()
                driver.switch_to.window(driver.window_handles[1])
                soup2 = driver.page_source
                newsoup = BeautifulSoup(soup2, features="lxml")
                fName = fnamefunc()
                mName = mnamefunc()
                lName = lnamefunc()
                lNumber = lnumfunc()
                lType = ltypefunc()
                status = statusfunc()
                orig_issued_date = origfunc()
                expiry = expiryfunc()
                renewed = renewedfunc()
                
                # print(fName,mName,lName,lNumber,lType,status, orig_issued_date, expiry,renewed)
                info = [fName,mName,lName,lNumber,lType, status, orig_issued_date, expiry, renewed]
                thewriter.writerow(info)
                driver.close()
                driver.switch_to.window(driver.window_handles[0])  
                LINKS4.clear()
    print('Part 4/4')
    print('Done scrapping')
