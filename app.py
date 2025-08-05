from flask import Flask
from routes import main_bp, validacao_bp
from routes.validacoes_especificas import validacoes_bp
from routes.checklists_manuais import checklists_bp

app = Flask(__name__)
app.secret_key = 'mdw_validacao_secret_key_2025'  # Necessário para flash messages

# Registro dos blueprints
app.register_blueprint(main_bp)
app.register_blueprint(validacao_bp)
app.register_blueprint(validacoes_bp)
app.register_blueprint(checklists_bp)

if __name__ == '__main__':
    app.run(debug=True)