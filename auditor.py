import sys
import json


with open("politicas/politica.json", "r", encoding="utf-8") as f:
    dados_auditoria = json.load(f)

with open("exemplos_dev/config_dev.json", "r", encoding="utf-8") as f:
    dados_dev = json.load(f)

if dados_dev.get('porta_permitida') != dados_auditoria.get('porta_permitida'):
    print("ERRO DE SEGURANÇA: Porta não permitida para uso no sistema.")
    sys.exit(1)

elif dados_dev.get('tamanho_min_senha') < dados_auditoria.get('tamanho_min_senha'):
    print("ERRO DE SEGURANÇA: Senha não comporta a segurança necessária da política.")
    sys.exit(1)

else:
    print("Requisitos comprovados e registados nas políticas definidas.")
    sys.exit(0)