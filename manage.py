# Always keep the monkeypatching above anything.
# Otherwise any library before it will use unpatched sockets and threads
# import gevent.monkey
# gevent.monkey.patch_all()

from __init__ import create_app
import os
import unittest
import sys
# import newrelic.agent
from flask_script import Manager
from flask_script import Server
import config

# "staging" for Staging
# "production" for Production
env = os.environ.get('HOSTENV') or 'development'

# if env == "production":
#   newrelic_cfg_file = os.path.join(os.getcwd(), "conf", "newapp-newrelic-%s.ini" % env)
#   newrelic.agent.initialize(newrelic_cfg_file)

app = create_app()
app.config['DEBUG'] = True
manager = Manager(app)
manager.add_command("runserver", Server(host="0.0.0.0", port=config.PORT))

@manager.command
def test(coverage=False):
  """Run the unit tests."""

  tests = unittest.TestLoader().discover('test')
  unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
  manager.run()
