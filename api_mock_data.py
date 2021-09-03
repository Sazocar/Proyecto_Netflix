import random
import requests

class ApiMockData():
    response = requests.get(
        'https://my.api.mockaroo.com/users_data_registration_netflix.json?key=09283100')
    
    data = response.json()

    i = random.randint(0,99)

    email = data[i]['email']
    password = data[i]['password']
    name = data[i]['name']
    last_name = data[i]['last_name']
    username = data[i]['user_name']
    age = data[i]['age']
    sex = data[i]['sex']
    id_credit_card = data[i]['id_credit_card']
    credit_card_date = data[i]['credit_card_date']
    safe_code = data[i]['safe_code']

