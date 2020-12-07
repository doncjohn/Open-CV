import requests
import json

def ocr_space_file(filename, overlay=False, api_key='', language='eng'):
    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()

result = ocr_space_file(filename='a.png', language='eng')
result = json.loads(result)
result = result.get("ParsedResults")[0].get("ParsedText")
print(result)
