# Um motorista deseja calcular o consumo médio de combustível do seu carro. Crie um programa que receba a quantidade de quilômetros percorridos e a quantidade de litros de combustível consumidos, e calcule o consumo médio (km por litro).

km = float(input("quilometros percorridos"))
consumo = float(input("consumo de gasolina"))
total = (km/consumo)
print(f"o consumo total é de {total}")