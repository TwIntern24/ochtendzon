def main():
  import os
  import argparse

  parser = argparse.ArgumentParser(
    prog='ochtendzon',
    description='Simple compiler toolchain for the Tau language. ',
    fromfile_prefix_chars='@',
  )

  subparsers = parser.add_subparsers(title='commands', required=True, dest='command')

  parser_build = subparsers.add_parser('build', help='Compile the current package')
  parser_build.add_argument('--target', choices=('cpp', 'cranelift'), default='cpp')

  parser_init = subparsers.add_parser('init', help='Create a new ochtendzon package')
  parser_init.add_argument('--name', type=str)

  parser_run = subparsers.add_parser('run', help='Run a binary of the local package')

  args = parser.parse_args()

  match args.command:
    case 'build':
      from ochtendzon.build import build
      build(args)
