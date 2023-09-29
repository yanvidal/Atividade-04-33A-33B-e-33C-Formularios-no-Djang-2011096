from django.shortcuts import render, redirect
from .models import Jogos, Jogadores


# Create your views here.
def home(request):
    times = Jogos.objects.all()
    jogadores = Jogadores.objects.all()
    print(jogadores)
    print(times)
    return render(request,
                  "home.html",
                  context={
                      "jogadores": jogadores,
                      "jogos": times
                  })


def create_jogo(request):
    if request.method == "POST":
        #criar um novo jogo usando os valores do formulário
        print(request.POST)
        Jogos.objects.create(times=request.POST["times"],
                             placar=request.POST["placar"],
                             situacao=request.POST["situacao"],
                             release_date=request.POST["release_date"])

        return redirect("home")
    return render(request, "forms.html")


def update_jogo(request, id):
    jogo = Jogos.objects.get(id=id)
    print(jogo.times)
    if request.method == "POST":
        #criar um novo jogo usando os valores do formulário
        jogo.times = request.POST["times"]
        jogo.placar = request.POST["placar"]
        jogo.situacao = request.POST["situacao"]
        jogo.release_date = request.POST["release_date"]
        jogo.save()
        return redirect("home")
    return render(request,
                  "forms.html",
                  context={
                      "type": "Atualizar",
                      "jogo": jogo
                  })


def delete_jogo(request, id):
    jogo = Jogos.objects.get(id=id)
    print(jogo.times)
    if request.method == "POST":
        #criar um novo jogo usando os valores do formulário
        jogo.delete()

        return redirect("home")
    return render(request, "areyousure.html", context={"jogo": jogo})


def create_jogadores(request):
  if request.method == "POST":
    #criar um novo jogo usando os valores do formulário
    print(request.POST)
    Jogadores.objects.create(jogadores=request.POST["jogadores"],
                             frequencia=request.POST["frequencia"],
                             posicao=request.POST["posicao"],
                             gols=request.POST["gols"])
    return redirect("home")
  
  frequencia = Jogadores.frequencia.field.choices
  posicao = Jogadores.posicao.field.choices
  return render(request, "forms2.html",context={
              "frequencia": frequencia,
              "posicao": posicao,
            })


def update_jogadores(request, id):
    jogador = Jogadores.objects.get(id=id)
    print(jogador.jogadores)
    if request.method == "POST":
        #criar um novo jogo usando os valores do formulário
        jogador.jogadores = request.POST["jogadores"]
        jogador.frequencia = request.POST["frequencia"]
        jogador.posicao = request.POST["posicao"]
        jogador.gols = request.POST["gols"]
        jogador.save()
        return redirect("home")
    frequencia = Jogadores.frequencia.field.choices
    posicao = Jogadores.posicao.field.choices
    return render(request,
                  "forms2.html",
                  context={
                    "type": "Atualizar",
                    "jogador": jogador,
                    "frequencia": frequencia,
                    "posicao": posicao,
                  })


def delete_jogadores(request, id):
    jogador = Jogadores.objects.get(id=id)
    print(jogador.jogadores)
    if request.method == "POST":
        #criar um novo jogo usando os valores do formulário
        jogador.delete()
        return redirect("home")
    return render(request, "forms2.html", context={"jogador": jogador})
