import os, subprocess

files = [ "MainWindow",
          "ManageDrugsWindow",
          "IssueLogWindow",
          "DrugUpdatingWindow",
          "DrugAddingWindow",
          "DrugIssuingWindow",
          "DelDrugWindow",
          "LoginWindow",
          "ManageProhibitionsWindow",
          "ProhibitionAddingWindow",
          "ManageManufacturersWindow",
          "ManufacturerAddingWindow",
          "ManufacturerUpdatingWindow",
          "ManageSuppliersWindow",
          "SupplierAddingWindow",
          "SupplierUpdatingWindow",
          "DeliveryLogWindow",
          "DeleteProhibitionWindow"
          ]

ui_folder_path = os.path.abspath('./ui').replace('\\', '/') + '/'
py_folder_path = os.path.abspath('./').replace('\\', '/') + '/'
for file_name in files:
  ui_file_path = ui_folder_path + file_name + '.ui'
  py_file_path = py_folder_path + file_name + '.py'
  # print(ui_file_path)
  # print(py_file_path)
  try:
    command = ["pyuic5", "-x", ui_file_path, "-o", py_file_path]
    # print(command)
    subprocess.call(command)
  except Exception as error:
    print(error)
    exit(-1)
print("[ DONE ]")