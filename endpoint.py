import requests
def urlcheck(url):
    try:
        resp = requests.get(url)
    except:
        print('please double check your url')
    else:

        status = resp.status_code
        if status == 200:
            print('site is up')
        else:
            print('site is down')