import requests


def the_most_intelligent(names):
    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
    response = requests.get(url).json()
    intelligence = -1
    for hero in response:
        if hero['name'] in names and hero['powerstats']['intelligence'] > intelligence:
            intelligence = hero['powerstats']['intelligence']
            name = hero['name']
    return f'{name}, {intelligence}'


if __name__ == '__main__':
    print(the_most_intelligent(['Hulk', 'Thanos', 'Capitan America']))
