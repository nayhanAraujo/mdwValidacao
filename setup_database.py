#!/usr/bin/env python3
"""
Script de configuração do banco de dados Firebird
"""

import os
import sys
import subprocess
from pathlib import Path

def verificar_firebird():
    """Verifica se o Firebird está instalado e rodando"""
    print("🔍 Verificando Firebird...")
    
    try:
        # Tentar conectar com o Firebird
        import firebird.driver as fdb
        print("   ✅ Driver firebird-driver encontrado")
        return True
    except ImportError:
        print("   ❌ Driver firebird-driver não encontrado")
        print("   💡 Execute: pip install firebird-driver")
        return False

def verificar_arquivo_banco():
    """Verifica se o arquivo do banco existe"""
    print("🔍 Verificando arquivo do banco...")
    
    db_file = Path("database/MDWVALIDACAO.FDB")
    if db_file.exists():
        print(f"   ✅ Arquivo do banco encontrado: {db_file}")
        return True
    else:
        print(f"   ❌ Arquivo do banco não encontrado: {db_file}")
        return False

def instalar_dependencias():
    """Instala as dependências necessárias"""
    print("📦 Instalando dependências...")
    
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("   ✅ Dependências instaladas com sucesso")
        return True
    except subprocess.CalledProcessError as e:
        print(f"   ❌ Erro ao instalar dependências: {e}")
        return False

def testar_conexao():
    """Testa a conexão com o banco"""
    print("🧪 Testando conexão com o banco...")
    
    try:
        from database.test_connection import testar_conexao
        return testar_conexao()
    except Exception as e:
        print(f"   ❌ Erro ao testar conexão: {e}")
        return False

def criar_estrutura():
    """Cria a estrutura do banco se necessário"""
    print("🏗️ Verificando estrutura do banco...")
    
    try:
        from database import db_connection
        
        # Conectar ao banco
        db_connection.connect()
        
        # Verificar se a tabela existe
        result = db_connection.execute_query("SELECT COUNT(*) FROM VALIDACOES")
        print(f"   ✅ Tabela VALIDACOES encontrada com {result[0][0]} registros")
        
        db_connection.disconnect()
        return True
        
    except Exception as e:
        print(f"   ❌ Erro ao verificar estrutura: {e}")
        print("   💡 Certifique-se de que o Firebird está rodando e o arquivo .FDB existe")
        return False

def main():
    """Função principal do setup"""
    print("🚀 Configurando banco de dados Firebird...\n")
    
    # Verificar dependências
    if not verificar_firebird():
        print("\n📦 Instalando driver firebird-driver...")
        if not instalar_dependencias():
            print("❌ Falha na instalação das dependências")
            return False
    
    # Verificar arquivo do banco
    if not verificar_arquivo_banco():
        print("❌ Arquivo do banco não encontrado")
        print("💡 Certifique-se de que o arquivo MDWVALIDACAO.FDB está em database/")
        return False
    
    # Testar conexão
    if not testar_conexao():
        print("❌ Falha no teste de conexão")
        return False
    
    # Verificar estrutura
    if not criar_estrutura():
        print("❌ Falha na verificação da estrutura")
        return False
    
    print("\n🎉 Configuração concluída com sucesso!")
    print("✅ O banco de dados está pronto para uso")
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        print("\n❌ Configuração falhou. Verifique os erros acima.")
        sys.exit(1)
    else:
        print("\n✨ Setup concluído!") 