import requests

# Put here your token from https://yandex.ru/dev/disk/poligon/
YANDEX_TOKEN = 'AgAAAAA6wCXpAADLW3o9UKJyK0n6qX3OfUgGEWI'


def creating_folder_on_yd(folder_name='qwerty_qwerty_qwerty', token=YANDEX_TOKEN):
    response = requests.put(
        "https://cloud-api.yandex.net/v1/disk/resources",
        params={"path": folder_name},
        headers={"Authorization": f"OAuth {token}"}
    )
    return response.status_code


if __name__ == '__main__':
    creating_folder_on_yd.__call__()
