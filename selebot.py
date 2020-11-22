from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


PATH = "C:\chromedriver\chromedriver.exe" #path to chromedriver here
URL = "https://online.seterra.com/de/vgp/3014" #dont change this, link to the site
count = 0
driver = webdriver.Chrome(PATH)
sleep(1)
driver.get(URL)

sleep(2.5)
delay = 0.01

#accept cookies
cookie = driver.find_element_by_class_name("cc_btn_accept_all")
cookie.click()
sleep(0.2)
#restart game
restart = driver.find_element_by_id("cmdRestart")
restart.click()
sleep(0.005)


#id's of the states
baden = driver.find_element_by_id("AREA_GERMANY_BADENWURTTEMBERG")
bayern = driver.find_element_by_id("AREA_GERMANY_BAYERN")
berlin = driver.find_element_by_id("AREA_GERMANY_BERLIN")
brandenburg = driver.find_element_by_id("AREA_GERMANY_BRANDENBURG")
bremen = driver.find_element_by_id("AREA_GERMANY_BREMEN")
hamburg = driver.find_element_by_id("AREA_GERMANY_HAMBURG")
hessen = driver.find_element_by_id("AREA_GERMANY_HESSEN")
mecklenburg = driver.find_element_by_id("AREA_GERMANY_MECKLENBURGVORPOMMERN")
niedersachsen = driver.find_element_by_id("AREA_GERMANY_NIEDERSACHSEN")
nordrhein = driver.find_element_by_id("AREA_GERMANY_NORDRHEINWESTFALEN")
rheinland = driver.find_element_by_id("AREA_GERMANY_RHEINLANDPFALZ")
saarland = driver.find_element_by_id("AREA_GERMANY_SAARLAND")
sachsen = driver.find_element_by_id("AREA_GERMANY_SACHSEN")
sachsen_anhalt = driver.find_element_by_id("AREA_GERMANY_SACHSENANHALT")
schleswig = driver.find_element_by_id("AREA_GERMANY_SCHLESWIGHOLSTEIN")
thuringen = driver.find_element_by_id("AREA_GERMANY_THURINGEN")



while count < 17:
    action = webdriver.common.action_chains.ActionChains(driver)

    question = driver.find_element_by_id("currQuestion")
    current = question.text
    current = current.lower()

    print(current)
    if "baden" in current:
        print("baden")
        action.move_to_element_with_offset(baden, 110, 50)
        action.click()
        action.perform()
        count += 1
        sleep(delay)
    elif "bayern" in current:
        print("bayern")
        bayern.click()
        count += 1
        sleep(delay)
    elif "berlin" in current:
        print("berlin")
        berlin.click()
        count += 1
        sleep(delay)
    elif "brandenburg" in current:
        print("brandenburg")
        brandenburg.click()
        count += 1
        sleep(delay)
    elif "bremen" in current:
        print("bremen")
        action.move_to_element_with_offset(bremen, 34, 60)
        action.click()
        action.perform()
        count += 1
        sleep(delay)
    elif "hamburg" in current:
        print("hamburg")
        hamburg.click()
        count += 1
        sleep(delay)
    elif "hessen" in current:
        print("hessen")
        action.move_to_element_with_offset(hessen, 100, 15)
        action.click()
        action.perform()
        count += 1
        sleep(delay)
    elif "mecklenburg" in current:
        print("mecklenburg")
        mecklenburg.click()
        count += 1
        sleep(delay)
    elif "niedersachsen" in current:
        print("niedersachsen")
        niedersachsen.click()
        count += 1
        sleep(delay)
    elif "nordrhein" in current:
        print("nordrhein")
        nordrhein.click()
        count += 1
        sleep(delay)
    elif "rheinland" in current:
        print("rheinland")
        rheinland.click()
        count += 1
        sleep(delay)
    elif "saarland" in current:
        print("saarland")
        action.move_to_element_with_offset(saarland, 40, 18)
        action.click()
        action.perform()
        count += 1
        sleep(delay)
    elif "anhalt" in current:
        print("sachsen anhalt")
        sachsen_anhalt.click()
        count += 1
        sleep(delay)
    elif "sachsen" in current:
        print("sachsen")
        sachsen.click()
        count += 1
        sleep(delay)
    elif "schleswig" in current:
        print("schleswig")
        schleswig.click()
        count += 1
        sleep(delay)
    elif "thüringen" in current:
        print("thüringen")
        action.move_to_element_with_offset(thuringen, 50, 10)
        action.click()
        action.perform()
        count += 1
        sleep(delay)

print("Done")

sleep(20)
driver.quit()
exit