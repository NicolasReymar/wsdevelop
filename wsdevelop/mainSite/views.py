from glob import escape
from django.http import HttpResponse
from django.shortcuts import render
import os

# Create your views here.
TEMPLATE_DIRS = {
  'os.path.join(BASE_DIR, "templates"),'
}



def basePage(request):
  dataToShow = [['550063615', 'MERCADOLIBRE ELECTRONICA_CL', 'Las Condes', 'METROPOLITANA', 'brand;large_seller;mshops', '8216', 'http://perfil.mercadolibre.cl/MERCADOLIBRE+ELECTRONICA_CL', 'platinum', '254957', '237800', '17157', '0.92', '0.02', '0.06'], ['385845686', 'MISTORECHILE', 'Las Condes', 'METROPOLITANA', 'brand;large_seller', '2661', 'http://perfil.mercadolibre.cl/MISTORECHILE', 'platinum', '36756', '34651', '2105', '0.87', '0.04', '0.09'], ['418010336', 'TIENDASOFICIALESIM', 'Quillota', 'CL-VS', 'brand;large_seller;eshop;mshops', '5497', 'http://perfil.mercadolibre.cl/TIENDASOFICIALESIM', 'platinum', '45719', '43645', '2074', '0.91', '0.03', '0.06'], ['301258112', 'ADMINISTRADORA ADP', 'Pudahuel', 'METROPOLITANA', 'brand;large_seller;eshop;mshops', '10545', 'http://perfil.mercadolibre.cl/ADMINISTRADORA+ADP', 'platinum', '97449', '91571', '5878', '0.88', '0.03', '0.09'], ['305330042', 'ELECTRONICAGAMER', 'Santiago', 'CL-RM', 'brand;large_seller', '1851', 'http://perfil.mercadolibre.cl/ELECTRONICAGAMER', 'platinum', '5709', '5315', '394', '0.9', '0.03', '0.07'], ['236292130', 'MOBILEHUT', 'Santiago', 'METROPOLITANA', 'brand;large_seller;eshop;mshops', '19931', 'http://perfil.mercadolibre.cl/MOBILEHUT', 'platinum', '74228', '70118', '4110', '0.94', '0.02', '0.04'], ['700043984', 'RADIOVICTORIATCLCHILESPARA', 'Pudahuel', 'METROPOLITANA', 'brand;large_seller;mshops', '336', 'http://perfil.mercadolibre.cl/RADIOVICTORIATCLCHILESPARA', 'platinum', '8347', '7654', '693', '0.85', '0.05', '0.1'], ['1169010278', 'COCO5153227', 'Providencia', 'CL-RM', 'brand;large_seller;mshops', '0', 'http://perfil.mercadolibre.cl/COCO5153227', 'None', '157', '147', '10', '0', '1', '0'], ['271947391', 'MOWSTORE', 'Vitacura', 'CL-RM', 'brand;large_seller;mshops', '1338', 'http://perfil.mercadolibre.cl/MOWSTORE', 'platinum', '11418', '11003', '415', '0.96', '0.02', '0.02'], ['502576083', 'CUBO24', 'Las Condes', 'CL-RM', 'brand;large_seller;eshop', '123', 'http://perfil.mercadolibre.cl/CUBO24', 'platinum', '923', '851', '72', '0.97', '0.01', '0.02'], ['809231755', 'ELEL98543', 'Cerrillos', 'CL-RM', 'brand;large_seller', '65', 'http://perfil.mercadolibre.cl/ELEL98543', 'platinum', '10729', '10210', '519', '0.9', '0.01', '0.09'], ['1086025078', 'RMCOMMUNICATIONSSPARMCOMMUN', 'Las Condes', 'CL-RM', 'brand;large_seller;mshops', '2', 'http://perfil.mercadolibre.cl/RMCOMMUNICATIONSSPARMCOMMUN', 'silver', '72', '66', '6', '1', '0', '0'], ['330176422', 'REUSE CL', 'Providencia', 'METROPOLITANA', 'brand;large_seller;eshop;mshops', '55', 'http://perfil.mercadolibre.cl/REUSE+CL', 'platinum', '478', '419', '59', 
'0.93', '0.03', '0.04'], ['433323657', 'HP TIENDAOFICIAL', 'Pudahuel', 'METROPOLITANA', 'brand;large_seller', '3230', 'http://perfil.mercadolibre.cl/HP+TIENDAOFICIAL', 'platinum', '43825', '41763', '2062', '0.78', '0.06', '0.16'], ['252227874', 'ACER STORE', 'Colina', 'CL-RM', 'brand;large_seller;mshops', '2758', 'http://perfil.mercadolibre.cl/ACER+STORE', 'platinum', '5703', '5234', '469', '0.94', 
'0.03', '0.03'], ['499658570', 'LOGITECH OFICIAL', 'Maipú', 'CL-RM', 'brand;large_seller;mshops', '1968', 'http://perfil.mercadolibre.cl/LOGITECH+OFICIAL', 'platinum', '18213', '17312', '901', '0.91', 
'0.02', '0.07'], ['541487032', 'AC3132916', 'Las Condes', 'METROPOLITANA', 'brand;large_seller;mshops', '412', 'http://perfil.mercadolibre.cl/AC3132916', 'platinum', '2844', '2736', '108', '0.9', '0.04', '0.06'], ['404495030', 'ECOMSUR', 'Pudahuel', 'METROPOLITANA', 'brand;large_seller;mshops', '14706', 'http://perfil.mercadolibre.cl/ECOMSUR', 'None', '34293', '25375', '8918', '0.61', '0.07', '0.32'], ['1021060004', 'REDELCOM', 'Providencia', 'CL-RM', 'brand;large_seller;mshops', '6', 'http://perfil.mercadolibre.cl/REDELCOM', 'platinum', '1256', '1213', '43', '0.78', '0.14', '0.08'], ['114674801', 'ANKERSTORE', 'Pudahuel', 'CL-RM', 'brand;large_seller;mshops', '7637', 'http://perfil.mercadolibre.cl/ANKERSTORE', 'platinum', '25347', '24313', '1034', '0.95', '0.03', '0.02'], ['585708375', 'REDRAGON_TIENDA', 'Maipú', 'CL-RM', 'brand;large_seller', '650', 'http://perfil.mercadolibre.cl/REDRAGON_TIENDA', 'platinum', '5639', '5348', '291', '0.9', '0.02', '0.08'], ['476415131', 'OFFICIALSTORES', 'Las Condes', 'CL-RM', 'brand;large_seller', '189', 'http://perfil.mercadolibre.cl/OFFICIALSTORES', 'platinum', '1733', '1576', '157', '0.84', '0.08', '0.08'], ['294848523', 'MACROTEL TO', 'Huechuraba', 'CL-RM', 'brand;large_seller', '2617', 'http://perfil.mercadolibre.cl/MACROTEL+TO', 'platinum', '3142', '2946', '196', '0.87', '0.05', '0.08'], ['336248267', 'IMPORTADORAVICTORIACAPITALLT', 'Renca', 'CL-RM', 'brand;large_seller', '1795', 'http://perfil.mercadolibre.cl/IMPORTADORAVICTORIACAPITALLT', 'platinum', '23832', '22425', '1407', '0.91', '0.04', '0.05'], ['450662449', 'HEAD CHILE', 'El Belloto', 'CL-VS', 'brand;large_seller;eshop', '1483', 'http://perfil.mercadolibre.cl/HEAD+CHILE', 'platinum', '32548', '30538', '2010', '0.92', '0.02', '0.06'], ['269961502', 'MAXELL CHILE', 'Santiago', 'METROPOLITANA', 'brand;large_seller;eshop', '2462', 'http://perfil.mercadolibre.cl/MAXELL+CHILE', 'platinum', '6927', '6652', '275', '0.97', '0.02', '0.01'], ['348386320', 'LENOVOAGENCIAENCHILE', 'Las Condes', 'CL-RM', 'brand;large_seller', '216', 'http://perfil.mercadolibre.cl/LENOVOAGENCIAENCHILE', 'gold', '2487', '2288', '199', '0.87', '0.04', '0.09'], ['353806922', 'HUION-OFFICIAL-STORE CHILE', 'Providencia', 'CL-RM', 'brand;large_seller', '352', 'http://perfil.mercadolibre.cl/HUION-OFFICIAL-STORE+CHILE', 'silver', '2091', '1996', '95', '0.95', '0.01', '0.04'], ['1086991077', 'RAZER OFICIAL', 'Santiago', 'CL-RM', 'brand;large_seller;mshops', '3', 'http://perfil.mercadolibre.cl/RAZER+OFICIAL', 'platinum', '384', '364', '20', '1', '0', '0'], ['736808452', 'BUBBACHILESPABUBBACHILESPA', 'Lo Barnechea', 'CL-RM', 'brand;large_seller', '106', 'http://perfil.mercadolibre.cl/BUBBACHILESPABUBBACHILESPA', 'platinum', '14597', '14012', '585', '0.96', '0', '0.04'], ['589019446', 'BLIKTECHNICA', 'Lampa', 'CL-RM', 'brand;large_seller', '617', 'http://perfil.mercadolibre.cl/BLIKTECHNICA', 'platinum', '6942', '6497', '445', '0.9', '0.02', '0.08'], ['543504573', 'CAIXUN', 'San Bernardo', 'CL-RM', 'brand;large_seller', '683', 'http://perfil.mercadolibre.cl/CAIXUN', 'platinum', '10639', '9896', '743', '0.91', '0.04', '0.05'], ['177969871', '-SONY CHILE', 'Pudahuel', 'CL-RM', 'brand;large_seller', '10804', 'http://perfil.mercadolibre.cl/-SONY+CHILE', 'platinum', '45246', '42693', '2553', '0.91', '0.04', '0.05'], ['1139856127', 'JUEGOSDEVIDEODECHILESPAJU', 'Las Condes', 'CL-RM', 'brand;large_seller', 
'1', 'http://perfil.mercadolibre.cl/JUEGOSDEVIDEODECHILESPAJU', 'None', '95', '92', '3', '1', '0', '0'], ['1118543211', 'TPVCHILESPA', 'Pudahuel', 'CL-RM', 'brand;large_seller', '0', 'http://perfil.mercadolibre.cl/TPVCHILESPA', 'None', '990', '934', '56', '0.5', '0', '0.5'], ['231203596', 'SUPERSTORE.OFICIAL', 'Temuco', 'CL-AR', 'brand;large_seller;eshop;mshops', '1014', 'http://perfil.mercadolibre.cl/SUPERSTORE.OFICIAL', 'platinum', '23985', '23313', '672', '0.97', '0.02', '0.01'], ['359525873', 'GASEI S.A.', 'Huechuraba', 'CL-RM', 'brand;large_seller', '1801', 'http://perfil.mercadolibre.cl/GASEI+S.A.', 'platinum', '22594', '21278', '1316', '0.86', '0.03', '0.11'], ['379965148', 'FOTOGRAFICAFORESTIERSA', 'Huechuraba', 'CL-RM', 'brand;large_seller;mshops', '874', 'http://perfil.mercadolibre.cl/FOTOGRAFICAFORESTIERSA', 'platinum', '13254', '12689', '565', '0.92', '0.03', '0.05'], ['282301884', 'DJI OFICIAL', 'Providencia', 'CL-RM', 'brand;large_seller', '657', 'http://perfil.mercadolibre.cl/DJI+OFICIAL', 'None', '4799', '4451', '348', '0.94', '0.03', '0.03'], ['568368994', 'SOLUTIONS2GO', 'Pudahuel', 'CL-RM', 'brand;large_seller', '268', 'http://perfil.mercadolibre.cl/SOLUTIONS2GO', 'platinum', '10936', '10370', '566', '0.86', '0.05', '0.09'], ['226369160', 'ONLINECLUB.TO', 'La Florida', 'CL-RM', 'brand;large_seller;eshop;mshops', '12778', 'http://perfil.mercadolibre.cl/ONLINECLUB.TO', 'platinum', '143735', '139075', '4660', '0.92', '0.02', '0.06'], ['586576821', 'EMATCHSPAEMATCHSPA', 'Renca', 'CL-RM', 'brand;large_seller;mshops', '353', 'http://perfil.mercadolibre.cl/EMATCHSPAEMATCHSPA', 'platinum', '62259', '59819', '2440', '0.95', '0.02', '0.03'], ['410952794', 'TUHOME CHILE', 'San Bernardo', 'METROPOLITANA', 'brand;large_seller;eshop;mshops', '4056', 'http://perfil.mercadolibre.cl/TUHOME+CHILE', 'platinum', '5969', '5640', '329', '0.94', '0.04', '0.02'], ['668300945', 'MOSAICO S.A', 'Colina', 'CL-RM', 'brand;large_seller;mshops', '45', 'http://perfil.mercadolibre.cl/MOSAICO+S.A', 'platinum', '4780', '4523', '257', '0.72', '0.07', '0.21'], ['394820259', 'FORM DESIGN', 'Pudahuel', 'CL-RM', 'brand;large_seller;eshop', '1551', 'http://perfil.mercadolibre.cl/FORM+DESIGN', 'platinum', '4988', '4512', '476', '0.93', '0.05', '0.02'], ['493446659', 'TORK FULLKOM', 'Lampa', 'CL-RM', 'brand;large_seller;mshops', '515', 'http://perfil.mercadolibre.cl/TORK+FULLKOM', 'platinum', 
'9913', '9719', '194', '0.95', '0.02', '0.03'], ['279737632', 'GRUPOBECASPA', 'Pudahuel', 'CL-RM', 'brand;large_seller', '1407', 'http://perfil.mercadolibre.cl/GRUPOBECASPA', 'platinum', '12703', '12053', '650', '0.88', '0.04', '0.08'], ['824507017', 'TIENDAMERCADAZOCHILE', 'Quilicura', 'METROPOLITANA', 'brand;large_seller', '209', 'http://perfil.mercadolibre.cl/TIENDAMERCADAZOCHILE', 'platinum', '1875', '1777', '98', '0.96', '0.03', '0.01'], ['140485081', 'PUNTARANCO SPA', 'Vitacura', 'CL-RM', 'brand;large_seller;eshop;mshops', '1665', 'http://perfil.mercadolibre.cl/PUNTARANCO+SPA', 'platinum', 
'2985', '2780', '205', '0.89', '0.07', '0.04'], ['454915851', 'VIRUTEX ILKO', 'Cerrillos', 'CL-RM', 'brand;large_seller', '892', 'http://perfil.mercadolibre.cl/VIRUTEX+ILKO', 'platinum', '25064', '24256', '808', '0.91', '0.02', '0.07'], ['280236845', 'UNILEVER TOUCH', 'Las Condes', 'CL-RM', 'brand;large_seller', '764', 'http://perfil.mercadolibre.cl/UNILEVER+TOUCH', 'platinum', '40756', '38475', '2281', '0.86', '0.02', '0.12'], ['451305548', 'CEM OFICIAL', 'Estacion Central', 'CL-RM', 'brand;large_seller;mshops', '1038', 'http://perfil.mercadolibre.cl/CEM+OFICIAL', 'platinum', '10044', '9284', '760', '0.84', '0.07', '0.09'], ['225024072', 'OSTER CHILE', 'Pudahuel', 'METROPOLITANA', 'brand;large_seller', '3986', 'http://perfil.mercadolibre.cl/OSTER+CHILE', 'platinum', '46057', '44376', '1681', 
'0.85', '0.04', '0.11'], ['662520848', 'GROUPESEB CHILE', 'Renca', 'CL-RM', 'brand;large_seller;mshops', '364', 'http://perfil.mercadolibre.cl/GROUPESEB+CHILE', 'platinum', '19457', '18570', '887', '0.77', '0.05', '0.18'], ['404609800', 'COMEINDSTROLLERLTDA', 'Quilicura', 'CL-RM', 'brand;large_seller;mshops', '1673', 'http://perfil.mercadolibre.cl/COMEINDSTROLLERLTDA', 'platinum', '27977', '26164', 
'1813', '0.75', '0.11', '0.14'], ['228531702', 'TIENDASOFICIALESMDS', 'Pudahuel', 'CL-RM', 'brand;large_seller;mshops', '5447', 'http://perfil.mercadolibre.cl/TIENDASOFICIALESMDS', 'platinum', '25346', '23776', '1570', '0.83', '0.05', '0.12'], ['775481601', 'ENERGECTIC SPA', 'Colina', 'CL-RM', 'brand;large_seller;mshops', '58', 'http://perfil.mercadolibre.cl/ENERGECTIC+SPA', 'platinum', '5166', '4916', '250', '1', '0', '0'], ['637886696', 'RECKITTB', 'Colina', 'CL-RM', 'brand;large_seller', '142', 'http://perfil.mercadolibre.cl/RECKITTB', 'platinum', '15608', '14889', '719', '0.86', '0.04', '0.1'], ['761293225', 'CAMBIASOHNOS', 'Valparaiso', 'CL-VS', 'brand;large_seller', '119', 'http://perfil.mercadolibre.cl/CAMBIASOHNOS', 'platinum', '41019', '39441', '1578', '0.98', '0.02', '0'], ['1093409314', 'DEMARIAIGENIX', 'Renca', 'CL-RM', 'brand;large_seller', '17', 'http://perfil.mercadolibre.cl/DEMARIAIGENIX', 'platinum', '5813', '5472', '341', '1', '0', '0'], ['606228917', 'ELITE PROFESSIONAL', 'Renca', 'CL-RM', 'brand;large_seller', '271', 'http://perfil.mercadolibre.cl/ELITE+PROFESSIONAL', 'platinum', '9736', '9429', '307', '0.9', '0.05', '0.05'], ['494183906', 'SBD CHILE', 'Pudahuel', 'METROPOLITANA', 'brand;large_seller;mshops', '9660', 'http://perfil.mercadolibre.cl/SBD+CHILE', 'platinum', '157972', '148566', '9406', '0.77', '0.03', '0.2'], ['543841678', 'THERMOS CL', 'Huechuraba', 'CL-RM', 'brand;large_seller;mshops', '235', 'http://perfil.mercadolibre.cl/THERMOS+CL', 'platinum', '17358', '15133', '2225', '0.55', '0.04', '0.41'], ['582484584', 'GAMA OFICIAL', 'Huechuraba', 'CL-RM', 'brand;large_seller', '1509', 'http://perfil.mercadolibre.cl/GAMA+OFICIAL', 'platinum', '20829', '19984', '845', '0.98', '0', '0.02'], ['600275643', 'COMERCIALIZADORALOSROBLESLT', 'San Bernardo', 'CL-RM', 'brand;large_seller', '3384', 'http://perfil.mercadolibre.cl/COMERCIALIZADORALOSROBLESLT', 'platinum', '80112', '77015', '3097', '0.91', '0.02', '0.07'], ['656540155', 'EMEM1147861', 'Providencia', 'CL-RM', 'brand;large_seller;eshop;mshops', '768', 'http://perfil.mercadolibre.cl/EMEM1147861', 'None', '6684', '6219', '465', '0.81', '0.13', '0.06'], ['538990655', 'PL MLC', 'Las Condes', 'METROPOLITANA', 'brand;large_seller', '3745', 'http://perfil.mercadolibre.cl/PL+MLC', 'platinum', '154808', '148772', '6036', '0.95', '0.02', '0.03'], ['1105795065', 'BLANIK OFICIAL', 'Colina', 'CL-RM', 'brand;large_seller', '3', 'http://perfil.mercadolibre.cl/BLANIK+OFICIAL', 'platinum', '3210', '3105', '105', '0.61', '0.13', '0.26'], ['823673932', 'SUPERMERCADOS CHILE', 'Pudahuel', 'CL-RM', 'brand;large_seller', '164', 'http://perfil.mercadolibre.cl/SUPERMERCADOS+CHILE', 'platinum', '53162', '50312', '2850', '0.98', '0.01', '0.01'], ['649528682', 'KITCHENCENTERSPAKITCHENCENT', 'Recoleta', 'CL-RM', 'brand;large_seller', '523', 'http://perfil.mercadolibre.cl/KITCHENCENTERSPAKITCHENCENT', 'gold', '1851', '1718', '133', '0.85', '0.09', '0.06'], ['325982945', 'SACTI', 'Maipú', 'METROPOLITANA', 'brand;large_seller', '40084', 'http://perfil.mercadolibre.cl/SACTI', 'platinum', '87966', '83046', '4920', '0.85', '0.08', '0.07'], ['234945806', 'DORELJUVENILECHILE', 'Pudahuel', 'METROPOLITANA', 'brand;large_seller', '6596', 'http://perfil.mercadolibre.cl/DORELJUVENILECHILE', 'platinum', '20597', '19672', '925', '0.85', '0.08', '0.07'], ['1043860603', 'THECLOROXCOMPANYCHILE', 'Renca', 'CL-RM', 'brand;large_seller', '35', 'http://perfil.mercadolibre.cl/THECLOROXCOMPANYCHILE', 'platinum', '7612', '7105', '507', '0.96', '0', '0.04'], ['498638501', 'ASSA ABLOY', 'Pudahuel', 'CL-RM', 'brand;large_seller;mshops', '373', 'http://perfil.mercadolibre.cl/ASSA+ABLOY', 'platinum', '6586', '6257', '329', '0.86', '0.03', '0.11'], ['393546577', 'CASAMARILLA1920', 'Vitacura', 'CL-RM', 'brand;large_seller;mshops', 
'610', 'http://perfil.mercadolibre.cl/CASAMARILLA1920', 'platinum', '5826', '5593', '233', '0.9', '0.04', '0.06'], ['376182641', 'BOYA CHILE', 'Providencia', 'CL-RM', 'brand;large_seller;mshops', '355', 'http://perfil.mercadolibre.cl/BOYA+CHILE', 'platinum', '2332', '2195', '137', '0.97', '0.02', '0.01'], ['237931934', 'MUSICWORLDCHILE', 'Quilicura', 'CL-RM', 'brand;large_seller;mshops', '1429', 'http://perfil.mercadolibre.cl/MUSICWORLDCHILE', 'platinum', '1776', '1675', '101', '0.98', '0.01', '0.01'], ['259865773', 'MARCOMTECHSPA', 'Ñuñoa', 'CL-RM', 'brand;large_seller', '1410', 'http://perfil.mercadolibre.cl/MARCOMTECHSPA', 'gold', '1146', '1109', '37', '0.98', '0.02', '0'], ['808126285', 'CONSULTORASOLVENETCHILESPAC', 'Colina', 'CL-RM', 'brand;large_seller', '0', 'http://perfil.mercadolibre.cl/CONSULTORASOLVENETCHILESPAC', 'silver', '55', '51', '4', '0', '1', '0'], ['356755452', 'DISCOVERY ADVENTURES', 'Las Condes', 'CL-RM', 'brand;large_seller', '633', 'http://perfil.mercadolibre.cl/DISCOVERY+ADVENTURES', 'platinum', '8783', '8194', '589', '0.92', '0.01', '0.07'], ['238578600', 'INVERSIONESVALRODLTDA', 'San Joaquín', 'CL-RM', 'brand;large_seller;eshop;mshops', '1823', 'http://perfil.mercadolibre.cl/INVERSIONESVALRODLTDA', 'platinum', '9778', '9385', '393', '0.97', '0.02', '0.01'], ['235629627', 'SOYMOMO', 'Providencia', 'CL-RM', 'brand;large_seller;eshop;mshops', '227', 'http://perfil.mercadolibre.cl/SOYMOMO', 'None', '4985', '4647', '338', '0.87', '0.04', '0.09']]

  table_content = '''<tr>'''
  for i in dataToShow:
    table_content += '''<td>{}</td>
                        <td>{}</td>
                        <td>{}</td>
                        <td>{}</td>
                        <td>{}</td>
                        <td>{}</td>
                        <td>{}</td>
                        </tr>
                        '''.format(i[0],i[1],i[3],i[5],i[6],i[7],i[8])
  table_content += ''

  return render(request,'index.html',context={'table_content' : table_content} )



def falabellaPage(request):
  dataToShow = {'HP TIENDA OFICIAL': ['HP TIENDA OFICIAL', '7', 'https://www.falabella.com/falabella-cl/seller/HP Tienda Oficial', "['cat70057'; 'Home > Computación-Notebooks']"], 'BOOKCOMPUTER': ['BOOKCOMPUTER', '23', 'https://www.falabella.com/falabella-cl/seller/Bookcomputer', "['cat70057'; 'Home > Computación-Notebooks']"], 'LENOVO AGENCIA EN CHILE': ['LENOVO AGENCIA EN CHILE', '1', 'https://www.falabella.com/falabella-cl/seller/LENOVO AGENCIA EN CHILE', "['cat70057'; 'Home > Computación-Notebooks']"], 'CINTEGRAL': ['CINTEGRAL', '2', 'https://www.falabella.com/falabella-cl/seller/Cintegral', "['cat70057'; 'Home > Computación-Notebooks']"], 'REUSE': ['REUSE', '10', 'https://www.falabella.com/falabella-cl/seller/REUSE', "['cat70057'; 'Home > Computación-Notebooks']"], 'REPARACIONES BBCC LIMITADA': ['REPARACIONES BBCC LIMITADA', '1', 'https://www.falabella.com/falabella-cl/seller/REPARACIONES BBCC LIMITADA', "['cat70057'; 'Home > Computación-Notebooks']"], 'OPC STORE': ['OPC STORE', '17', 'https://www.falabella.com/falabella-cl/seller/OPC STORE', "['cat70057'; 'Home > Computación-Notebooks']"], 'ESPEX': ['ESPEX', '5', 'https://www.falabella.com/falabella-cl/seller/Espex', "['cat70057'; 'Home > Computación-Notebooks']"], 'TOTTUS': ['TOTTUS', '1', 'https://www.falabella.com/falabella-cl/seller/TOTTUS', "['cat70057'; 'Home > Computación-Notebooks']"], 'SAN PABLO TI LIMITADA': ['SAN PABLO TI LIMITADA', '1', 'https://www.falabella.com/falabella-cl/seller/San Pablo TI Limitada', "['cat70057'; 'Home > Computación-Notebooks']"], 'TIENDA OFICIAL LENOVO': ['TIENDA OFICIAL LENOVO', '4', 'https://www.falabella.com/falabella-cl/seller/TIENDA OFICIAL LENOVO', "['cat70057'; 'Home > Computación-Notebooks']"], 'IMPORTADORA Y COMERCIAL MALAGA SPA': ['IMPORTADORA Y COMERCIAL MALAGA SPA', '1', 'https://www.falabella.com/falabella-cl/seller/IMPORTADORA Y COMERCIAL MALAGA SPA', "['cat70057'; 'Home > Computación-Notebooks']"], 'SODIMAC': ['SODIMAC', '18', 'https://www.falabella.com/falabella-cl/seller/SODIMAC', 
"['cat70057'; 'Home > Computación-Notebooks']"], 'ECOIN DIGITAL': ['ECOIN DIGITAL', '1', 'https://www.falabella.com/falabella-cl/seller/ECOIN DIGITAL', "['cat70057'; 'Home > Computación-Notebooks']"], 
'EXPERIMAX': ['EXPERIMAX', '3', 'https://www.falabella.com/falabella-cl/seller/EXPERIMAX', "['cat70057'; 'Home > Computación-Notebooks']"], 'MRICK CHILE': ['MRICK CHILE', '1', 'https://www.falabella.com/falabella-cl/seller/MRICK CHILE', "['cat70057'; 'Home > Computación-Notebooks']"], 'ADVANTAGE COMPUTACION LIMITADA          ': ['ADVANTAGE COMPUTACION LIMITADA          ', '3', 'https://www.falabella.com/falabella-cl/seller/Advantage computacion limitada          ', "['cat70057'; 'Home > Computación-Notebooks']"], 'ECOIN': ['ECOIN', '3', 'https://www.falabella.com/falabella-cl/seller/ECOIN', "['cat70057'; 'Home > Computación-Notebooks']"], 'ADVANTAGE COMPUTACION LIMITADA': ['ADVANTAGE COMPUTACION LIMITADA', '1', 'https://www.falabella.com/falabella-cl/seller/Advantage computacion limitada', "['cat70057'; 'Home > Computación-Notebooks']"], 'COMERCIAL G': ['COMERCIAL G', '1', 'https://www.falabella.com/falabella-cl/seller/COMERCIAL G', "['cat70057'; 'Home > Computación-Notebooks']"], 'ECOTEA CHILE SPA': ['ECOTEA CHILE SPA', '1', 'https://www.falabella.com/falabella-cl/seller/Ecotea Chile Spa', "['cat70057'; 'Home > Computación-Notebooks']"]}
  
  table_content = '''<tr>'''
  for i in dataToShow:
    table_content += '''<td>{}</td>
                        <td>{}</td>
                        <td>{}</td>
                        <td>{}</td>
                        </tr>
                        '''.format(i[dataToShow][0],i[dataToShow][1],i[dataToShow][2],i[dataToShow][3])
  table_content += ''

  return render(request,'falabellaPage.html',context={'table_content' : table_content} )