from django.shortcuts import render
from tuites.models import Tuite
from django.views.generic import CreateView
from django.urls import reverse_lazy
from tuites.forms import PostTuiteForm
from django.contrib.auth.mixins import LoginRequiredMixin



class PostTuiteView(LoginRequiredMixin, CreateView):
    model = Tuite
    template_name = 'post_tuite.html'
    form_class = PostTuiteForm
    success_url = reverse_lazy('post_tuite')

    def get_initial(self):
        return {
            'user': self.request.user
        }

    def form_valid(self, form):
        messages.sucess(
            self.request,
            'Voce postou tuite'
        )
        return super().form_valid(form)



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