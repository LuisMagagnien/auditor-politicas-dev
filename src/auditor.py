import json


with open("politica.json", "r", encoding="utf-8") as f:
    dados_auditoria = json.load(f)


with open("config_dev.json", "r", encoding="utf-8") as f:
    dados_dev = json.load(f)


if dados_dev.get('porta_permitida') != dados_auditoria.get('porta_permitida'):
    print("Porta não permitida para uso no sistema.")
elif dados_dev.get('tamanho_min_senha') < dados_auditoria.get('tamanho_min_senha'):
    print("Senha não comporta a segurança necessária da política.")
else:
    print("Requisitos comprovados e registados nas políticas definidas.")