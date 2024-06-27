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
from .views import site_view


#NOTE: StarClinic

from .models import recepcionista_model
from .models import log_model
from .models import especialidade_model
from .models import medico_model 
from .models  import consulta_model
from .models  import prontuariopaciente_model
from .models  import planosaude_model













