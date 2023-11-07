from urllib import response
import requests

def main():
    url =""
    headers = {
    'x-rapidapi-host':''
    'x-rapidapi-key';''
    }
    response = requests.request("GET", url, headers = headers)


    ### to store data 
    with open('response.json','w') as f:
        json.dump(response.text, f, ensure_ascil=False)

    print(response.text)

main()
