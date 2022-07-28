from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required
from .models import Product
from . import db

produto = Blueprint('produto', __name__)

@produto.route('/produtos')
@login_required
def listagem():
    return 'Listagem'

@produto.route('/produtos/cadastro')
@login_required
def cadastro():
    return 'Cadastro de produto'    