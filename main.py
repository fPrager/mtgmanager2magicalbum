import file
import mappings

# sample target format
# data = [
#     ['ENG','Alara Reborn','Architects of Will','',2,1,''],	
#     ['EN','Alara Reborn','Arsenal Thresher','',2,0,''],	
#     ['RUS','Alara Reborn','Bant Sojourners','',2,0,'']	
# ]
# 7 columns (Lang, Set, Name, Version, QtyReg, QtyFoil, Notes).


SOURCE_SAMPLE_NAME = 'samples/mtgManger.csv'
TARGET_NAME = 'output.csv'

sourceData = file.readCSV(SOURCE_SAMPLE_NAME)
result = []

for row in sourceData:
  language = mappings.mapLanguage(int(row['Language']))
  code = mappings.mapSetCode(row['Code'])
  name = mappings.mapName(row['Name'], code, language)
  version = mappings.mapVersion(name, code, language)
  foiled = row['Foil'] == '1'
  quantity = row['Quantity']
  qtyReg = quantity if not foiled else 0
  qtyFoiled = quantity if foiled else 0
  
  entry = [language,code, name, version, qtyReg, qtyFoiled, '']
  result.append(entry)

file.writeCSV(TARGET_NAME, result)

