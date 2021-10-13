from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

from selenium.webdriver.common.by import By


class Bot:

    # Abrir chrome em debug
    # /usr/bin/google-chrome-stable --remote-debugging-port=9222 --user-data-dir=/home/paulo/workspace/bot/chromeProfile

    def __init__(self):
        opt = Options()
        opt.add_experimental_option("debuggerAddress", "localhost:9222")
        self.driver = webdriver.Chrome(executable_path="/home/paulo/workspace_python/bot/chromedriver", options=opt)
        self.actions = ActionChains(self.driver)
        self.skin_title = "USP-S | Neo-Noir"
        self.steam_url = "https://steamcommunity.com/tradeoffer/new/?partner=158585055&token=WTh7nnsx"

    def start(self):
        while not self.get_element():
            self.refresh()

        print("### Iniciando ###")
        self.do_it(self.get_element())

    def refresh(self):
        print("Atualizando a página.")
        self.driver.refresh()
        time.sleep(5)
        self.start()

    def do_it(self, element):
        print(f"Item [{element.text}] encontrado.")

        item_qtd = element.find_element_by_xpath("./following-sibling::div") \
            .find_element(By.CLASS_NAME, "item-quantity-left").find_element(By.TAG_NAME, "span")

        if "out" not in item_qtd.text:
            print("Item disponivel. Retirando.")
            redeem_btn = element.find_element_by_xpath("..").find_element_by_xpath("./following-sibling::div")
            self.actions.move_to_element(redeem_btn).perform()
            redeem_btn.click()
            time.sleep(1)
            form = self.driver.find_element(By.NAME, "vm.redemptionForm")
            form.find_element(By.TAG_NAME, "button").click()
            print("Preenchendo com a url da steam.")
            form.find_element(By.TAG_NAME, "input").send_keys(self.steam_url)
            # form.submit()
            time.sleep(2)
            print(f"Item [{element.text}] retirado com sucesso.")
            print("### Finalizando ###")
            quit()
        else:
            print("Item ainda não disponivel.")
            self.refresh()

    def get_element(self):
        try:
            return self.driver.find_element_by_xpath("//*[contains(text(),'{0}')]".format(self.skin_title))
        except NoSuchElementException:
            print(f"Item [{self.skin_title}] não encontrado.")
            return


bot = Bot()
bot.start()
