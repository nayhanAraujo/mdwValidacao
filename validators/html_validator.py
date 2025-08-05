import re

def validar_html(conteudo):
    erros = []

     # Corrigindo a verificação do containerHtml:
    if not re.search(r'<div[^>]*\bid\s*=\s*["\']containerHtml["\']', conteudo, re.IGNORECASE):
        erros.append("❌ Falta o containerHtml principal.")

    if any(tag in conteudo.lower() for tag in ["<html", "<head", "<body", "<link"]):
        erros.append("❌ Uso proibido das tags <html>, <head>, <body> ou <link>.")

    if "function iniciarFuncoes()" not in conteudo:
        erros.append("❌ Função iniciarFuncoes() ausente.")

    if not conteudo.strip().endswith("iniciarFuncoes();"):
        erros.append("❌ iniciarFuncoes(); deve ser a última instrução.")

    nomes_proibidos = [".container", ".button", ".form", ".input", ".table"]
    if any(nome in conteudo for nome in nomes_proibidos):
        erros.append("❌ Uso de classes genéricas proibidas.")

    if 'id="VR_' not in conteudo:
        erros.append("❌ Campos sem prefixo VR_ para persistência.")

    return erros
