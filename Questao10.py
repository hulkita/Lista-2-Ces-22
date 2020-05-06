def meu_decorador(f):
    def decorar():
        print("Decorador funcionando!!!")
        f()
    return decorar

@meu_decorador
def minha_funcao():
    print("Função teste")


minha_funcao()

