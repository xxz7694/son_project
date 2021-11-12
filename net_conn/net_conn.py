import requests


def print_baidu():
    res = requests.get("http://www.baidu.com")
    if res.status_code == 200:
        print("changed yes")
    else:
        print("changed no")


if __name__ == "__main__":
    print_baidu()
