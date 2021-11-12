import requests


def print_baidu():
    res = requests.get("http://www.baidu.com")
    if res.status_code == 200:
        print("changed new yes")
    else:
        print("changed new no")


if __name__ == "__main__":
    print_baidu()
