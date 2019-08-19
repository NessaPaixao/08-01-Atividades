def lista_de_compras(pessoa, *args):
    print("Segue abaixo a lista de compra de " + (pessoa) + ":")
    for arg in args:
        print(arg)


lista_de_compras("Maria Antonieta", "Queijo", "Goiabada")

lista_de_compras("Sophia", "Chocolate", "Refrigerante", "Cookies", "Salgadinho")

lista_de_compras("Miguel Junior Junior", "Ração", "Mordedor")

def lista_de_compras(pessoa, **kwargs):
    print("Olá" + (pessoa))
    fruta = kwargs.get("fruta")
    bebida = kwargs["bebida"]
    if fruta is not None:
        print("Na lista de compras há uma fruta e uma massa:" + (fruta))

lista_de_compras("Sophia", guloseima="Chocolate", bebida="Refrigerante", fruta="ameixa",)
