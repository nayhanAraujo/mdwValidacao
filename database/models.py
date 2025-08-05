import json
from datetime import datetime
from .connection import db_connection
import logging

logger = logging.getLogger(__name__)

class Validacao:
    """Modelo para gerenciar validações no banco de dados"""
    
    def __init__(self):
        self.db = db_connection
    
    def salvar_validacao_automatica(self, tipo_validacao, resultado, nome_arquivo):
        """
        Salva uma validação automática no banco de dados
        
        Args:
            tipo_validacao (str): Tipo da validação (html, sql, executeblock, csharp)
            resultado (dict): Resultado da validação com erros e status
            nome_arquivo (str): Nome do arquivo validado
        """
        try:
            # Conectar ao banco
            self.db.connect()
            
            # Preparar dados para inserção
            resultado_json = json.dumps(resultado, ensure_ascii=False)
            
            query = """
                INSERT INTO VALIDACOES (TIPO_VALIDACAO, RESULTADO, NOME_ARQUIVO, DATA_VALIDACAO)
                VALUES (?, ?, ?, ?)
            """
            
            params = (tipo_validacao, resultado_json, nome_arquivo, datetime.now())
            
            # Executar inserção
            rows_affected = self.db.execute_query(query, params)
            
            logger.info(f"Validação salva com sucesso. Linhas afetadas: {rows_affected}")
            return True
            
        except Exception as e:
            logger.error(f"Erro ao salvar validação: {e}")
            raise
        finally:
            self.db.disconnect()
    
    def salvar_validacao_manual(self, checklist_data, nome_arquivo=None):
        """
        Salva uma validação manual no banco de dados
        
        Args:
            checklist_data (dict): Dados do checklist preenchido
            nome_arquivo (str): Nome do arquivo validado (opcional)
        """
        try:
            # Conectar ao banco
            self.db.connect()
            
            # Preparar resultado da validação manual
            resultado = {
                'tipo': 'validacao_manual',
                'checklist': checklist_data,
                'data_validacao': datetime.now().isoformat(),
                'status': 'completo'
            }
            
            resultado_json = json.dumps(resultado, ensure_ascii=False)
            
            query = """
                INSERT INTO VALIDACOES (TIPO_VALIDACAO, RESULTADO, NOME_ARQUIVO, DATA_VALIDACAO)
                VALUES (?, ?, ?, ?)
            """
            
            params = ('validacao_manual', resultado_json, nome_arquivo or 'N/A', datetime.now())
            
            # Executar inserção
            rows_affected = self.db.execute_query(query, params)
            
            logger.info(f"Validação manual salva com sucesso. Linhas afetadas: {rows_affected}")
            return True
            
        except Exception as e:
            logger.error(f"Erro ao salvar validação manual: {e}")
            raise
        finally:
            self.db.disconnect()
    
    def buscar_validacoes(self, limit=50, offset=0):
        """
        Busca validações do banco de dados
        
        Args:
            limit (int): Limite de registros
            offset (int): Offset para paginação
            
        Returns:
            list: Lista de validações
        """
        try:
            # Conectar ao banco
            self.db.connect()
            
            query = """
                SELECT ID, TIPO_VALIDACAO, RESULTADO, NOME_ARQUIVO, DATA_VALIDACAO
                FROM VALIDACOES
                ORDER BY DATA_VALIDACAO DESC
                ROWS ? TO ?
            """
            
            params = (offset + 1, offset + limit)
            
            # Executar consulta
            results = self.db.execute_query(query, params)
            
            # Processar resultados
            validacoes = []
            for row in results:
                id_val, tipo, resultado_json, nome_arquivo, data = row
                
                try:
                    resultado = json.loads(resultado_json)
                except:
                    resultado = {'erro': 'Erro ao processar resultado'}
                
                validacao = {
                    'id': id_val,
                    'tipo_validacao': tipo,
                    'resultado': resultado,
                    'nome_arquivo': nome_arquivo,
                    'data_validacao': data.isoformat() if data else None
                }
                validacoes.append(validacao)
            
            return validacoes
            
        except Exception as e:
            logger.error(f"Erro ao buscar validações: {e}")
            raise
        finally:
            self.db.disconnect()
    
    def buscar_validacao_por_id(self, id_validacao):
        """
        Busca uma validação específica por ID
        
        Args:
            id_validacao (int): ID da validação
            
        Returns:
            dict: Dados da validação ou None se não encontrada
        """
        try:
            # Conectar ao banco
            self.db.connect()
            
            query = """
                SELECT ID, TIPO_VALIDACAO, RESULTADO, NOME_ARQUIVO, DATA_VALIDACAO
                FROM VALIDACOES
                WHERE ID = ?
            """
            
            params = (id_validacao,)
            
            # Executar consulta
            results = self.db.execute_query(query, params)
            
            if results:
                id_val, tipo, resultado_json, nome_arquivo, data = results[0]
                
                try:
                    resultado = json.loads(resultado_json)
                except:
                    resultado = {'erro': 'Erro ao processar resultado'}
                
                return {
                    'id': id_val,
                    'tipo_validacao': tipo,
                    'resultado': resultado,
                    'nome_arquivo': nome_arquivo,
                    'data_validacao': data.isoformat() if data else None
                }
            
            return None
            
        except Exception as e:
            logger.error(f"Erro ao buscar validação por ID: {e}")
            raise
        finally:
            self.db.disconnect()
    
    def testar_conexao(self):
        """
        Testa a conexão com o banco de dados
        
        Returns:
            bool: True se a conexão foi bem-sucedida
        """
        try:
            self.db.connect()
            query = "SELECT COUNT(*) FROM VALIDACOES"
            result = self.db.execute_query(query)
            logger.info(f"Conexão testada com sucesso. Total de validações: {result[0][0]}")
            return True
        except Exception as e:
            logger.error(f"Erro ao testar conexão: {e}")
            return False
        finally:
            self.db.disconnect() 