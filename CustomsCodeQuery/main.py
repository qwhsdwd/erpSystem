import requests
import json
import time


def run(number):
    headers = {
        "authority": "music.163.com",
        "method": "GET",
        "path": "/",
        "scheme": "https",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "accept-encoding": "gzip,deflate,br",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "max-age=0",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"
    }
    url = "https://unipass.customs.go.kr/csp/retrievePersEcmVldyVrfc.do"
    pyload = {"persEcm": number, "dcerNm": "", "cralTelno": ""}
    response = requests.post(url, data=pyload, headers=headers).text
    try:
        result = json.loads(response)
        if result['rslt'] == '일치':
            return True
        else:
            return False
    except:
        return False


if __name__ == '__main__':
    start = time.time()
    number = "P160014628371"
    result = run(number)
    if result:
        print(number, "正确")
    else:
        print(number, "错误")
    print("共用时{}".format(time.time()-start))
