import random
import unittest
from time import sleep
from selenium import webdriver
from api_mock_data import ApiMockData
from selenium.webdriver.support.ui import Select 

class CreateNewUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver = self.driver
        driver.maximize_window()
        driver.get('http://127.0.0.1:8000/user/plan/')

    def test_create_new_user(self):
        driver = self.driver
        sex_options = ['', 'M', 'F', 'N/A']
        active_sex_options = []

        self.assertEqual('Suscripcion', driver.title)

        email = driver.find_element_by_name('email')
        password = driver.find_element_by_name('password')
        name = driver.find_element_by_name('name')
        last_name = driver.find_element_by_name('last_name')
        user_name = driver.find_element_by_name('user_name')
        age = driver.find_element_by_name('age')
        id_credit_card = driver.find_element_by_name('id_credit_card')
        credit_card_date = driver.find_element_by_name('credit_card_date')
        safe_code = driver.find_element_by_name('safe_code')
        sex = Select(driver.find_element_by_name('sex'))
        submit_button = driver.find_element_by_id('boton_continuar')
        
        self.assertEqual(4, len(sex.options))

        for option in sex.options:
            active_sex_options.append(option.text)

        self.assertListEqual(active_sex_options, sex_options)


        self.assertTrue(email.is_enabled() 
            and password.is_enabled()
            and name.is_enabled()
            and last_name.is_enabled()
            and user_name.is_enabled()
            and age.is_enabled()
            and id_credit_card.is_enabled()
            and credit_card_date.is_enabled()
            and safe_code.is_enabled()
            and submit_button.is_enabled())

        email.clear()
        password.clear()
        name.clear()
        last_name.clear()
        user_name.clear()
        age.clear()
        id_credit_card.clear()
        credit_card_date.clear()
        safe_code.clear()

        email.send_keys(ApiMockData.email)
        sleep(1)
        password.send_keys(ApiMockData.password)
        sleep(1)
        name.send_keys(ApiMockData.name)
        sleep(1)
        last_name.send_keys(ApiMockData.last_name)
        sleep(1)
        user_name.send_keys(ApiMockData.username)
        sleep(1)
        age.send_keys(ApiMockData.age)
        sleep(1)
        sex.select_by_visible_text(ApiMockData.sex)
        sleep(1)
        id_credit_card.send_keys(ApiMockData.id_credit_card)
        sleep(1)
        credit_card_date.send_keys(ApiMockData.credit_card_date)
        sleep(1)
        safe_code.send_keys(ApiMockData.safe_code)
        sleep(1)

        submit_button.click()
        sleep(2)

        country = Select(self.driver.find_element_by_id('id_country'))
        list_countries = [option.text for option in country.options]
        country.select_by_index(random.randint(1,len(list_countries)))
        sleep(1)
        
        city = Select(self.driver.find_element_by_id('id_city'))
        list_cities = [option.text for option in city.options]
        city.select_by_index(random.randint(1, len(list_cities)))
        sleep(4)

        print(list_countries)
        print(list_cities)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
