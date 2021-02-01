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
    print('*'*20)
    if response_data['state'] == 'Total':
        print('Here\'s the stats for India:')
    else:
        print('State:', response_data['state'])
    print('Active:', response_data['active'])
    print('Confirmed:', response_data['confirmed'])
    print('Recovered:', response_data['recovered'])
    print('Deceased:', response_data['deaths'])
    print('Increase in Confirmed cases:', response_data['confirmed_inc'])
    print('Increase in Deceased cases:', response_data['deaths_inc'])
    print('Increase in confirmed cases:', response_data['recovered_inc'])
    print('Last update:', response_data['update'])
    print('*'*20)


if response.status_code == 200:
    print('******Welcome to covid_cli******')
    print('Connected to the API....')
    data = generate_data(response.json()['statewise'])
    get_data(data['total'])
    print('Available states:', list(data.keys()))
    while True:
        terminal_input = input('Enter State Name: ')
        if terminal_input == 'exit':
            break
        if terminal_input not in data.keys():
            print('Please enter a valid indian state')
            continue
        get_data(data[terminal_input])

else:
    print('Can\'t connect to the API right now. \n Please try again later.')
