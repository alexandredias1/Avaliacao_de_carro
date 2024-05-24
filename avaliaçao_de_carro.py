#Avaliação de carros

car1 = int(input("Digite a nota do carro: "))
car2 = float(input("Digite o preço do carro: "))

if car1 >= 0 and car1 <= 50:
    valFinal = car2 - (car2 * 30) / 100
    print(f"O preço final do carro é: {valFinal}")
elif car1 > 50 and car1 <= 80:
    print(f"O preço final do carro é: {car2}")
elif car1 > 80 and car1 <= 100:
    valFinal = car2 + (car2 * 20) / 100
    print(f"{valFinal}")
else:
    print("Valor inválido")