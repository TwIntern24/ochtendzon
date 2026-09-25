from ochtendzon.build.files import build_folder, create_folder, link_binary
from os.path import isdir

def build(args):
  create_folder('target')

  if isdir('src'):
    object_files = []
    build_folder(args, 'src', object_files)
    print(object_files)
    link_binary('target/hello-world', object_files)
  else:
    print('Source folder not found')
    os.exit(1)
  
