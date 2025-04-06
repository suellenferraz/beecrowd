# Lanche

codigo, quantidade = map(int, input().split())
precos = {
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50
}
preco = precos.get(codigo, 0)
valor_total = preco * quantidade
print(f"Total: R$ {valor_total:.2f}")
