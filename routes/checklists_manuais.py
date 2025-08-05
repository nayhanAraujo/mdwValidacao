from flask import Blueprint, render_template, request, flash, redirect, url_for
from database import Validacao
import logging

logger = logging.getLogger(__name__)

checklists_bp = Blueprint('checklists', __name__)

@checklists_bp.route('/checklist-html', methods=['GET', 'POST'])
def checklist_html():
    """Checklist manual específico para HTML"""
    if request.method == 'POST':
        try:
            # Coletar dados do checklist HTML
            checklist_data = {}
            for key in request.form:
                if key.startswith('html_'):
                    checklist_data[key] = request.form[key] == 'on'
            
            # Salvar no banco de dados
            try:
                validacao = Validacao()
                validacao.salvar_validacao_manual(checklist_data, 'checklist_html')
                flash('Checklist HTML salvo com sucesso!', 'success')
                return redirect(url_for('checklists.checklist_html'))
            except Exception as e:
                logger.error(f"Erro ao salvar checklist HTML: {e}")
                flash('Erro ao salvar checklist no banco de dados', 'error')
        
        except Exception as e:
            logger.error(f"Erro no processamento do checklist HTML: {e}")
            flash('Erro ao processar checklist', 'error')
    
    return render_template('checklist_html.html')

@checklists_bp.route('/checklist-bi', methods=['GET', 'POST'])
def checklist_bi():
    """Checklist manual específico para BI"""
    if request.method == 'POST':
        try:
            # Coletar dados do checklist BI
            checklist_data = {}
            for key in request.form:
                if key.startswith('bi_'):
                    checklist_data[key] = request.form[key] == 'on'
            
            # Salvar no banco de dados
            try:
                validacao = Validacao()
                validacao.salvar_validacao_manual(checklist_data, 'checklist_bi')
                flash('Checklist BI salvo com sucesso!', 'success')
                return redirect(url_for('checklists.checklist_bi'))
            except Exception as e:
                logger.error(f"Erro ao salvar checklist BI: {e}")
                flash('Erro ao salvar checklist no banco de dados', 'error')
        
        except Exception as e:
            logger.error(f"Erro no processamento do checklist BI: {e}")
            flash('Erro ao processar checklist', 'error')
    
    return render_template('checklist_bi.html')

@checklists_bp.route('/checklist-api', methods=['GET', 'POST'])
def checklist_api():
    """Checklist manual específico para API"""
    if request.method == 'POST':
        try:
            # Coletar dados do checklist API
            checklist_data = {}
            for key in request.form:
                if key.startswith('api_'):
                    checklist_data[key] = request.form[key] == 'on'
            
            # Salvar no banco de dados
            try:
                validacao = Validacao()
                validacao.salvar_validacao_manual(checklist_data, 'checklist_api')
                flash('Checklist API salvo com sucesso!', 'success')
                return redirect(url_for('checklists.checklist_api'))
            except Exception as e:
                logger.error(f"Erro ao salvar checklist API: {e}")
                flash('Erro ao salvar checklist no banco de dados', 'error')
        
        except Exception as e:
            logger.error(f"Erro no processamento do checklist API: {e}")
            flash('Erro ao processar checklist', 'error')
    
    return render_template('checklist_api.html')

@checklists_bp.route('/checklist-relatorio', methods=['GET', 'POST'])
def checklist_relatorio():
    """Checklist manual específico para Relatórios"""
    if request.method == 'POST':
        try:
            # Coletar dados do checklist Relatório
            checklist_data = {}
            for key in request.form:
                if key.startswith('rel_'):
                    checklist_data[key] = request.form[key] == 'on'
            
            # Salvar no banco de dados
            try:
                validacao = Validacao()
                validacao.salvar_validacao_manual(checklist_data, 'checklist_relatorio')
                flash('Checklist Relatório salvo com sucesso!', 'success')
                return redirect(url_for('checklists.checklist_relatorio'))
            except Exception as e:
                logger.error(f"Erro ao salvar checklist Relatório: {e}")
                flash('Erro ao salvar checklist no banco de dados', 'error')
        
        except Exception as e:
            logger.error(f"Erro no processamento do checklist Relatório: {e}")
            flash('Erro ao processar checklist', 'error')
    
    return render_template('checklist_relatorio.html')

@checklists_bp.route('/checklist-csharp', methods=['GET', 'POST'])
def checklist_csharp():
    """Checklist manual específico para C#"""
    if request.method == 'POST':
        try:
            # Coletar dados do checklist C#
            checklist_data = {}
            for key in request.form:
                if key.startswith('cs_'):
                    checklist_data[key] = request.form[key] == 'on'
            
            # Salvar no banco de dados
            try:
                validacao = Validacao()
                validacao.salvar_validacao_manual(checklist_data, 'checklist_csharp')
                flash('Checklist C# salvo com sucesso!', 'success')
                return redirect(url_for('checklists.checklist_csharp'))
            except Exception as e:
                logger.error(f"Erro ao salvar checklist C#: {e}")
                flash('Erro ao salvar checklist no banco de dados', 'error')
        
        except Exception as e:
            logger.error(f"Erro no processamento do checklist C#: {e}")
            flash('Erro ao processar checklist', 'error')
    
    return render_template('checklist_csharp.html') 