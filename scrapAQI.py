import requests
import base64

url = "https://app.cpcbccr.com/aqi_dashboard/aqi_all_Parameters"

cookieFromHeader = 'ccr_captcha="jm6vXf3io8f1h+dwnwiOUBKfFglQB5e95G53cIWmYRpZ1WtQRmSCe9RNBLkDIZFqFfPOuu04RiM7jKrusTwi7PQKAqexaS5ckPW7Pa8AV6SzbKpRZUCdo2priZDl/u7a57F5P2mu6VR2LqrsXcrHjltLSZuY0hgzt22fIZMvdqaX4kj0Deu6/aoFTeqoCdmvY96myamDOWkWKr48Y614Pfkdxfd7KMO4kWAlXwV+mmQ="; ccr_public="qE/YAekPaR/hLEQYQpi1SDdh19Jm+10LWAHSUOr07HN87RZDp0uJ9NpTHv0UpJok9mii50IcVnDLLd3RHSvIDKWFq5o/beNcEgnpw+unTQRplARq/st98EqDyRooWBrrYTlmoytNeHA47KXdib1j6TL5k9K/JKJNNoMkCBEh8+TnMe0b6qALf4r6xpXSQItyroa9Eh41mC/d7NQ9zy5PaWJeBgOHTUPdvs83WxpBbkt9c3402086KI7MOdVHPt86sBec0ru3gZrEhndmQ054u2r+TF8aRxEarwXLtMggsQGtbAfJQd+0IUTcF1N2Jzjm'

headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Cookie': cookieFromHeader}

reqBody = '{"station_id":"site_301","date":"2023-02-08T16:00:00Z"}'.encode()

encodedReqBody = base64.b64encode(reqBody).decode()

res = requests.post(url, data=encodedReqBody, headers=headers)

resBody = base64.b64decode(res.text).decode()

print(resBody)