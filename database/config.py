import os
from pathlib import Path

# Configurações padrão (desenvolvimento)
DB_CONFIG = {
    'host': 'localhost',
    'port': 3052,
    'database': str(Path(__file__).parent / 'MDWVALIDACAO.FDB'),  # Caminho correto
    'user': 'SYSDBA',
    'password': 'masterkey',
    'charset': 'UTF8'
}

# Sobrescreve configurações para produção
if os.getenv('FLASK_ENV') == 'production':
    DB_CONFIG.update({
        'host': os.getenv('DB_HOST', 'localhost'),
        'port': int(os.getenv('DB_PORT', 3052)),
        'user': os.getenv('DB_USER', 'SYSDBA'),
        'password': os.getenv('DB_PASSWORD', 'masterkey'),
        'database': os.getenv('DB_PATH', str(Path(__file__).parent / 'MDWVALIDACAO.FDB'))
    })