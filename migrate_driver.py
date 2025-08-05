#!/usr/bin/env python3
"""
Script para migrar do driver fdb antigo para o novo firebird-driver
"""

import subprocess
import sys
import os

def verificar_driver_antigo():
    """Verifica se o driver antigo está instalado"""
    try:
        import fdb
        print("⚠️  Driver fdb antigo encontrado")
        return True
    except ImportError:
        print("✅ Driver fdb antigo não encontrado")
        return False

def desinstalar_driver_antigo():
    """Desinstala o driver antigo"""
    print("🗑️  Desinstalando driver fdb antigo...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "fdb", "-y"])
        print("   ✅ Driver fdb desinstalado com sucesso")
        return True
    except subprocess.CalledProcessError as e:
        print(f"   ❌ Erro ao desinstalar fdb: {e}")
        return False

def instalar_novo_driver():
    """Instala o novo driver"""
    print("📦 Instalando novo driver firebird-driver...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "firebird-driver==1.0.0"])
        print("   ✅ Driver firebird-driver instalado com sucesso")
        return True
    except subprocess.CalledProcessError as e:
        print(f"   ❌ Erro ao instalar firebird-driver: {e}")
        return False

def testar_novo_driver():
    """Testa o novo driver"""
    print("🧪 Testando novo driver...")
    try:
        import firebird.driver as fdb
        print("   ✅ Novo driver importado com sucesso")
        return True
    except ImportError as e:
        print(f"   ❌ Erro ao importar novo driver: {e}")
        return False

def testar_conexao():
    """Testa a conexão com o novo driver"""
    print("🔍 Testando conexão com novo driver...")
    try:
        from database.test_connection import testar_conexao
        return testar_conexao()
    except Exception as e:
        print(f"   ❌ Erro ao testar conexão: {e}")
        return False

def main():
    """Função principal da migração"""
    print("🔄 Migrando do driver fdb para firebird-driver...\n")
    
    # Verificar se o driver antigo está instalado
    if verificar_driver_antigo():
        print("📋 Driver antigo encontrado. Iniciando migração...")
        
        # Desinstalar driver antigo
        if not desinstalar_driver_antigo():
            print("❌ Falha ao desinstalar driver antigo")
            return False
        
        # Instalar novo driver
        if not instalar_novo_driver():
            print("❌ Falha ao instalar novo driver")
            return False
    else:
        print("📋 Driver antigo não encontrado. Instalando novo driver...")
        
        # Instalar novo driver
        if not instalar_novo_driver():
            print("❌ Falha ao instalar novo driver")
            return False
    
    # Testar novo driver
    if not testar_novo_driver():
        print("❌ Falha ao testar novo driver")
        return False
    
    # Testar conexão
    if not testar_conexao():
        print("❌ Falha ao testar conexão")
        return False
    
    print("\n🎉 Migração concluída com sucesso!")
    print("✅ O novo driver firebird-driver está funcionando")
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        print("\n❌ Migração falhou. Verifique os erros acima.")
        sys.exit(1)
    else:
        print("\n✨ Migração concluída!") 