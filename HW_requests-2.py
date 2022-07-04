import requests
from txt import token


class YandexDisk:
    url = 'https://cloud-api.yandex.net/v1/disk'

    def __init__(self, token):
        self.token = token

    def _get_headers(self):
        return {'Content-Type': 'application/json',
                'Authorization': f'OAuth {self.token}'}

    def _get_upload_link(self, disk_file_path):
        upload_url = self.url + '/resources/upload'
        headers = self._get_headers()
        params = {'path': disk_file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, params=params, headers=headers)
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path).get('href', '')
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Done")


if __name__ == '__main__':
    ya = YandexDisk(token)
    ya.upload_file_to_disk('txt.txt', 'txt.txt')