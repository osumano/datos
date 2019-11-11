
from datos import app

from apiv1 import blueprint as apiv1

app.register_blueprint(apiv1)
