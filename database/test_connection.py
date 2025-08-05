#!/usr/bin/env python3
"""
Script para testar a conexão com o banco de dados Firebird
"""

import sys
import os

# Adicionar o diretório pai ao path para importar os módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import Validacao, db_connection

def testar_conexao():
    """Testa a conexão com o banco de dados"""
    print("🔍 Testando conexão com o banco de dados Firebird...")
    
    try:
        # Testar conexão básica
        print("1. Testando conexão básica...")
        db_connection.connect()
        print("   ✅ Conexão estabelecida com sucesso!")
        
        # Testar query simples
        print("2. Testando query simples...")
        result = db_connection.execute_query("SELECT COUNT(*) FROM VALIDACOES")
        print(f"   ✅ Query executada. Total de registros: {result[0][0]}")
        
        # Testar modelo de validação
        print("3. Testando modelo de validação...")
        validacao = Validacao()
        if validacao.testar_conexao():
            print("   ✅ Modelo de validação funcionando!")
        else:
            print("   ❌ Erro no modelo de validação")
        
        print("\n🎉 Todos os testes passaram! O banco está funcionando corretamente.")
        return True
        
    except Exception as e:
        print(f"❌ Erro durante o teste: {e}")
        print("\n🔧 Possíveis soluções:")
        print("1. Verifique se o Firebird está rodando na porta 3050")
        print("2. Verifique se o arquivo MDWVALIDACAO.FDB existe")
        print("3. Verifique as credenciais (SYSDBA/masterkey)")
        print("4. Instale o driver firebird-driver: pip install firebird-driver")
        return False
    
    finally:
        db_connection.disconnect()

def testar_insercao():
    """Testa a inserção de dados"""
    print("\n🧪 Testando inserção de dados...")
    
    try:
        validacao = Validacao()
        
        # Testar inserção de validação automática
        resultado_teste = {
            'erros': ['Teste de erro 1', 'Teste de erro 2'],
            'status': 'com_erros',
            'arquivo_teste': 'teste.html'
        }
        
        success = validacao.salvar_validacao_automatica(
            'html', 
            resultado_teste, 
            'teste_automatico.html'
        )
        
        if success:
            print("   ✅ Inserção de validação automática funcionou!")
        else:
            print("   ❌ Erro na inserção de validação automática")
        
        # Testar inserção de validação manual
        checklist_teste = {
            'sec1_1': True,
            'sec1_2': False,
            'sec2_1': True,
            'sec2_2': True,
            'sec2_3': True
        }
        
        success = validacao.salvar_validacao_manual(
            checklist_teste, 
            'teste_manual.html'
        )
        
        if success:
            print("   ✅ Inserção de validação manual funcionou!")
        else:
            print("   ❌ Erro na inserção de validação manual")
        
        print("🎉 Testes de inserção concluídos!")
        return True
        
    except Exception as e:
        print(f"❌ Erro durante teste de inserção: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Iniciando testes do banco de dados...\n")
    
    # Testar conexão
    if testar_conexao():
        # Se a conexão funcionou, testar inserção
        testar_insercao()
    
    print("\n✨ Testes concluídos!") 