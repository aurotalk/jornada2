from django.shortcuts import render
from tuites.models import Tuite


def post_tuite(request):
    context = {}
    if request.method == 'POST':
        print('Enviando formulário!!')
        content = request.POST.get('content', None)
        print(content)
        if content == '' or content == ' ':
            context['error']= 'Tuite nao pode ta vazxio'
        else:
            tuite = Tuite.objects.create(
                content = content,
                author = request.user,             
            )
            context['sucess_message'] = f'Seu Tuite de "{tuite.content}" conteúdo foi enviado'
        
    return render(request, 'post_tuite.html', context)