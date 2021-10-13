import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class Bot:

    # Abrir chrome em debug
    # /usr/bin/google-chrome-stable --remote-debugging-port=9222 --user-data-dir=/home/paulo/workspace/bot/chromeProfile

    def __init__(self):
        opt = Options()
        opt.add_experimental_option("debuggerAddress", "localhost:9222")
        self.driver = webdriver.Chrome(executable_path="/home/paulo/workspace_python/bot/chromedriver", options=opt)
        self.actions = ActionChains(self.driver)
        self.type = "title"
        self.amount_diff = 10000

    def start(self):
        print("Iniciando...")

        if "cost" in self.type:
            items = self.get_elements_by_cost()
            if len(items) == 0:
                print(f"Itens indisponíveis...")
                self.refresh()
                self.start()
            self.do_it(self.get_elements_by_cost(), "../..")
        else:
            items = self.get_elements_by_title()
            if len(items) == 0:
                print(f"Itens indisponíveis...")
                self.refresh()
                self.start()
            self.do_it(self.get_elements_by_title(), "..")

    def refresh(self):
        time.sleep(2)
        print("Refreshing...")
        self.driver.refresh()
        time.sleep(5)

    def get_elements_by_title(self):

        all_items = self.driver.find_elements(By.CLASS_NAME, "item-title")

        items_map = {}
        for itemTitle in all_items:
            if "Assinatura" in itemTitle.text:
                cost = itemTitle.find_element_by_xpath("./following-sibling::div").find_element(By.CLASS_NAME,
                                                                                                "item-cost")
                item_qtd = itemTitle.find_element_by_xpath("..") \
                    .find_element(By.CLASS_NAME, "item-quantity-left").find_element(By.TAG_NAME, "span").text
                if "out" not in item_qtd:
                    items_map[cost.text.split()[1]] = itemTitle

        return sorted(items_map.items(), reverse=True)

    def get_elements_by_cost(self):

        amount_total = int(self.driver.find_element_by_xpath(
            "//*[@id='app']/div/md-content/div[1]/div[1]/div[4]/div[1]/p[1]/span/strong"
        ).text.replace(',', ''))

        all_items_info = list(
            filter(lambda cost: amount_total >= int(cost.text.split()[1]) >= (amount_total - self.amount_diff),
                   self.driver.find_elements(By.CLASS_NAME, "item-cost")))

        if len(all_items_info) == 0:
            return all_items_info

        items_map = {}
        for info in all_items_info:
            item_qtd = info.find_element_by_xpath("..") \
                .find_element(By.CLASS_NAME, "item-quantity-left").find_element(By.TAG_NAME, "span").text
            if "out" not in item_qtd:
                items_map[(info.text.split()[1])] = info

        return sorted(items_map.items(), reverse=True)

    def do_it(self, elements, back_path):

        print(f"[{len(elements)}] itens encontrados")

        was_redeemed = False
        steam_url = "https://steamcommunity.com/tradeoffer/new/?partner=158585055&token=WTh7nnsx"
        item_redeemed = ""

        #     for itemTitle in elements:
        #         if "Anubis" in itemTitle.text:
        #             item_qtd = itemTitle.find_element_by_xpath("./following-sibling::div").find_element(
        #                 By.CLASS_NAME, "item-quantity-left").find_element(By.TAG_NAME, "span")
        #             if "out" not in item_qtd.text:
        #                 elements_list[itemTitle] = item_qtd
        #
        # print(f"[{len(elements_list)}] itens para iterar")
        #
        #     if len(elements_list) == 0:
        #         print(f"Itens indisponíveis...")
        #         self.refresh()
        #         self.start()
        #
        #

        for key, value in elements:
            if was_redeemed:
                print(f"Item de valor [{item_redeemed}] retirado. Finalizando...")
                break

            redeem_btn = value.find_element_by_xpath(back_path).find_element_by_xpath("./following-sibling::div")
            self.actions.move_to_element(redeem_btn).perform()
            redeem_btn.click()
            time.sleep(1)
            # form = self.driver.find_element(By.NAME, "vm.redemptionForm")
            # form.find_element(By.TAG_NAME, "button").click()
            # form.find_element(By.TAG_NAME, "input").send_keys(steam_url)
            # form.submit()
            item_redeemed = key
            was_redeemed = True
            print(f"Retirando o item de valor [{item_redeemed}]")

        if not was_redeemed:
            print(f"Nenhum item retirado :( Finalizando...")


bot = Bot()
bot.start()
