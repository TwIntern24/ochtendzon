import subprocess
import sys
from ochtendzon.config import CONFIG_NAME, load_config

def run(args):
  if isfile(CONFIG_NAME):
    config = load_config()
  else:
    print('ochtendzon toml config not found')
    return 1

  if isdir('target'):
    binary = config['project']['name']
    with subprocess.Popen([f'target/{binary}'],
      stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr) as process:
      return process.returncode
  else:
    print('Target folder not found')
    return 1
  
