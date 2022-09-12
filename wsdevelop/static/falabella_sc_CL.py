import requests
from datetime import date
import json


def getFalabellaSc():
    categories = [
            ['cat70057',
            'Home > Computación-Notebooks'],
            ['cat5860031',
            'Home > Computación-Notebooks > Notebooks Tradicionales'],
            ['cat2028',
            'Home > Computación-Notebooks Gamers'],
            ['cat2450060',
            'Home > Computación-Notebooks > Notebooks Convertibles 2en1'],
            ['cat15880017',
            'Home > Especiales-Gamer'],
            ['cat5860030',
            'Home > Computación-Notebooks > MacBooks'],
            ['cat4850013',
            'Home > Computación-Computación Gamer'],
            ['cat1012',
            'Home > Tecnología-TV'],
            ['cat7190148',
            'Home > Tecnología-TV > Televisores LED'],
            ['cat11161614',
            'Home > Tecnología-TV > LEDs menores a 50 pulgadas'],
            ['cat11161675',
            'Home > Tecnología-TV > LEDs entre 50 - 55 pulgadas'],
            ['cat11161679',
            'Home > Tecnología-TV > LEDs sobre 55 pulgadas'],
            ['cat2850016',
            'Home > TV-Televisores OLED'],
            ['cat10020021',
            'Home > TV-Televisores QLED'],
            ['cat18110001',
            'Home > Tecnología-Premium'],
            ['cat7230007',
            'Home > Computación-Tablets'],
            ['cat3205',
            'Home > Electrohogar-Línea Blanca > Refrigeradores'],
            ['cat4048',
            'Home > Electrohogar-Línea Blanca > Refrigeradores > Freezers'],
            ['cat4049',
            'Home > Electrohogar-Línea Blanca > Refrigeradores > Frigobar'],
            ['cat4091',
            'Home > Refrigeración-Side by Side'],
            ['cat1820006',
            'Home > Computación-Impresión > Impresoras Multifuncionales'],
            ['cat2049',
            'Home > Tecnología-Computadores > Impresoras'],
            ['cat3151',
            'Home > Microondas'],
            ['cat3114',
            'Home > Electrodomésticos Cocina- Electrodomésticos de cocina > '
            'Hornos Eléctricos'],
            ['cat3025',
            'Home > Electrohogar- Aspirado y Limpieza > Aspiradoras'],
            ['cat3136',
            'Home > Electrohogar-Lavado > Lavado'],
            ['cat4060',
            'Home > Electrohogar-Lavado > Lavadoras'],
            ['cat1700002',
            'Home > Electrohogar-Lavado > Lavadoras-Secadoras'],
            ['cat4088',
            'Home > Electrohogar-Lavado > Secadoras'],
            ['cat1280018',
            'Home > Telefonía- Celulares y Teléfonos > Celulares Básicos'],
            ['cat720161',
            'Home > Telefonía- Celulares y Teléfonos > Smartphones'],
            ['cat70028',
            'Home > Fotografía-Cámaras Compactas'],
            ['cat70029', 
            'Home > Fotografía-Cámaras Semiprofesionales'],
            ['cat2005',
            'Home > Tecnología-Audio'],
            ['cat3091',
            'Home > Tecnología-Audio > Equipos de Música y Karaokes'],
            ['cat3171',
            'Home > Tecnología-Audio > Parlantes Bluetooth'],
            ['cat2045',
            'Home > Tecnología-Audio > Soundbar y Home Theater'],
            ['cat1130010',
            'Home > Audio- Hi-Fi > Tornamesas'],
            ['cat6260041',
            'Home > Día del Niño Chile- Tecnología > Audio > Karaoke'],
            ['cat2032',
            'Home > TV-Blu Ray y DVD'],
            ['cat3087',
            'Home > Computación- Almacenamiento > Discos duros'],
            ['cat3177',
            'Home > Computación- Almacenamiento > Pendrives'],
            ['cat70037',
            'Home > Computación- Accesorios Tecnología > '
            'Accesorios Fotografía > Tarjetas de Memoria'],
            ['cat2070',
            'Home > TV-Proyectores'],
            ['cat3770004',
            'Home > Tecnología- Videojuegos > Consolas'],
            ['cat4440005',
            'Home > Tecnología-Videojuegos > Playstation'],
            ['cat70003',
            'Home > Tecnología-Videojuegos > Nintendo'],
            ['cat4440004',
            'Home > Tecnología-Videojuegos > Xbox'],
            ['cat40051',
            'Home > Computación-All In One'],
            ['cat7830015',
            'Home > Electrohogar- Aire Acondicionado > Portátiles'],
            ['cat7830014',
            'Home > Electrohogar- Aire Acondicionado >Split'],
            ['cat3197',
            'Home > Electrohogar- Aire Acondicionado > Purificadores'],
            ['cat2062',
            'Home > Computación-Monitores'],
            ['cat2013',
            'Home > Electrohogar- Aire Acondicionado > Calefont y Termos'],
            ['cat3155', 
            'Home > Computación- Accesorios Tecnología > '
            'Accesorios Computación > Mouse'],
            ['cat9900007',
            'Home > Electrohogar- Calefacción > Estufas Parafina Láser'],
            ['cat9910024',
            'Home > Electrohogar- Calefacción > Estufas Gas'],
            ['cat9910006',
            'Home > Electrohogar- Calefacción > Estufas Eléctricas'],
            ['cat9910027',
            'Home > Electrohogar- Calefacción > Estufas Pellet y Leña'],
            ['cat4290063',
            'Home > Telefonía- Wearables > SmartWatch'],
            ['cat4730023',
            'Home > Computación- Accesorios Tecnología > '
            'Accesorios Computación > Teclados > Teclados Gamers'],
            ['cat2370002',
            'Home > Computación- Accesorios Tecnología > '
            'Accesorios Computación > Teclados'],
            ['cat2930003',
            'Home > Computación- Accesorios Tecnología > Accesorios TV > '
            'Teclados Smart'],
            ['cat1640002',
            'Home > Tecnología-Audio > Audífonos'],
            ['cat3239',
            'Home > Tecnología-Audio > Parlantes y Subwoofer'],
            ['cat3203',
            'Home > Tecnología-Audio > Hi-Fi'],
            ['cat4061',
            'Home > Lavado-Lavavajillas'],
            ['cat12084890',
            'Home > Tecnología-Computadores > Accesorios Computación > Sillas '
            'Gamer']
        ]

        
    

    stored_data = []
    baseUrl = 'https://www.falabella.com/s/browse/v1/listing/cl?'
    page = 0


    verb = True
    count = 5


    tags = ['Nombre','Items vendidos','Link','Categoría']
    fileName = date.today()


    savedFile = open(str(fileName)+'-falabella.csv','a')
    print(','.join(tags),file=savedFile)
    savedFile.close()

    data = []

    for i in categories:
        print('----====  ',i)
        page = 1
        dataToStore = {}
        while True:
            
            if page > 200:
                print('Page overflow')
                break
            response = requests.get(baseUrl+'zones=ZL_CERRILLOS%2CLOSC%2C130617%2C13&categoryId='+i[0]+'&page='+str(page))
            if(response.status_code == 200):
                
                falabellaResponse = response.json()

                if(falabellaResponse['responseType'] == 'Success'):
                    if(falabellaResponse['data']):
                        if(falabellaResponse['data']['results']):
                            for each_item in falabellaResponse['data']['results']:
                                
                                if(str(each_item['sellerName']).upper() != 'FALABELLA'):
                                    if(str(each_item['sellerName']).upper() in dataToStore):
                                        
                                        dataToStore[str(each_item['sellerName']).upper()][1] =  str(int(dataToStore[str(each_item['sellerName']).upper()][1]) + 1)

                                    elif(str(each_item['sellerName']).upper() not in dataToStore):


                                        dataToStore[str(each_item['sellerName']).upper()] = [str(each_item['sellerName']).upper(),str(1),str('https://www.falabella.com/falabella-cl/seller/'+each_item['sellerName']),str(i).replace(',',';')]
            print(str(i),'________________----')
            page += 1        
        print('page change')
        print(dataToStore)
        for j in dataToStore:
            data.append(dataToStore[j])
    print("SC done.")
    return(data)