from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from timeit import default_timer as timer
from datetime import timedelta
from datetime import datetime 
import time

class Bot:
    # username = ''
    # password = ''
    
    geckodriver = '/home/paulo/workspace/bot/geckodriver'

    def __init__(self):
        firefoxProfile = webdriver.FirefoxProfile()
        firefoxProfile.set_preference("intl.accept_languages", "pt,pt-BR")
        firefoxProfile.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Firefox(
            firefox_profile=firefoxProfile, executable_path=self.geckodriver
        )

    # def login(self):
        # print(f'######  Início! -> {datetime.now()}')
        # driver = self.driver
        # driver.get("")
        # time.sleep(3)
        # user_element = driver.find_element_by_xpath("//*[@id='login-username']")
        # user_element.clear()
        # user_element.send_keys(self.username)
        # time.sleep(2)
        # password_element = driver.find_element_by_xpath("//*[@id='password-input']")
        # password_element.clear()
        # password_element.send_keys(self.password)
        # time.sleep(2)
        # password_element.send_keys(Keys.RETURN)
        # time.sleep(5)
        # self.post_comment()
        # driver.quit()
        # print(f'######  Fim!')

    # @staticmethod
    # def type_like_a_person(sentence, single_input_field):
    #     for letter in sentence:
    #         single_input_field.send_keys(letter)
    #         time.sleep(random.randint(5, 10) / 30)

    # def post_comment(self):
    #     driver = self.driver
    #     for pic_href in self.links_de_posts:
    #         driver.get(pic_href)
    #         # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
    #         # num_comments = random.randint(5,20)
    #         num_comments = 10

    #         lst_used_comments = []
    #         print(f'Comentando [{num_comments}] vezes no post [{pic_href}]')
    #         for a in range(num_comments):
    #             try:
    #                 driver.find_element_by_class_name("Ypffh").click()
    #                 comment_input_box = driver.find_element_by_class_name("Ypffh")
    #                 comment_input_box.clear()
    #                 time.sleep(1)

    #                 comment = random.choice(self.comments)

    #                 while(comment in lst_used_comments):
    #                     comment = random.choice(self.comments)
                    
    #                 lst_used_comments.append(comment)

    #                 self.type_like_a_person(comment, comment_input_box)
    #                 time.sleep(random.randint(1, 3))
    #                 # driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]").click()

    #                 print(f'{self.count_comment} comentários')

    #                 self.count_comment += 1
    #                 time.sleep(random.randint(60, 80))
    #             except Exception as e:
    #                 print(e)
    #                 time.sleep(5)
            
    #         # print(f'-> {lst_used_comments}')
        
    #     # self.post_comment()

bot = Bot()
bot.login()