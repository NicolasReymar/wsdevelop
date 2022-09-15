import os
import requests
from datetime import date

def getMeliSc(maxOffset):
  print('meliscPe')

  sellers = []
  categories = []
  baseUrl = 'https://api.mercadolibre.com/sites/MPE/search?limit=50'
  baseCatUrl = 'https://api.mercadolibre.com/sites/MPE/'
  offset = 0
  catResponse  = requests.get(baseCatUrl)
  catResponse = catResponse.json()

  for i in catResponse["categories"]:
    categories.append((i['id'],i['name']))

  tags = ['Id','Nombre','Ciudad','Estado','Tags','Puntuacion','Link','Nivel_vendedor','Transacciones_totales','Transacciones_completadas','Transacciones_canceladas','Rating_positivo','Rating_neutral','Rating_negativo']
  
  data = []

  for i in categories:
      print(i[1],'',end='')
      offset = 0
      while True:
          if offset > round(1000 * (maxOffset/100)):
              print('Page overflow')
              break
          response = requests.get(baseUrl+'&category='+i[0]+'&official_store=all'+'&offset='+str(offset))

          if(response.status_code == 200):
              meliResponse = response.json()
              for j in meliResponse['results']:
                  item = j


                  if(str(item['seller']['id']) not in sellers):
                      try:
                          responseSeller = requests.get('https://api.mercadolibre.com/users/'+str(item['seller']['id']))
                          responseSeller = responseSeller.json()
                          sellers.append(str(item['seller']['id']))
                          dataToStore = [str(responseSeller['id']),responseSeller['nickname'],responseSeller['address']['city'],responseSeller['address']['state']]
                          tags = ''
                          for k in responseSeller['tags']:
                              tags += ';'+str(k)
                          dataToStore.append(tags[1:])
                          dataToStore.append(str(responseSeller['points']))
                          dataToStore.append(str(responseSeller['permalink']))
                          dataToStore.append(str(responseSeller['seller_reputation']['power_seller_status']))
                          dataToStore.append(str(responseSeller['seller_reputation']['transactions']['total']))
                          dataToStore.append(str(responseSeller['seller_reputation']['transactions']['completed']))
                          dataToStore.append(str(responseSeller['seller_reputation']['transactions']['canceled']))
                          dataToStore.append(str(responseSeller['seller_reputation']['transactions']['ratings']['positive']))
                          dataToStore.append(str(responseSeller['seller_reputation']['transactions']['ratings']['neutral']))
                          dataToStore.append(str(responseSeller['seller_reputation']['transactions']['ratings']['negative']))

                          data.append(dataToStore)
                      except:
                          print('skipping ',j)  
                      

          offset += 50
  return data

