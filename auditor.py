import json

with open("politica.json", "r", encoding="utf-8") as f:
    dados_auditoria = json.load(f)
print(dados_auditoria)

with open("config_dev.json", "r", encoding="utf-8") as f:
    dados_dev = json.load(f)
print(dados_dev)



porta_permitida = 443
senha_minima = 12

if porta_permitida != 443:
    print("Porta não permitida para uso no sistema. ")
elif senha_minima != 12:
    print("Senha não comporta a segurança necessária da politicas. ")
else:
    print("Requisitos comprovados e registrados nas politicas definidas. ")