
from datos import app

from apiv1 import blueprint as apiv1

app.register_blueprint(apiv1)

app.run(host='0.0.0.0', port=5000, debug=False)

