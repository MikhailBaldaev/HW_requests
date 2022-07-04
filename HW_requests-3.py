import requests
from datetime import datetime, timedelta


def get_quaries(days, tag):
    url = 'https://api.stackexchange.com/2.3/questions'
    to_date = int(datetime.now().timestamp())
    from_date = int((datetime.now() - timedelta(days=days)).timestamp())
    params = {
        'site': 'stackoverflow',
        'order': 'desc',
        'sort': 'activity',
        'fromdate': from_date,
        'todate': to_date,
        'tagged': tag,
        'page': 1,
        'pagesize': 100
    }
    result = []
    while True:
        response = requests.get(url, params=params).json()
        for item in response['items']:
            result.append(item['title'])
        if not response['has_more']:
            break
        params['page'] += 1
    return result


if __name__ == '__main__':
    print(*get_quaries(2, 'Python'), sep='\n')