from selenium import webdriver
from os import system, name
import chromedriver_binary
from time import time, strftime, gmtime, sleep
import pyfiglet, os, threading
import chromedriver_autoinstaller

# Check if the current version of chromedriver exists
# and if it doesn't exist, download it automatically,
# then add chromedriver to path
chromedriver_autoinstaller.install()

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

clear()
system('title CHO66X-BOT V3')

print(pyfiglet.figlet_format("CHO66X-BOT", font="slant"))
print("1. Viewers Bot.\n2. Likes Bot -sedang dalam pengembangan-.\n3. Followers Bot -sedang dalam pengembangan-.\n3. Share Bot.\n4. Share Bot Juga.\n")

auto = int(input("Mode: "))

if auto == 1 or auto == 2 or auto == 3 or auto == 4:
    vidUrl = input("Link Video TikTok: ")

    start = time()
    time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome( options=chrome_options)
    driver.set_window_size(1024, 650)

    Views = 0
    Hearts = 0
    Followers = 0

def beautify(arg):
    return format(arg, ',d').replace(',', '.')

def title1(): # Update the title IF option 1 was picked.
    global Views
    
    while True:
        time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))
        system(f'title CHO66X-BOT V3 ^| Views Sent: {beautify(Views)} ^| Elapsed Time: {time_elapsed}')

def title2(): # Update the title IF option 2 was picked.
    global Hearts
    
    while True:
        time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))
        system(f'title CHO66X-BOT V3 ^| Hearts Sent: {beautify(Hearts)} ^| Elapsed Time: {time_elapsed}')

def title3(): # Update the title IF option 3 was picked.
    global Followers
    
    while True:
        time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))
        system(f'title CHO66X-BOT V3 ^| Followers Sent: {beautify(Followers)} ^| Elapsed Time: {time_elapsed}')
        
def title4(): # Update the title IF option 1 was picked.
    global Shares
    
    while True:
        time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))
        system(f'title CHO66X-BOT V3 ^| Shares Sent: {beautify(Shares)} ^| Elapsed Time: {time_elapsed}')

    
def loop1():
    global Views
    sleep(10)
    
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[4]/div/button").click()
        
    except:
        print("[-] Captcha belum terpecahkan!")
        driver.refresh()
        loop1()
        
    try:
        sleep(2)
        driver.find_element_by_xpath("//*[@id=\"sid4\"]/div/form/div/input").send_keys(vidUrl)
        
        sleep(1)
        driver.find_element_by_xpath("//*[@id=\"sid4\"]/div/form/div/div/button").click()
        
        sleep(5)
        driver.find_element_by_xpath("//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9V\"]/div[1]/div/form/button").click()
        
        driver.refresh()
        Views += 1000
        print("[+] Views dikirim!")
        
        sleep(300)
        loop1()
        
    except:
        print("[-] Masih Delay. Kita Mencoba lagi..") 
        driver.refresh()
        loop1()

def loop2():
    global Hearts
    sleep(10)
    
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[2]/div/button").click()
        
    except:
        print("[-] Captcha belum terpecahkan!")
        driver.refresh()
        loop2()
        
    try:
        sleep(2)
        driver.find_element_by_xpath('//*[@id="sid2"]/div/form/div/input').send_keys(vidUrl)
        
        sleep(1)
        driver.find_element_by_xpath('//*[@id="sid2"]/div/form/div/div/button').click()
        
        sleep(5)
        driver.find_element_by_xpath('//*[@id="c2VuZE9nb2xsb3dlcnNfdGlrdG9r"]/div[1]/div/form/button').click()
        
        sleep(6)
        hearts = driver.find_element_by_xpath('//*[@id="c2VuZE9nb2xsb3dlcnNfdGlrdG9r"]/span').text.split()
        
        Hearts += int(hearts[0])
        print("[+] Likes Dikirim!")
        
        sleep(5)
        driver.refresh()
        
        sleep(1800)
        loop2()
        
    except:
        print("[-] Masih Delay. Kita Mencoba lagi....") 
        driver.refresh()
        loop2()

def loop3():
    global Followers
    sleep(10)
    
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[1]/div/button").click()
        
    except:
        print("[-] Captcha belum terpecahkan!")
        driver.refresh()
        loop3()
        
    try:
        sleep(2)
        driver.find_element_by_xpath("//*[@id=\"sid\"]/div/form/div/input").send_keys(vidUrl)
        
        sleep(1)
        driver.find_element_by_xpath("//*[@id=\"sid\"]/div/form/div/div/button").click()
        
        sleep(5)
        driver.find_element_by_xpath("//*[@id=\"c2VuZF9mb2xsb3dlcnNfdGlrdG9r\"]/div[1]/div/form/button").click()
        sleep(6)
        folls = driver.find_element_by_xpath('//*[@id="c2VuZF9mb2xsb3dlcnNfdGlrdG9r"]/span').text.split()
        
        Followers += int(folls[0])
        print("[+] Followers dikirim!")
        driver.refresh()
        
        sleep(1800)
        loop3()
        
    except:
        print("[-] Masih Delay. Kita Mencoba lagi...")
        driver.refresh()
        loop3()

def loop4():
    global Shares
    sleep(10)
    
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[5]/div/button").click()
        
    except:
        print("[-] Captcha belum terpecahkan!")
        driver.refresh()
        loop4()
        
    try:
        sleep(2)
        driver.find_element_by_xpath("//*[@id=\"sid7\"]/div/form/div/input").send_keys(vidUrl)
        
        sleep(1)
        driver.find_element_by_xpath("//*[@id=\"sid7\"]/div/form/div/div/button").click()
        
        sleep(5)
        driver.find_element_by_xpath("//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9s\"]/div[1]/div/form/button").click()
        
        driver.refresh()
        Shares += 100
        print("[+] Shares dikirim!")
        
        sleep(300)
        loop4()
        
    except:
        print("[-] Masih Delay. Kita Mencoba lagi...")
        driver.refresh()
        loop4()

clear()

print(pyfiglet.figlet_format("CHO66X-BOT V3", font="slant"))
print("Log:")

if auto == 1:
    driver.get("https://zefoy.com/")
    
    a = threading.Thread(target=title1)
    b = threading.Thread(target=loop1)
    
    a.start()
    b.start()
    
elif auto == 2:
    driver.get("https://zefoy.com/")
    
    a = threading.Thread(target=title2)
    b = threading.Thread(target=loop2)
    
    a.start()
    b.start()
    
elif auto == 3:
    driver.get("https://zefoy.com/")
    
    a = threading.Thread(target=title3)
    b = threading.Thread(target=loop3)
    
    a.start()
    b.start()
    
elif auto == 4:
    driver.get("https://zefoy.com/")
    
    a = threading.Thread(target=title4)
    b = threading.Thread(target=loop4)
    
    a.start()
    b.start()
    
elif auto == 5:
    print("[+] Program ini dibuat oleh CHO66X. [CHO66X-BOT]")
    
else:
    print(f"{auto} yang bener lah, pilihan gak valid. Tolong pilih 1, 2, 3, 4 atau 5")
