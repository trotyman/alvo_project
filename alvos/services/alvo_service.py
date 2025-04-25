from alvos.models.alvo import Alvo

def get_todos_os_alvos():
    return Alvo.objects.all()

def criar_alvo(**dados):
    return Alvo.objects.create(**dados)

def atualizar_alvo(alvo: Alvo, **dados):
    for campo, valor in dados.items():
        setattr(alvo, campo, valor)
    alvo.save()
    return alvo

def excluir_alvo(alvo: Alvo):
    alvo.delete()
