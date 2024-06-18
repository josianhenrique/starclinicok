#importando o flask
from flask import Flask
#importando o SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,upgrade
from flask_wtf import CSRFProtect
from flask_babel import Babel
#criando o aplicativo
app = Flask(__name__)
#puxando o arquivo config.py
app.config.from_object('config')
#criando um objeto db da classe SQLAlchemy
db = SQLAlchemy(app)
#criar uma variável migrate e passar a instância da aplicação e do db
migrate = Migrate(app,db)
csrf = CSRFProtect(app)
csrf.init_app(app)

babel = Babel(app)

from .views import especialidade_view
from .views import planosaude_view
from .views import recepcionista_view
from .views import medico_view
from .views import prontuariopaciente_view
from .views import consulta_view
from .views import log_view
from .views import login_view

#NOTE: StarClinic

from .models import recepcionista
from .models import log
from .models import especialidade
from .models import medico 
from .models  import consulta
from .models  import prontuariopaciente
from .models  import planosaude_model













