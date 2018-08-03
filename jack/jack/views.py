from django.http import HttpResponse


def hello(request):
    return HttpResponse('Olá')


def articles(request, year):
    return HttpResponse('O ano enviado foi: '+str(year))

def lerDoBanco(nome):
    listanomes =[
        {'nome': 'breno','idade': 19},
         {'nome': 'brenda','idade': 25},
          {'nome': 'claudio','idade': 47},
           {'nome': 'iraci','idade': 50},
    ]
    for pessoa in listanomes:
        if pessoa['nome'] == nome:
            return pessoa
    else:
        return {'nome': 'Não econtrada', 'idade': 0}

def fname(request, nome):
    result = lerDoBanco(nome)
    print(result)
    if result['idade'] > 0:
        return HttpResponse('A pessoa foi encontrada, ela tem ' + str(result['idade'])+' anos')
    else:
        return HttpResponse('Pessoa não encontrada')

