import os
import sys
import newrelic.agent
from apps import create_app
from flask_script import Manager
from flask_script import Server
import config

# "staging" for Staging
# "production" for Production
env = os.environ.get('HOSTENV') or 'development'
newrelic_cfg_file = os.path.join(os.getcwd(), "conf", "newapp-newrelic-%s.ini" % env)

if env == "production":
  newrelic.agent.initialize(newrelic_cfg_file)

app = create_app()
app.config['DEBUG'] = True
manager = Manager(app)
manager.add_command("runserver", Server(host="0.0.0.0", port=config.PORT))

@manager.command
def test(coverage=False):
  """Run the unit tests."""
  pass

if __name__ == '__main__':
  manager.run()
