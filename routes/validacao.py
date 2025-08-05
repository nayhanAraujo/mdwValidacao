from flask import Blueprint, render_template, request, flash, redirect, url_for
from validators import html_validator
from database import Validacao
import logging

logger = logging.getLogger(__name__)

validacao_bp = Blueprint('validacao', __name__)

@validacao_bp.route('/validar', methods=['GET', 'POST'])
def validar():
    erros = []
    tipo = None
    nome = None
    if request.method == 'POST':
        tipo = request.form['tipo']
        arquivo = request.files['arquivo']
        conteudo = arquivo.read().decode('utf-8')
        nome = arquivo.filename
        if tipo == 'html':
            erros = html_validator.validar_html(conteudo)
    return render_template('index.html', erros=erros, tipo=tipo, nome=nome)

@validacao_bp.route('/validacao-manual', methods=['GET', 'POST'])
def validacao_manual():
    if request.method == 'POST':
        try:
            # Coletar dados do checklist
            checklist_data = {}
            for key in request.form:
                if key.startswith('sec'):
                    checklist_data[key] = request.form[key] == 'on'
            
            # Salvar no banco de dados
            try:
                validacao = Validacao()
                validacao.salvar_validacao_manual(checklist_data)
                flash('Checklist salvo com sucesso!', 'success')
                return redirect(url_for('validacao.validacao_manual'))
            except Exception as e:
                logger.error(f"Erro ao salvar checklist: {e}")
                flash('Erro ao salvar checklist no banco de dados', 'error')
        
        except Exception as e:
            logger.error(f"Erro no processamento do checklist: {e}")
            flash('Erro ao processar checklist', 'error')
    
    return render_template('validacao_manual.html')