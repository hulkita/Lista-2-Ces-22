def MercadoExtra(nome, *tipos, **produtos):
    print("Bem vindos ao", nome)
    print("Nosso supermercado trabalha nas seguintes áreas:")
    for tipo in tipos:
        print(tipo)
    print("------------------------------------------------------")
    print("Os preços e produtos se encontram na tabela a seguir")
    print("------------------------------------------------------")

    products = sorted(produtos.keys())
    for p in products:
        print(p, ":", produtos[p])

    print("Obrigado pela visita")

MercadoExtra("Extra", "frutas", "informatica", "cozinha",
             banana = '10 reais',
             computador = '2000 reais',
             geladeira = '1000 reais')