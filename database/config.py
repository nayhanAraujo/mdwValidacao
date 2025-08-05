import os
from pathlib import Path

# Configurações do banco de dados Firebird
DB_CONFIG = {
    'host': 'localhost',
    'port': 3050,
    'database': str(Path(__file__).parent / 'MDWVALIDACAO.FDB'),
    'user': 'SYSDBA',
    'password': 'masterkey',
    'charset': 'UTF8'
}

# Configurações alternativas para desenvolvimento
if os.getenv('FLASK_ENV') == 'development':
    DB_CONFIG.update({
        'host': 'localhost',
        'port': 3050,
        'user': 'SYSDBA',
        'password': 'masterkey'
    })

# Configurações para produção (pode ser sobrescrito por variáveis de ambiente)
if os.getenv('FLASK_ENV') == 'production':
    DB_CONFIG.update({
        'host': os.getenv('DB_HOST', 'localhost'),
        'port': int(os.getenv('DB_PORT', 3050)),
        'user': os.getenv('DB_USER', 'SYSDBA'),
        'password': os.getenv('DB_PASSWORD', 'masterkey'),
        'database': os.getenv('DB_PATH', str(Path(__file__).parent / 'MDWVALIDACAO.FDB'))
    }) 