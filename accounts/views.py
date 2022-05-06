from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import  User
from django.contrib.auth.decorators import login_required
from .models  import FormContato



def login(request):
    if request.method !='POST':
        return render(request,'accounts/login.html')

    usuario= request.POST.get('usuario')
    senha = request.POST.get('senha')

    user= auth.authenticate(request,username=usuario,password=senha)

    if not user:
        messages.error(request,'Usuario ou senha incorretos')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Login realizado com sucesso.')
        return redirect('dashboard')

def logout(request):
    auth.logout(request)
    return redirect('dashboard')


def cadastro(request):
    if request.method != 'POST':
        return render(request,'accounts/cadastro.html')

    nome= request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha= request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    #verificar se tem algum campo do formulário vazio
    if not nome or not sobrenome or not email or not usuario or not senha or not senha2:
        messages.error(request,'Nenhum campo pode estar vazio')
        return render(request, 'accounts/cadastro.html')

    #valida o email
    try:
        validate_email(email)
    except:
        messages.error(request, 'Email Inválido')
        return render(request, 'accounts/cadastro.html')

    #verifica se o e-mail é maior que 6 caracteres
    if len(senha) < 6:
        messages.error(request, 'Senha precisa ter no mínimo 6 caracteres')
        return render(request, 'accounts/cadastro.html')

    #verifica se as senhas estão corretas
    if senha != senha2:
        messages.error(request, 'A suas senhas estão diferentes')
        return render(request, 'accounts/cadastro.html')

    #verifica se o usuário já existe na base de dados
    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'o usuário já existe')
        return render(request, 'accounts/cadastro.html')

    #verifica se o email já existe na base de dados
    if User.objects.filter(username=email).exists():
        messages.error(request, 'Email já existe')
        return render(request, 'accounts/cadastro.html')

    messages.success(request,'Registrado com sucesso!')


    user=  User.objects.create_user(username=usuario,email=email,password=senha, first_name=nome, last_name=sobrenome)

    user.save()
    return redirect('login')



@login_required(redirect_field_name='login')
def dashboard(request):
    if request.method != 'POST':
        form = FormContato()
        return render(request, 'accounts/dashboard.html', {'form': form})

    form = FormContato(request.POST,request.FILES)

    if not form.is_valid():
        messages.error(request,'ERRO AO ENVIAR FORMULÁRIO')
        form = FormContato(request.POST)
        return render(request, 'accounts/dashboard.html', {'form': form})
    descricao= request.POST.get('descricao')

    if len(descricao) <5 :
        messages.error(request, 'Descrição precisa ter no mínimo 5 caracteres')
        form = FormContato(request.POST)
        return render(request, 'accounts/dashboard.html', {'form': form})
    form.save()
    messages.success(request, f'Contato {request.POST.get("nome")}{request.POST.get("sobrenome")} salvo com sucesso')
    return redirect('dashboard')








