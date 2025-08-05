import firebird.driver as fdb
from contextlib import contextmanager
from .config import DB_CONFIG
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DatabaseConnection:
    """Classe para gerenciar conexões com o banco de dados Firebird"""
    
    def __init__(self, config=None):
        self.config = config or DB_CONFIG
        self._connection = None
    
    def connect(self):
        """Estabelece conexão com o banco de dados"""
        try:
            self._connection = fdb.connect(
                host=self.config['host'],
                port=self.config['port'],
                database=self.config['database'],
                user=self.config['user'],
                password=self.config['password'],
                charset=self.config['charset']
            )
            logger.info("Conexão com o banco de dados estabelecida com sucesso")
            return self._connection
        except Exception as e:
            logger.error(f"Erro ao conectar com o banco de dados: {e}")
            raise
    
    def disconnect(self):
        """Fecha a conexão com o banco de dados"""
        if self._connection:
            try:
                self._connection.close()
                self._connection = None
                logger.info("Conexão com o banco de dados fechada")
            except Exception as e:
                logger.error(f"Erro ao fechar conexão: {e}")
    
    def execute_query(self, query, params=None):
        """Executa uma query e retorna os resultados"""
        try:
            cursor = self._connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            
            # Para SELECT, retorna os resultados
            if query.strip().upper().startswith('SELECT'):
                results = cursor.fetchall()
                cursor.close()
                return results
            else:
                # Para INSERT, UPDATE, DELETE
                self._connection.commit()
                cursor.close()
                return cursor.rowcount
                
        except Exception as e:
            logger.error(f"Erro ao executar query: {e}")
            self._connection.rollback()
            raise
    
    @contextmanager
    def get_connection(self):
        """Context manager para gerenciar conexões"""
        try:
            if not self._connection:
                self.connect()
            yield self._connection
        except Exception as e:
            logger.error(f"Erro na conexão: {e}")
            raise
        finally:
            # Não fechar a conexão aqui, deixar para o método disconnect
            pass

# Instância global da conexão
db_connection = DatabaseConnection() 