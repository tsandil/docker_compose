import requests
import redis
import time

# Create Connection to Redis 
eng = redis.Redis(
     host='redis', 
     port=6379, 
    #  decode_responses=True
     )

def fetch_data():
    url = f'https://api.coindesk.com/v1/bpi/currentprice.json'
    print(f"The URL is : {url}\n")

    try:
        response = requests.get(url=url)
        response.raise_for_status()
        data = response.json()
        eng.set(f"crypto_data:{int(time.time()*1000)}",data['bpi']['USD']['rate_float'])
        print(f"\nData Stored in Redis is : {data['bpi']['USD']['rate_float']}")
    except requests.RequestException as e:
        print(f"Error Fetching the Data : {e}")
    return data

if __name__ =='__main__':
        for i in range(2):
            data = fetch_data()
            time.sleep(2)
