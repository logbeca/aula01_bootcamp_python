nome = input("Insira seu nome:")
salario = float(input("Insira seu salário:"))
bonus = float(input("Insira sua porcentagem do bonus:"))
kpi = 1000 + ( salario * bonus )

print(f"Olá , {nome} , o seu valor bônus foi de   {kpi}")
