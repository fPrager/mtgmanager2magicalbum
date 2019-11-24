import csv

def read(name):
  f = open(name, 'r')
  data = f.read()
  f.close()
  return data

def write(name, data):
  f = open(name, 'w')
  f.write(data)
  f.close()
  
def readCSV(name):
  f = open(name, mode='r')
  reader = csv.DictReader(f)
  return reader

def writeCSV(name, data):
  f = open(name,'w', newline='\n', encoding='utf-16-le')
  writer = csv.writer(f,  delimiter='\t')
  writer.writerows(data)
  f.close()

  # read wrong formatted file
  f = open(name, 'rb')
  data = f.read()
  f.close()

  # append missing start bytes FF and FE
  f = open(name, 'wb')
  f.write(bytearray(b'\xFF\xFE') + data)
  f.close()