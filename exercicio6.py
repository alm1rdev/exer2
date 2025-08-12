# calculadora de imc

ola=input("ola, agoara vamos calcular seu imc,TECLE ENTER !")
p1=float(input("qual seu peso em quilogramas?"))
p2=float(input("qual sua altura em metros"))
calculo=p1/(p2*p2)
print(f"SEU IMC E DE : {calculo:.2f}. Se seu imc esta entre 18 e 25 parabens voce esta em bem! ATENCAO, abaixo de 18 e acima de 25 procure orientacao de um profissional da saude.")
