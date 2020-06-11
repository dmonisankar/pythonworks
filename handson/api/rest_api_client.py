import requests

temp_input = input("Enter temperature ( centigrade):")
req_body = 'https://8qeppepkvg.execute-api.ap-south-1.amazonaws.com/test/weather?temperature=' + temp_input
resp = requests.get(req_body)

if resp.status_code != 200:
    print("Please retry with valid input")
else:
    decoded_response = resp.json()
    if 'error' in decoded_response.keys():
        print(decoded_response['error'])
    else:
        print('It is {}'.format(decoded_response['result']))
