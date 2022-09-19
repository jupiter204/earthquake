from time import sleep
import requests

url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/E-A0015-001?Authorization=CWB-21D9E424-3CCB-456F-A4D3-13D5A7FFA85A&limit=1'

tim2 = ''

while 1:

    data = requests.get(url, timeout=5)
    data_json = data.json()

    eq = data_json['records']['earthquake']

    tim = eq[0]['earthquakeInfo']['originTime']

    if tim != tim2:
        file = open('./earthquake.txt', 'a', encoding='utf-8')
        tim2 = tim
        rpt = eq[0]['reportContent']
        loc = eq[0]['earthquakeInfo']['epiCenter']['location']
        val = eq[0]['earthquakeInfo']['magnitude']['magnitudeValue']  # 芮氏規模
        dep = eq[0]['earthquakeInfo']['depth']['value']               # 地震深度
        print(f'{rpt}\n地點 {loc}，芮氏規模 {val} 級，深度 {dep} 公里\n')
        file.write(f'{rpt}\n地點 {loc}，芮氏規模 {val} 級，深度 {dep} 公里\n\n')
        file.close()

    sleep(10)
