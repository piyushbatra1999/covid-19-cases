import requests
response = requests.get('https://api.covid19india.org/data.json')


def generate_data(response_data):  # input is statewise data
    data_from_api = {}
    for i in range(len(response_data)):
        if response_data[i]['state'].lower() == 'state unassigned':
            continue
        data_from_api[response_data[i]['state'].lower()] = {
            "active": response_data[i]['active'],
            "confirmed": response_data[i]['confirmed'],
            "deaths": response_data[i]['deaths'],
            "recovered": response_data[i]['recovered'],
            "confirmed_inc": response_data[i]['deltaconfirmed'],
            "deaths_inc": response_data[i]['deltadeaths'],
            "recovered_inc": response_data[i]["deltarecovered"],
            "update": response_data[i]['lastupdatedtime'],
            "state": response_data[i]['state']}
    return data_from_api


def get_data(response_data):
    if response_data['state'] == 'Total':
        data = f'''Here\'s the stats for India:\nActive: {response_data['active']}\nConfirmed: {response_data['confirmed']}\nRecovered: {response_data['recovered']}\nDeceased: {response_data['deaths']}\nIncrease in Confirmed cases:\n{response_data['confirmed_inc']}\nIncrease in Deceased cases:\n{response_data['deaths_inc']}\nIncrease in confirmed cases:\n{response_data['recovered_inc']}\nLast updated:{ response_data['update']} '''
    else:
        data = f'''State: {response_data['state']}\nActive: {response_data['active']}\nConfirmed: {response_data['confirmed']}\nRecovered: {response_data['recovered']}\nDeceased: {response_data['deaths']}\nIncrease in Confirmed cases:\n{response_data['confirmed_inc']}\nIncrease in Deceased cases:\n{response_data['deaths_inc']}\nIncrease in confirmed cases:\n{response_data['recovered_inc']}\nLast updated:{ response_data['update']} '''
    return data


def fetch(state):
    if response.status_code == 200:
        data = generate_data(response.json()['statewise'])
        if state == 'india':
            return get_data(data['total'])
        else:
            return get_data(data[state])
    else:
        return 'Can\'t connect to the API right now. \n Please try again later.'
