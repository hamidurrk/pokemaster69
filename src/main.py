from selenium import webdriver
import time
import random
import sys
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from tqdm import tqdm

def gen_prompt(message, value = 70, char="-"):
    print("\n")
    wrt = " " + message + " "
    print(wrt.center(value, char))
    print("\n")

def loading(i, total):
    progress = (i / total) * 100
    sys.stdout.write('\r')
    sys.stdout.write("Poke Progress: | %-50s | %0.2f%% (%d poked)" % ('█' * int(progress/2), progress, i))
    sys.stdout.flush()

def wait(duration):
    num_iterations = 100
    time_interval = (duration-1) / num_iterations

    with tqdm(total=num_iterations, desc="Loading", unit="iteration", ncols=100) as pbar:
        for _ in range(num_iterations):
            time.sleep(time_interval)
            pbar.update(1)
    print("\n")

class PokeMaster69:
    def __init__(self, username, password, browser_type=0):
        self.username = username
        self.password = password
        gen_prompt("PokeMaster69: The Ultimate Socializing Tool")
        firefox_options = webdriver.FirefoxOptions()
        # firefox_options.add_argument("--headless") 
        firefox_options.add_argument("--devtools")
        if (browser_type):
            self.bot = webdriver.Firefox(executable_path=GeckoDriverManager().install(), service_args = ['--marionette-port', '2828', '--connect-existing'], options=firefox_options)
        else:
            self.bot = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        # self.bot.set_window_position(0, 0) 
        # self.bot.set_window_size(960, 1043)
        sys.stdout.flush()
        gen_prompt("PokeMaster69 initialized", char="#")
        print("\n")
    
    def highlight_element(self, element, color='yellow'):
        bot = self.bot
        original_style = element.get_attribute('style')
        new_style = f"border: 2px solid {color}; background-color: yellow; {original_style}"
        bot.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, new_style)

    def login(self):
        bot = self.bot
        bot.get("https://www.facebook.com/")
        time.sleep(1)
        gen_prompt("Navigated to Facebook", char="#")
        try:
            bot.find_element_by_xpath('//*[@id="email"]').send_keys(self.username)
            gen_prompt("Username Entered")
            bot.find_element_by_xpath('//*[@id="pass"]').send_keys(self.password)
            gen_prompt("Password Entered")
            time.sleep(1)
            
            bot.find_element_by_xpath('//*[@id="pass"]').send_keys(Keys.RETURN)
            gen_prompt("Login Requested")
            wait(5)
            
            print("\n"*4)
        except:
            pass
        
    def poke(self, new_people_to_poke=50):
        bot = self.bot
        poke_url = 'https://www.facebook.com/pokes/'
        current_url = bot.current_url
        
        if (current_url != poke_url):
            bot.get('https://www.facebook.com/pokes/')
            gen_prompt("Navigating to " + self.username + "'s Pokes", char="#")
            wait(4)
        gen_prompt("Displaying " + self.username + "'s Pokes", char="#")
                 
        while(1):    
            poke_box = bot.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[1]")
            poke_backs = poke_box.find_elements_by_xpath("./div")
            num_poke_backs = len(poke_backs) - 2
            print(f"Number of people waiting for Poke Back: {num_poke_backs}")  
            poke_count = 0
            new_poke_count = 0
            
            for i in range(2, num_poke_backs + 2):
                loading(i - 1, num_poke_backs)
                pokes = f"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[1]/div[{i}]/div/div/div[1]/div[2]/div[2]/div/div/div"
                try:
                    element = bot.find_element_by_xpath(pokes)
                    # bot.element.click()
                    self.highlight_element(element)
                    poke_count += 1
                except Exception as e:
                    # print("Poke box error:", e)
                    continue
                # time.sleep(random.randint(5, 15))
                time.sleep(0.1)
            print(f"\nSuccessfully Poked {poke_count} People Back")
            
            for i in range(2, new_people_to_poke + 2):
                loading(i - 1, new_people_to_poke)
                pokes = f"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[2]/div[{i}]/div/div/div[1]/div[2]/div[2]/div/div/div"
                try:
                    element = bot.find_element_by_xpath(pokes)
                    new_poke_count += 1
                    # bot.element.click()
                    self.highlight_element(element)
                    check_further = bot.find_element_by_xpath(f"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[2]/div[{i+5}]/div/div/div[1]/div[2]/div[2]/div/div/div")
                    
                    is_visible = bot.execute_script("return arguments[0].getBoundingClientRect().top >= 0 && arguments[0].getBoundingClientRect().bottom <= window.innerHeight;", check_further)
                    if not is_visible:
                        # print("The element is not visible on the screen.")
                        bot.execute_script("window.scrollBy(0, 1000);")
                        time.sleep(0.5)

                    
                except Exception as e:
                    # print("Poke box error:", e)
                    bot.execute_script("window.scrollBy(0, 1000);")
                    time.sleep(0.5)
                    continue
                # time.sleep(random.randint(5, 15))
                time.sleep(0.1)
            print(f"\nSuccessfully Poked {new_poke_count} New People")
            bot.get('https://www.facebook.com/pokes/')
            gen_prompt("Reloading " + self.username + "'s Pokes", char="#")
            wait(4)
            
with open("C:\\Users\\hamid\\OneDrive\\Documents\\credential.txt", 'r', encoding='utf-8') as f:
    password = f.read()

pokemaster = PokeMaster69('hamidur.rk', password, browser_type=1)

# pokemaster.login()
pokemaster.poke()