import subprocess, os

this_script_dir = __file__.replace(os.path.basename(__file__), '')
abs_ui_dir_path =  this_script_dir + 'windows_ui/'
abs_py_dir_path = this_script_dir + 'windows_py/'

files_list = os.listdir(abs_ui_dir_path)

for file_name in files_list:
  abs_ui_file_path = abs_ui_dir_path + file_name
  abs_py_file_path = abs_py_dir_path + file_name.replace('.ui', '.py')
  try:
    command = ["pyuic5", "-x", abs_ui_file_path, "-o", abs_py_file_path]
    subprocess.call(command)
  except Exception as error:
    print(error)
    exit(-1)
print("[ DONE ]")