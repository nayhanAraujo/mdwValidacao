from flask import Blueprint, render_template, request, flash, redirect, url_for
from validators import html_validator
from database import Validacao
import logging

logger = logging.getLogger(__name__)

validacoes_bp = Blueprint('validacoes', __name__)

@validacoes_bp.route('/validar-html', methods=['GET', 'POST'])
def validar_html():
    """Validação específica para scripts HTML"""
    if request.method == 'POST':
        try:
            arquivo = request.files['arquivo']
            if arquivo.filename == '':
                flash('Por favor, selecione um arquivo HTML', 'error')
                return render_template('validar_especifica.html', tipo='HTML', titulo='Validar Script HTML')
            
            conteudo = arquivo.read().decode('utf-8')
            nome_arquivo = arquivo.filename
            
            # Validar HTML
            erros = html_validator.validar_html(conteudo)
            
            # Preparar resultado
            resultado = {
                'erros': erros,
                'status': 'com_erros' if erros else 'sem_erros',
                'arquivo': nome_arquivo,
                'tipo_validacao': 'html'
            }
            
            # Salvar no banco
            try:
                validacao = Validacao()
                validacao.salvar_validacao_automatica('html', resultado, nome_arquivo)
                flash('Validação salva com sucesso!', 'success')
            except Exception as e:
                logger.error(f"Erro ao salvar validação: {e}")
                flash('Erro ao salvar validação no banco de dados', 'error')
            
            return render_template('resultado_validacao.html', 
                                erros=erros, 
                                tipo='HTML', 
                                nome=nome_arquivo)
                                
        except Exception as e:
            logger.error(f"Erro na validação HTML: {e}")
            flash('Erro durante a validação', 'error')
            return render_template('validar_especifica.html', tipo='HTML', titulo='Validar Script HTML')
    
    return render_template('validar_especifica.html', tipo='HTML', titulo='Validar Script HTML')

@validacoes_bp.route('/validar-bi', methods=['GET', 'POST'])
def validar_bi():
    """Validação específica para painéis BI"""
    if request.method == 'POST':
        try:
            arquivo = request.files['arquivo']
            if arquivo.filename == '':
                flash('Por favor, selecione um arquivo BI', 'error')
                return render_template('validar_especifica.html', tipo='BI', titulo='Validar Painel BI')
            
            conteudo = arquivo.read().decode('utf-8')
            nome_arquivo = arquivo.filename
            
            # Aqui você pode implementar validações específicas para BI
            erros = []  # Placeholder para validações BI
            
            resultado = {
                'erros': erros,
                'status': 'com_erros' if erros else 'sem_erros',
                'arquivo': nome_arquivo,
                'tipo_validacao': 'bi'
            }
            
            # Salvar no banco
            try:
                validacao = Validacao()
                validacao.salvar_validacao_automatica('bi', resultado, nome_arquivo)
                flash('Validação salva com sucesso!', 'success')
            except Exception as e:
                logger.error(f"Erro ao salvar validação: {e}")
                flash('Erro ao salvar validação no banco de dados', 'error')
            
            return render_template('resultado_validacao.html', 
                                erros=erros, 
                                tipo='BI', 
                                nome=nome_arquivo)
                                
        except Exception as e:
            logger.error(f"Erro na validação BI: {e}")
            flash('Erro durante a validação', 'error')
            return render_template('validar_especifica.html', tipo='BI', titulo='Validar Painel BI')
    
    return render_template('validar_especifica.html', tipo='BI', titulo='Validar Painel BI')

@validacoes_bp.route('/validar-api', methods=['GET', 'POST'])
def validar_api():
    """Validação específica para painéis API"""
    if request.method == 'POST':
        try:
            arquivo = request.files['arquivo']
            if arquivo.filename == '':
                flash('Por favor, selecione um arquivo API', 'error')
                return render_template('validar_especifica.html', tipo='API', titulo='Validar Painel API')
            
            conteudo = arquivo.read().decode('utf-8')
            nome_arquivo = arquivo.filename
            
            # Aqui você pode implementar validações específicas para API
            erros = []  # Placeholder para validações API
            
            resultado = {
                'erros': erros,
                'status': 'com_erros' if erros else 'sem_erros',
                'arquivo': nome_arquivo,
                'tipo_validacao': 'api'
            }
            
            # Salvar no banco
            try:
                validacao = Validacao()
                validacao.salvar_validacao_automatica('api', resultado, nome_arquivo)
                flash('Validação salva com sucesso!', 'success')
            except Exception as e:
                logger.error(f"Erro ao salvar validação: {e}")
                flash('Erro ao salvar validação no banco de dados', 'error')
            
            return render_template('resultado_validacao.html', 
                                erros=erros, 
                                tipo='API', 
                                nome=nome_arquivo)
                                
        except Exception as e:
            logger.error(f"Erro na validação API: {e}")
            flash('Erro durante a validação', 'error')
            return render_template('validar_especifica.html', tipo='API', titulo='Validar Painel API')
    
    return render_template('validar_especifica.html', tipo='API', titulo='Validar Painel API')

@validacoes_bp.route('/validar-relatorio', methods=['GET', 'POST'])
def validar_relatorio():
    """Validação específica para relatórios"""
    if request.method == 'POST':
        try:
            arquivo = request.files['arquivo']
            if arquivo.filename == '':
                flash('Por favor, selecione um arquivo de relatório', 'error')
                return render_template('validar_especifica.html', tipo='Relatório', titulo='Validar Relatório')
            
            conteudo = arquivo.read().decode('utf-8')
            nome_arquivo = arquivo.filename
            
            # Aqui você pode implementar validações específicas para relatórios
            erros = []  # Placeholder para validações de relatório
            
            resultado = {
                'erros': erros,
                'status': 'com_erros' if erros else 'sem_erros',
                'arquivo': nome_arquivo,
                'tipo_validacao': 'relatorio'
            }
            
            # Salvar no banco
            try:
                validacao = Validacao()
                validacao.salvar_validacao_automatica('relatorio', resultado, nome_arquivo)
                flash('Validação salva com sucesso!', 'success')
            except Exception as e:
                logger.error(f"Erro ao salvar validação: {e}")
                flash('Erro ao salvar validação no banco de dados', 'error')
            
            return render_template('resultado_validacao.html', 
                                erros=erros, 
                                tipo='Relatório', 
                                nome=nome_arquivo)
                                
        except Exception as e:
            logger.error(f"Erro na validação de relatório: {e}")
            flash('Erro durante a validação', 'error')
            return render_template('validar_especifica.html', tipo='Relatório', titulo='Validar Relatório')
    
    return render_template('validar_especifica.html', tipo='Relatório', titulo='Validar Relatório')

@validacoes_bp.route('/validar-csharp', methods=['GET', 'POST'])
def validar_csharp():
    """Validação específica para scripts C#"""
    if request.method == 'POST':
        try:
            arquivo = request.files['arquivo']
            if arquivo.filename == '':
                flash('Por favor, selecione um arquivo C#', 'error')
                return render_template('validar_especifica.html', tipo='C#', titulo='Validar Script C#')
            
            conteudo = arquivo.read().decode('utf-8')
            nome_arquivo = arquivo.filename
            
            # Aqui você pode implementar validações específicas para C#
            erros = []  # Placeholder para validações C#
            
            resultado = {
                'erros': erros,
                'status': 'com_erros' if erros else 'sem_erros',
                'arquivo': nome_arquivo,
                'tipo_validacao': 'csharp'
            }
            
            # Salvar no banco
            try:
                validacao = Validacao()
                validacao.salvar_validacao_automatica('csharp', resultado, nome_arquivo)
                flash('Validação salva com sucesso!', 'success')
            except Exception as e:
                logger.error(f"Erro ao salvar validação: {e}")
                flash('Erro ao salvar validação no banco de dados', 'error')
            
            return render_template('resultado_validacao.html', 
                                erros=erros, 
                                tipo='C#', 
                                nome=nome_arquivo)
                                
        except Exception as e:
            logger.error(f"Erro na validação C#: {e}")
            flash('Erro durante a validação', 'error')
            return render_template('validar_especifica.html', tipo='C#', titulo='Validar Script C#')
    
    return render_template('validar_especifica.html', tipo='C#', titulo='Validar Script C#') 