import json
import urllib.request
import time

import file

API_ENDPOINT = 'https://api.scryfall.com'
SEARCH_BY_NAME_ROUTE = '/cards/named?fuzzy='
STORED_LOOk_UPS = 'existingLookups.txt'

def readLocalCardInfo(name, set):
  content = file.read(STORED_LOOk_UPS)
  snippets = content.split('###')
  for snippet in snippets :
    if snippet == '':
      continue
    if snippet.split('$$$')[0] != name or snippet.split('$$$')[1] != set:
      continue
    return {
      'name': name,
      'set': set,
      'correctedName': snippet.split('$$$')[2],
      'reprint': int(snippet.split('$$$')[3])
    }
  return None

def storeLocalCardInfo(info):
  print(info)
  content = file.read(STORED_LOOk_UPS)
  newContent = content + '###' + info['name'] + '$$$' + info['set'] + '$$$' + info['correctedName'] + '$$$' + str(info['reprint'])
  file.write(STORED_LOOk_UPS, newContent)

def requestSetVariants(url, set, lang):
  webURL = urllib.request.urlopen(url)
  data = webURL.read()
  encoding = webURL.info().get_content_charset('utf-8')
  contents = json.loads(data.decode(encoding))
  variants = 0
  for cardPrint in contents['data']:
    if cardPrint['set'] == set and cardPrint['lang'] == lang:
      variants = variants + 1
  return variants

def byNameAndSet(name, set, lang):
  localInfo = readLocalCardInfo(name, set)
  if localInfo is not None:
    return localInfo

  urlFriendlyName = name.replace(' ','+')
  url = API_ENDPOINT+SEARCH_BY_NAME_ROUTE+urlFriendlyName+'&set='+set
  print('request from card details from \n', url)
  webURL = urllib.request.urlopen(url)
  data = webURL.read()
  encoding = webURL.info().get_content_charset('utf-8')
  contents = json.loads(data.decode(encoding))

  variantsCnt = requestSetVariants(contents['prints_search_uri'], contents['set'], lang)

  cardInfo = {
    'name': name,
    'set': set,
    'correctedName': contents['name'],
    'reprint': variantsCnt
  }
  time.sleep(0.05)
  storeLocalCardInfo(cardInfo)
  return cardInfo

  
