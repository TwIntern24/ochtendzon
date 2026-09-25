import os
import subprocess

def build_folder(args, folder, object_files):
  with os.scandir(folder) as it:
    for entry in it:
      if entry.is_file() and entry.name.endswith('.tau'): build_file(args, entry.path, object_files)
      elif entry.is_dir(): build_folder(args, entry.path, object_files)


def transpile_file(input, output, target):
  process = subprocess.Popen([
    'tau',
    '--input', input,
    '--output', output,
    '--target', target,
  ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
  stdout, stderr = process.communicate()

  if process.returncode != 0:
    print(f"When transpiling {input}: {stderr}")


def compile_file(base):
  process = subprocess.Popen([
    'g++',
    '-c', f'{base}.cpp', 
    '-o', f'{base}.o'
  ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
  stdout, stderr = process.communicate()

  if process.returncode != 0:
    print(f"When compiling {base}.cpp: {stderr}")


def link_binary(output, object_files):
  args = ['g++', '-o', output]
  args.extend(object_files)
  process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
  stdout, stderr = process.communicate()

  # Print the return code (0 means success)
  if process.returncode != 0:
    print(f"When linking {output}: {stderr}")


def build_file(args, file, object_files: list[str]):
  output = os.path.dirname(file).replace('src', 'target', 1)
  create_folder(output)

  transpile_file(file, output, args.target)

  base, _ = os.path.splitext(file.replace('src', 'target'))
  compile_file(base)
  
  object_files.append(f'{base}.o')

  
def create_folder(folder):
  os.makedirs(folder, exist_ok=True)