from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required
from .models import Product
from . import db

produto = Blueprint('produto', __name__)

@produto.route('/produtos')
@login_required
def listagem():
    produtos = Product.query
    return render_template('produto_listagem.html', title='Produto \ Listagem', produtos=produtos)

@produto.route('/produtos/cadastro')
@login_required
def cadastro():
    return render_template('produto_cadastro.html')

@produto.route('/produtos/add', methods=('GET', 'POST'))
@login_required
def create():
    
    descricao = request.form.get('descricao')
    valor = request.form.get('valor')

    if not descricao:
        flash('Descricao is required!')
    elif not valor:
        flash('Valor is required!')
    else:
        messages = []
        messages.append({'descricao': descricao, 'valor': valor})
        prod = Product(descricao=descricao, valor=valor)
        db.session.add(prod)
        db.session.commit()
        return 'Ak1'
        #return redirect(url_for('produto.create'))

    return redirect(url_for('produto.create'))
