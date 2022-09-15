from glob import escape
from multiprocessing import context
from pickle import TRUE
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
import os
from static import meli_sc_CL,meli_sc_PE,falabella_sc_CL

# Create your views here.
TEMPLATE_DIRS = {
  'os.path.join(BASE_DIR, "templates"),'
}


def index(request):
  return render(request,'index.html')

def meliPage(request):
  print('mpage')

  if(request.method == "GET"):
    try:
      country = request.GET['country']
    except:
      print('no country')
      country = 'NA'

    execute_function = request.GET.get('execute_function')
    range = request.GET.get('range')

    if(execute_function == 'TRUE' and range):
      
      if(country == 'CL'):
        print('dtsh1')
        dataToShow = meli_sc_CL.getMeliSc(int(range))
      elif(country == 'PE'):
        print('dtsh2')
        dataToShow = meli_sc_PE.getMeliSc(int(range))
      else:
        print('dtsh3')
        dataToShow = ''

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
    else:
      table_content=''
  return render(request,'meliPage.html',context={'table_content' : table_content,'country':country})



def falabellaPage(request):

  if(request.method == "GET"):
    try:
      country = request.GET['country']
    except:
      print('no country')
      country = 'NA'

    execute_function = request.GET.get('execute_function')
    print('execute_function = ',execute_function)
    print('country = ',country)
    range = request.GET.get('range')
    if(execute_function == 'TRUE' and country == 'CL'):
      dataToShow = falabella_sc_CL.getFalabellaSc(int(range))

      table_content = '''<tr>'''
      for i in dataToShow:
        table_content += '''<td>{}</td>
                            <td>{}</td>
                            <td>{}</td>
                            <td>{}</td>
                            </tr>
                            '''.format(i[0],i[1],i[2],i[3])
      table_content += ''
    else:
      table_content = ''
  return render(request,'falabellaPage.html',context={'table_content' : table_content,'country':country})

def scTool(request):
  if(request.method == "GET"):
    try:
      country = request.GET['country']
    except:
      print('no country')
      country = 'NA'
  return render(request,'scTool.html',context = {'country':country})