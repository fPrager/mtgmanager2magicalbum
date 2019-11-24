import request

LANGUAGES = ['en', 'de', 'pt', 'it', 'es', 'ja', 'cn', 'ru', 'tw', 'ko', ]
SET_CORRECTIONS = {
  'PELD': 'ELD',
  'FEM': 'FE',
  'PMEI': 'ZEN',
  'GK2_AZORIU': 'RTR',
  'DD3_GVL':'GVL',
  'DD3_JVC': 'JVC'
}

def mapVersion(name, set, lang):
  cardInfo = request.byNameAndSet(name, set, lang)
  if cardInfo['reprint'] > 1:
    return str(cardInfo['reprint'])
  return ''

def removeLowerCase(name, set, lang):
  cardInfo = request.byNameAndSet(name, set, lang)
  return cardInfo['correctedName']

def mapSpecialCases(name):
  return name.replace(' // ','|')

def mapName(name, set, lang):
  return mapSpecialCases(removeLowerCase(name, set, lang))

def mapSetCode(code):
  if code in SET_CORRECTIONS:
    return SET_CORRECTIONS[code]
  return code

def mapLanguage(index):
  return LANGUAGES[index]
