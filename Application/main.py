from imports import *

authDict = {'dbname':'dbname',
            'user':'username',
            'password':'password',
            'host':'localhost',
            'port': 5432,
            'conn_state': False,
            'sslmode':'require'}

class LoginWindow(QDialog):
  def __init__(self):
    super().__init__()
    self.ui = Ui_LoginWindow()
    self.ui.setupUi(self)
    self.init_UI()
  
  def init_UI(self):
    self.ui.permit_btn.clicked.connect(self.login)

  def login(self):
    db_name = self.ui.dbname_fld.text()
    user_name = self.ui.username_fld.text()
    password = self.ui.password_fld.text()
    host = self.ui.host_fld.text()
    if db_name!='' or user_name!='' or password!='' or host!='':
      authDict.update({'dbname': db_name, 'user': user_name, 'password': password, 'host': host})
      if connectToDB(authDict) == -1:
        error = Troubleshoot()
        error.showError("[!] FAIL")
      else:
        authDict.update({'conn_state': True})
        self.close()
    else:
      error = Troubleshoot()
      error.showError("[!] One or more fields are blank.")

class Troubleshoot():
  def __init__(self):
    super().__init__()
  def showError(self, message):
    error = QMessageBox()
    error.setWindowTitle("Error")
    error.setText(message)
    error.setIcon(QMessageBox.Warning)
    error.setStandardButtons(QMessageBox.Ok)
    error.exec_()
  
  def showDone(self, message):
    done = QMessageBox()
    done.setWindowTitle("Done")
    done.setText(message)
    done.setStandardButtons(QMessageBox.Ok)
    done.exec_()

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
    # self.player = QMediaPlayer()
    self.init_UI()

  def init_UI(self):
    self.open_LoginWindow()
    if authDict['conn_state'] == False:
      sys.exit()
    self.show()
    # self.playMusic()
    # self.playGif()
    self.ui.add_drugs_btn.clicked.connect(self.open_DrugAddingWindow)
    self.ui.manage_drugs_btn.clicked.connect(self.open_ManageDrugsWindow)
    self.ui.issue_log_btn.clicked.connect(self.open_IssueLogWindow)
    self.ui.manage_prohihbition_list_btn.clicked.connect(self.open_ManageProhibitionsWindow)
    self.ui.add_prohibition_btn.clicked.connect(self.open_ProhibitionAddingWindow)
    self.ui.manage_manufacturers_btn.clicked.connect(self.open_ManageManufacturersWindow)
    self.ui.add_manufacturers_btn.clicked.connect(self.open_ManufacturerAddingWindow)
    self.ui.manage_suppliers_btn.clicked.connect(self.open_ManageSuppliersWindow)
    self.ui.add_suppliers_btn.clicked.connect(self.open_SupplierAddingWindow)
    self.ui.delivery_log_btn.clicked.connect(self.open_DeliveryLogWindow)
    # self.closeEvent.connect(sys.exit)

  def open_ProhibitionAddingWindow(self):
    self.f = ProhibitionAddingWindow()
    self.f.show()
  def open_LoginWindow(self):
    self.f = LoginWindow()
    self.f.exec_()
  def open_DeliveryLogWindow(self):
    self.f = DeliveryLogWindow()
    self.f.show()
  # def playMusic(self):
  #   # full_path = os.path.join(os.getcwd(), '/media/music.mp3')
  #   full_path = os.path.abspath('./media/music.mp3').replace('\\', '/')
  #   # print(full_path)
  #   url = QUrl.fromLocalFile(full_path)
  #   content = QMediaContent(url)
  #   self.player.setMedia(content)
  #   self.player.play()
  # def playGif(self):
  #   movie = QMovie('./media/dog.gif')
  #   movie.setSpeed(100) #83
  #   self.ui.DogLabel.setMovie(movie)
  #   movie.start()
  def open_DrugAddingWindow(self):
    self.f = DrugAddingWindow()
    self.f.show()
  def open_ManageDrugsWindow(self):
    self.f = ManageDrugsWindow()
    self.f.show()
  def open_IssueLogWindow(self):
    self.f = IssueLogWindow()
    self.f.show()
  def open_ManageProhibitionsWindow(self):
    self.f = ManageProhibitionsWindow()
    self.f.show()
  def open_ManageManufacturersWindow(self):
    self.f = ManageManufacturersWindow()
    self.f.show()
  def open_ManufacturerAddingWindow(self):
    self.f = ManufacturerAddingWindow()
    self.f.show()
  def open_ManageSuppliersWindow(self):
    self.f = ManageSuppliersWindow()
    self.f.show()
  def open_SupplierAddingWindow(self):
    self.f = SupplierAddingWindow()
    self.f.show()

class ManageDrugsWindow(QDialog):
  def __init__(self):
    super().__init__()
    self.ui = Ui_ManageDrugsWindow()
    self.ui.setupUi(self)
    self.init_UI()
  
  def init_UI(self):
    self.ui.tableWidget.setColumnWidth(0, 100)
    self.ui.tableWidget.setColumnWidth(1, 655)
    self.ui.tableWidget.setColumnWidth(2, 80)
    self.ui.tableWidget.setColumnWidth(3, 95)
    self.fillTable(get_all_drugs(authDict))
    self.ui.search_btn.clicked.connect(self.findRecords)
    self.ui.refresh_btn.clicked.connect(self.refresh)
    self.ui.add_drug_btn.clicked.connect(self.open_DrugAddingWindow)
    self.ui.issue_drug_btn.clicked.connect(self.open_DrugIssuingWindow)
    self.ui.update_drug_btn.clicked.connect(self.open_DrugUpdatingWindow)
  
  def open_DrugAddingWindow(self):
    self.f = DrugAddingWindow()
    self.f.show()
  def open_DrugIssuingWindow(self):
    self.f = DrugIssuingWindow()
    self.f.show()
  def open_DrugUpdatingWindow(self):
    self.f = DrugUpdatingWindow()
    self.f.show() 
  def findRecords(self):
    drug_name = self.ui.search_fld.text()
    drug_atc = self.ui.drug_atc.text()
    res = find_drugs(authDict, drug_name, drug_atc)
    if res != 0:
      self.fillTable(res)
    elif res == -1:
      error = Troubleshoot()
      error.showError("[!] Error connecting to database.")
    else:
      error = Troubleshoot()
      error.showError("Nothing was found...")
  def refresh(self):
    self.close()
    self.f = ManageDrugsWindow()
    self.f.show()
    # self.fillTable(get_all_drugs())
  def fillTable(self, data):
    # self.ui.tableWidget.setSortingEnabled(True)
    # print(data)
    if data != 0:
      self.ui.tableWidget.setRowCount(len(data))
      row = 0
      for tup in data:
        col = 0
        for item in tup:
          cellinfo = QTableWidgetItem(str(item))
          if col == 0 or col == 3:
            cellinfo = QTableWidgetItem()
            cellinfo.setData(QtCore.Qt.DisplayRole, item)
            cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ui.tableWidget.setItem(row, col, cellinfo)
          else:
            cellinfo = QTableWidgetItem(str(item))
            cellinfo.setData(QtCore.Qt.DisplayRole, item)
            cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ui.tableWidget.setItem(row, col, cellinfo)
          col += 1
        row += 1

class DrugAddingWindow(QDialog):
  def __init__(self):
    super().__init__()
    self.ui = Ui_DrugAddingWindow()
    self.ui.setupUi(self)
    self.init_UI()
  
  def init_UI(self):
    for tup in get_all_manufacturers(authDict):
      self.ui.manufacturerComboBox.addItem("{} {}".format(tup[0], tup[1]))
    for tup in get_all_suppliers(authDict):
      self.ui.supplierComboBox.addItem("{} {}".format(tup[0], tup[1]))
    self.ui.add_drug_btn.clicked.connect(self.insertData)
    self.ui.manufacturer_is_supplier_checkbox.stateChanged.connect(self.changeSuppliersCBoxState)

  def changeSuppliersCBoxState(self):
    state = self.ui.supplierComboBox.isEnabled()
    self.ui.supplierComboBox.setEnabled(not state)
  def insertData(self):
    inputCorrect = True
    error_message = ""
    name = self.ui.inputline_drug_name.text()
    atc = self.ui.inputline_drug_atc.text()
    quantity = self.ui.quantity_spnbox.text()
    descr = self.ui.inputline_drug_description.toPlainText()
    drug_id = ''

    manufacturer_id_name = (self.ui.manufacturerComboBox.currentText()).split(' ')
    supplier_id_name = (self.ui.supplierComboBox.currentText()).split(' ')
    manufacturer_is_supplier = self.ui.manufacturer_is_supplier_checkbox.isChecked()
    manufacturer_id = ''
    manufacturer_name = ''
    supplier_id = ''
    supplier_name = ''
    whith_supplier_exists = False
    whith_manufacturer_exists = False
    absolutely_new_drug = False

    if name == '':
      inputCorrect = False
      error_message += '[!] Drug name field is blank.\n'
    
    if atc != '':
      if check_atc_chemical_substance(authDict, atc) == 0:
        inputCorrect = False
        error_message += '[!] ATC "{}" doesn\'t exists in database.\n'.format(atc.upper())
    else:
      inputCorrect = False
      error_message += '[!] ATC field is blank.\n'

    if manufacturer_id_name != ['']:
      manufacturer_id = manufacturer_id_name[0]
      manufacturer_name = manufacturer_id_name[1]
    else:
      inputCorrect = False
      error_message += '[!] Manufacturer is not selected.\n'

    if manufacturer_is_supplier == False:
      if supplier_id_name != ['']:
        supplier_id = supplier_id_name[0]
        supplier_name = supplier_id_name[1]
      else:
        inputCorrect = False
        error_message += '[!] Supplier is not selected.\n'
    elif manufacturer_is_supplier == True and manufacturer_id_name != ['']:
      supplier_id, supplier_name = manufacturer_id, manufacturer_name

    if descr == '':
      descr = "Some description."
    if check_drugs(authDict, name, atc) == 0:
      absolutely_new_drug = True

    if inputCorrect:
      res = 1
      res1 = 1
      res2 = 1
      if absolutely_new_drug:
        res = insert_drugs(authDict, name, atc, quantity, descr)
      else:
        drug_data = get_drug(authDict, name, atc)
        drug_id = str(drug_data[0][0])
        current_quantity = int(drug_data[0][3])
        updated_quantity = str(current_quantity + int(quantity))
        res = update_drugs(authDict, drug_id, quantity=updated_quantity)
        if check_drugs(authDict, name, atc, manufacturer_id) == 1:
          whith_manufacturer_exists = True
        if check_drugs(authDict, name, atc, supplier_id=supplier_id) == 1:
          whith_supplier_exists = True
      
      drug_data = get_drug(authDict, name, atc)
      # print(drug_data)
      if drug_data!=0:
        drug_id = str(drug_data[0][0])
      if whith_manufacturer_exists == False:
        res1 = insert_drug_manufacturer(authDict, drug_id, manufacturer_id)
      if whith_supplier_exists == False:
        res2 = insert_drug_supplier(authDict, drug_id, supplier_id)
      # get_drug(authDict, name=name, atc=atc, descr=descr)[0][0]
      
      if res == 1 and res1 == 1 and res2 == 1:
        done_msg = "Added successfully."
        if not absolutely_new_drug:
          done_msg = "Quantity of existing drug was increased"
        self.flushFields()
        done = Troubleshoot()
        done.showDone(done_msg)
      else:
        error = Troubleshoot()
        error.showError("[!] Error connecting to database.")
    else:
      error = Troubleshoot()
      error.showError(error_message)

  def flushFields(self):
    self.ui.inputline_drug_name.setText('')
    self.ui.inputline_drug_atc.setText('')
    self.ui.quantity_spnbox.setValue(0)
    self.ui.inputline_drug_description.setPlainText('')

class DrugIssuingWindow(QDialog):
  def __init__(self):
    super().__init__()
    self.ui = Ui_DrugIssuingWindow()
    self.ui.setupUi(self)
    self.init_UI()

  def init_UI(self):
    for tup in get_all_medic_ranks(authDict):
      self.ui.rank_cbox.addItem("{} {}".format(tup[0], tup[1]))
    self.ui.issue_btn.clicked.connect(self.issueDrug)

  def issueDrug(self):
    medic_rank_id_name = (self.ui.rank_cbox.currentText()).split(' ')
    drug_id = str(self.ui.drug_id_spnbox.value())
    medic_rank_id = medic_rank_id_name[0]
    quantity = str(self.ui.quantity_spnbox.value())
    timestamp = self.ui.datetime_editor.text()
    medic_fname = self.ui.medic_fname_fld.text()
    medic_lname = self.ui.medic_lname_fld.text()
    medic_pname = self.ui.medic_patronymic_fld.text()
    inputCorrect = True
    error_message = ""
    if check_drugs(authDict, drug_id=drug_id) == 0:
      inputCorrect = False
      error_message += "[!] Wrong or not existing drug_id\n"
    elif check_drugs_prohibited(authDict, drug_id, medic_rank_id) == 1:
      inputCorrect = False
      error_message += "[!] Drug cannot be issued to this medic rank.\n"
    if quantity == '0':
      inputCorrect = False
      error_message += "[!] Quantity must not be 0.\n"
    elif int(quantity) > int(get_drug(authDict, drug_id=drug_id)[0][3]):
      inputCorrect = False
      error_message += "[!] There are not enough drugs in stock.\n"
    if medic_fname == '' or medic_lname == '' or medic_pname == '':
      inputCorrect = False
      error_message += "[!] One or more of the medic name fields is blank.\n"
    if medic_rank_id == '' or medic_rank_id == None:
      inputCorrect = False
      error_message += "[!] Medic rank field is blank.\n"
    if inputCorrect:
      res1 = writeoff_drugs(authDict, drug_id, quantity)
      res2 = insert_issued_to_medic(authDict, drug_id, medic_rank_id, quantity, timestamp, medic_fname, medic_lname, medic_pname)
      if res1 == -1 and res2 == -1:
        error = Troubleshoot()
        error.showError("[!] Error connecting to database.")
      else:
        self.flushFields()
        done = Troubleshoot()
        done.showDone("Issued successfully.")
    else:
      error = Troubleshoot()
      error.showError(error_message)
  def flushFields(self):
    self.ui.drug_id_spnbox.setValue(0)
    self.ui.medic_fname_fld.setText('')
    self.ui.medic_lname_fld.setText('')
    self.ui.medic_patronymic_fld.setText('')
    self.ui.quantity_spnbox.setValue(0)

class DrugUpdatingWindow(QDialog):
  def __init__(self):
    super().__init__()
    self.ui = Ui_DrugUpdatingWindow()
    self.ui.setupUi(self)
    self.init_UI()

  def init_UI(self):
    self.ui.get_data_drug_btn.clicked.connect(self.getData)
    self.ui.update_drug_btn.clicked.connect(self.updateDrug)

  def getData(self):
    drug_id = self.ui.drug_id_spnbox.text()
    data = get_drug(authDict, drug_id=drug_id)
    if data != 0:
      self.ui.drug_name_fld.setText(data[0][1])
      self.ui.drug_atc_fld.setText(data[0][2])
      self.ui.quantity_spnbox.setValue(int(data[0][3]))
      self.ui.drug_description_fld.setPlainText(data[0][4])
    else:
      error = Troubleshoot()
      error.showError("There is no drug with this ID.")
    
  def updateDrug(self):
    drug_id = self.ui.drug_id_spnbox.text()
    drug_name = self.ui.drug_name_fld.text()
    drug_atc = self.ui.drug_atc_fld.text()
    drug_quantity = str(self.ui.quantity_spnbox.value())
    drug_description = self.ui.drug_description_fld.toPlainText()

    inputCorrect = True
    error_message = ''
    if drug_name == '':
      inputCorrect = False
      error_message += 'Drug name field is blank.\n'
    
    if drug_atc != '':
      if check_atc_chemical_substance(authDict, drug_atc) == 0:
        inputCorrect = False
        error_message += 'ATC "{}" doesn\'t exists in database.\n'.format(drug_atc.upper())
    else:
      inputCorrect = False
      error_message += 'ATC field is blank.\n'
    
    if drug_description == '':
      drug_description = "Some description."
    
    if inputCorrect:
      res = update_drugs(authDict, drug_id, drug_name, drug_atc, drug_quantity, drug_description)
      if res == 1:
        done = Troubleshoot()
        done.showDone("Updated successfully.")
      elif res == -1:
        error = Troubleshoot()
        error.showError("[!] Error connecting to database.")
      else:
        error = Troubleshoot()
        error.showError("[!] Something wrong...")
    else:
      error = Troubleshoot()
      error.showError(error_message)

class IssueLogWindow(QDialog):
  def __init__(self):
    super().__init__()
    self.ui = Ui_IssueLogWindow()
    self.ui.setupUi(self)
    self.init_UI()
  def init_UI(self):
    self.ui.tableWidget.setColumnWidth(0, 150)
    self.ui.tableWidget.setColumnWidth(1, 400)
    self.ui.tableWidget.setColumnWidth(2, 80)
    self.ui.tableWidget.setColumnWidth(3, 325)
    self.ui.tableWidget.setColumnWidth(4, 320)
    self.fillTable(find_issued_to_medic(authDict))
    self.ui.search_btn.clicked.connect(self.findRecords)
    self.ui.refresh_btn.clicked.connect(self.refresh)
  
  def refresh(self):
    self.close()
    self.f = IssueLogWindow()
    self.f.show()
  def findRecords(self):
    drug_name = self.ui.search_drug_fld.text()
    fname = self.ui.medic_fname_fld.text()
    lname = self.ui.medic_lname_fld.text()
    pname = self.ui.medic_patronymic_fld.text()
    from_date = self.ui.datetime_editor_from.text()
    to_date = self.ui.datetime_editor_to.text()
    res = find_issued_to_medic(authDict, drug_name, fname, lname, pname, from_date, to_date)
    # print(res)
    if res != 0:
      self.fillTable(res)
    elif res == -1:
      error = Troubleshoot()
      error.showError("[!] Error connecting to database.")
    else:
      error = Troubleshoot()
      error.showError("[!] Nothing was found...")
  def fillTable(self, data):
    if data != 0:
      self.ui.tableWidget.setRowCount(len(data))
      row = 0
      for tup in data:
        col = 0
        for i in range(0, len(tup)):
          cellinfo = QTableWidgetItem()
          if col == 0 or col == 1:
            cellinfo.setData(QtCore.Qt.DisplayRole, str(tup[i]))
            cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ui.tableWidget.setItem(row, col, cellinfo)
          if col == 2:
            cellinfo = QTableWidgetItem()
            cellinfo.setData(QtCore.Qt.DisplayRole, tup[i])
            cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ui.tableWidget.setItem(row, col, cellinfo)
          elif col == 3:
            insertinfo = "{} {} {}".format(str(tup[i+1]), str(tup[i]), str(tup[i+2]))
            cellinfo.setData(QtCore.Qt.DisplayRole, insertinfo)
            cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ui.tableWidget.setItem(row, col, cellinfo)
            i = 5
          elif col == 4:
            # cellinfo = QTableWidgetItem()
            cellinfo.setData(QtCore.Qt.DisplayRole, str(tup[6]))
            cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ui.tableWidget.setItem(row, col, cellinfo)
          col += 1
        row += 1

class DeliveryLogWindow(QDialog):
  def __init__(self):
    super().__init__()
    self.ui = Ui_DeliveryLogWindow()
    self.ui.setupUi(self)
    self.init_UI()
  def init_UI(self):
    self.ui.tableWidget.setColumnWidth(0, 100)
    self.ui.tableWidget.setColumnWidth(1, 400)
    self.ui.tableWidget.setColumnWidth(2, 100)
    self.ui.tableWidget.setColumnWidth(3, 200)
    self.ui.tableWidget.setColumnWidth(4, 200)
    self.ui.tableWidget.setColumnWidth(5, 100)
    self.ui.tableWidget.setColumnWidth(6, 200)
    self.ui.tableWidget.setColumnWidth(7, 200)
    self.fillTable(find_delivery_log(authDict))
    self.ui.search_btn.clicked.connect(self.findRecords)
    self.ui.refresh_btn.clicked.connect(self.refresh)

  def refresh(self):
    self.close()
    self.f = DeliveryLogWindow()
    self.f.show()
  def findRecords(self):
    drug_name = self.ui.search_drug_fld.text()
    manufacturer_name = self.ui.manufacturer_name_fld.text()
    manufacturer_country = self.ui.manufacturer_country_fld.text()
    supplier_name = self.ui.supplier_name_fld.text()
    supplier_country = self.ui.supplier_country_fld.text()
    res = find_delivery_log(authDict, drug_name, manufacturer_name, manufacturer_country, supplier_name, supplier_country)
    # print(res)
    if res != 0:
      self.fillTable(res)
    elif res == -1:
      error = Troubleshoot()
      error.showError("[!] Error connecting to database.")
    else:
      error = Troubleshoot()
      error.showError("[!] Nothing was found...")
  def fillTable(self, data):
    if data != 0:
      self.ui.tableWidget.setRowCount(len(data))
      row = 0
      for tup in data:
        col = 0
        for item in tup:
          cellinfo = QTableWidgetItem(str(item))
          if col == 0 or col == 2 or col == 4:
            cellinfo = QTableWidgetItem()
            cellinfo.setData(QtCore.Qt.DisplayRole, item)
            cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ui.tableWidget.setItem(row, col, cellinfo)
          else:
            cellinfo = QTableWidgetItem(str(item))
            cellinfo.setData(QtCore.Qt.DisplayRole, item)
            cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ui.tableWidget.setItem(row, col, cellinfo)
          col += 1
        row += 1

class ManageProhibitionsWindow(QDialog):
  def __init__(self):
    super().__init__()
    self.ui = Ui_ManageProhibitionsWindow()
    self.ui.setupUi(self)
    self.init_UI()
  def init_UI(self):
    self.ui.tableWidget.setColumnWidth(0, 150)
    self.ui.tableWidget.setColumnWidth(1, 563)
    self.ui.tableWidget.setColumnWidth(2, 563)
    self.fillTable(find_drugs_prohibited(authDict))
    for tup in get_all_medic_ranks(authDict):
      self.ui.rank_cbox.addItem("{} {}".format(tup[0], tup[1]))
    self.ui.search_btn.clicked.connect(self.findRecords)
    self.ui.refresh_btn.clicked.connect(self.refresh)
    self.ui.add_prohibition_btn.clicked.connect(self.open_AddProhibitionWindow)
    self.ui.delete_prohibition_btn.clicked.connect(self.open_DeleteProhibitionWindow)

  def refresh(self):
    self.close()
    self.f = ManageProhibitionsWindow()
    self.f.show()
  def findRecords(self):
    drug_name = self.ui.search_drug_fld.text()
    medic_rank_id_name = ''
    medic_rank_id = ''
    medic_rank_name = ''
    if self.ui.rank_cbox.currentText() != '':
      medic_rank_id_name = (self.ui.rank_cbox.currentText()).split(' ')
      medic_rank_id = medic_rank_id_name[0]
      medic_rank_name = medic_rank_id_name[1]
    res = find_drugs_prohibited(authDict, drug_name, medic_rank_id)
    # print(res)
    if res != 0:
      self.fillTable(res)
    elif res == -1:
      error = Troubleshoot()
      error.showError("[!] Error connecting to database.")
    else:
      error = Troubleshoot()
      error.showError("[!] Nothing was found...")
  def fillTable(self, data):
    # self.ui.tableWidget.setSortingEnabled(True)
    # print(data)
    if data != 0:
      self.ui.tableWidget.setRowCount(len(data))
      row = 0
      for tup in data:
        col = 0
        for item in tup:
          cellinfo = QTableWidgetItem(str(item))
          if col == 0:
            cellinfo = QTableWidgetItem()
            cellinfo.setData(QtCore.Qt.DisplayRole, item)
            cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ui.tableWidget.setItem(row, col, cellinfo)
          else:
            cellinfo = QTableWidgetItem(str(item))
            cellinfo.setData(QtCore.Qt.DisplayRole, item)
            cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ui.tableWidget.setItem(row, col, cellinfo)
          col += 1
        row += 1
  def open_AddProhibitionWindow(self):
    self.f = ProhibitionAddingWindow()
    self.f.show()
  def open_DeleteProhibitionWindow(self):
    self.f = DeleteProhibitionWindow()
    self.f.show()

class DeleteProhibitionWindow(QDialog):
  def __init__(self):
    super().__init__()
    self.ui = Ui_DeleteProhibitionWindow()
    self.ui.setupUi(self)
    self.init_UI()
  def init_UI(self):
    self.ui.del_prohibition_btn.clicked.connect(self.deleteProhibition)

  def deleteProhibition(self):
    inputCorrect = True
    error_message = ""
    prohibition_id = self.ui.prohibition_id_spnbox.text()
    res = check_drugs_prohibited(authDict, prohibition_id=prohibition_id)
    if res == 0:
      inputCorrect = False
      error_message += '[!] Prohibition ID doesn\'t exists in Data base\n'
    if inputCorrect:
      res = delete_drugs_prohibited(authDict, prohibition_id)
      if res == 1:
        done = Troubleshoot()
        done.showDone("Done.")
      if res == -1:
        error = Troubleshoot()
        error.showError("[!] Error connecting to database.")
    else:
      error = Troubleshoot()
      error.showError(error_message)

class ProhibitionAddingWindow(QDialog):
  def __init__(self):
    super().__init__()
    self.ui = Ui_ProhibitionAddingWindow()
    self.ui.setupUi(self)
    self.init_UI()
  def init_UI(self):
    for tup in get_all_medic_ranks(authDict):
      self.ui.rank_cbox.addItem("{} {}".format(tup[0], tup[1]))
    self.ui.add_prohibition_btn.clicked.connect(self.addProhibition)
  
  def addProhibition(self):
    inputCorrect = True
    error_message = ""

    medic_rank_id_name = []
    medic_rank_id = ''
    drug_id = self.ui.drug_id_spnbox.text()
    if check_drugs(authDict, drug_id=drug_id) == 0:
      inputCorrect = False
      error_message += "[!] Wrong or not existing drug_id\n"
    if self.ui.rank_cbox.currentText() != '':
      medic_rank_id_name = (self.ui.rank_cbox.currentText()).split(' ')
      medic_rank_id = medic_rank_id_name[0]
      if check_drugs_prohibited(authDict, drug_id, medic_rank_id) == 1:
        inputCorrect = False
        error_message +="[!] Record already exists.\n"
    else:
      inputCorrect = False
      error_message += "[!] Medic rank field is blank.\n"
    
    
    if inputCorrect:
      res = insert_drugs_prohibited(authDict, drug_id, medic_rank_id)
      if res == 1:
        done = Troubleshoot()
        done.showDone("Done.")
      else:
        error = Troubleshoot()
        error.showError("[!] Something wrong.")
    else:
      error = Troubleshoot()
      error.showError(error_message)

class ManageManufacturersWindow(QDialog):
  def __init__(self):
    super().__init__()
    self.ui = Ui_ManageManufacturersWindow()
    self.ui.setupUi(self)
    self.init_UI()

  def init_UI(self):
    self.ui.tableWidget.setColumnWidth(0, 100)
    self.ui.tableWidget.setColumnWidth(1, 600)
    self.ui.tableWidget.setColumnWidth(2, 285)
    self.fillTable(find_manufacturers(authDict))
    self.ui.search_btn.clicked.connect(self.findRecords)
    self.ui.add_manufacturer_btn.clicked.connect(self.open_ManufacturerAddingWindow)
    self.ui.update_manufacturer_btn.clicked.connect(self.open_ManufacturerUpdatingWindow)
    self.ui.refresh_btn.clicked.connect(self.refresh)

  def refresh(self):
    self.close()
    self.f = ManageManufacturersWindow()
    self.f.show()
  def findRecords(self):
    manufacturer_name = self.ui.search_manufacturer_fld.text()
    country = self.ui.search_country_fld.text()
    res = find_manufacturers(authDict, manufacturer_name, country)
    # print(res)
    if res != 0:
      self.fillTable(res)
    elif res == -1:
      error = Troubleshoot()
      error.showError("[!] Error connecting to database.")
    else:
      error = Troubleshoot()
      error.showError("[!] Nothing was found...")
  def fillTable(self, data):
    # self.ui.tableWidget.setSortingEnabled(True)
    # print(data)
    if data != 0:
      self.ui.tableWidget.setRowCount(len(data))
      row = 0
      for tup in data:
        col = 0
        for item in tup:
          cellinfo = QTableWidgetItem(str(item))
          if col == 0:
            cellinfo = QTableWidgetItem()
            cellinfo.setData(QtCore.Qt.DisplayRole, item)
            cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ui.tableWidget.setItem(row, col, cellinfo)
          else:
            cellinfo = QTableWidgetItem(str(item))
            cellinfo.setData(QtCore.Qt.DisplayRole, item)
            cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ui.tableWidget.setItem(row, col, cellinfo)
          col += 1
        row += 1
  def open_ManufacturerAddingWindow(self):
    self.f = ManufacturerAddingWindow()
    self.f.show()
  def open_ManufacturerUpdatingWindow(self):
    self.f = ManufacturerUpdatingWindow()
    self.f.show()

class ManufacturerAddingWindow(QDialog):
  def __init__(self):
    super().__init__()
    self.ui = Ui_ManufacturerAddingWindow()
    self.ui.setupUi(self)
    self.init_UI()

  def init_UI(self):
    self.ui.add_manufacturer_btn.clicked.connect(self.addManufacturer)

  def addManufacturer(self):
    inputCorrect = True
    error_message = ""
    manufacturer_name = self.ui.manufacturer_name_fld.text()
    country = self.ui.country_fld.text()
    contact_info = self.ui.contact_info_fld.toPlainText()

    if manufacturer_name == '':
      inputCorrect = False
      error_message += '[!] Manufacturer name field is blank.\n'
    if manufacturer_name != '' and check_manufacturers(authDict, manufacturer_name, country) == 1:
      inputCorrect = False
      error_message += '[!] Record already exists in database.\n'
    if country == '':
      inputCorrect = False
      error_message += '[!] Country field is blank.\n'
    if len(contact_info) > 200:
      inputCorrect = False
      error_message += '[!] Contact info length must be less then 200\n'
    if contact_info == '':
      contact_info = "No contact info."
    if inputCorrect:
      res = insert_manufacturers(authDict, manufacturer_name, country, contact_info)
      if res == -1:
        error = Troubleshoot()
        error.showError("[!] Error connecting to database.")
      else:
        self.flushFields()
        done = Troubleshoot()
        done.showDone("Added successfully.")
    else:
      error = Troubleshoot()
      error.showError(error_message)
  def flushFields(self):
    self.ui.manufacturer_name_fld.setText('')
    self.ui.country_fld.setText('')
    self.ui.contact_info_fld.setPlainText('')

class ManufacturerUpdatingWindow(QDialog):
  def __init__(self):
    super().__init__()
    self.ui = Ui_ManufacturerUpdatingWindow()
    self.ui.setupUi(self)
    self.init_UI()
  def init_UI(self):
    self.ui.get_data_manufacturer_btn.clicked.connect(self.getData)
    self.ui.update_manufacturer_btn.clicked.connect(self.updateManufacturer)
  def getData(self):
    manufacturer_id = self.ui.manufacturer_id_spnbox.text()
    data = get_manufacturer(authDict, manufacturer_id)
    if data != 0:
      self.ui.manufacturer_name_fld.setText(data[0][1])
      self.ui.country_fld.setText(data[0][2])
      self.ui.contact_info_fld.setPlainText(data[0][3])
    else:
      error = Troubleshoot()
      error.showError("There is no manufacturer with this ID.")
  def updateManufacturer(self):
    manufacturer_id = self.ui.manufacturer_id_spnbox.text()
    manufacturer_name = self.ui.manufacturer_name_fld.text()
    manufacturer_country = self.ui.country_fld.text()
    manufacturer_contact_info = self.ui.contact_info_fld.toPlainText()

    inputCorrect = True
    error_message = ''
    if manufacturer_name == '':
      inputCorrect = False
      error_message += 'Manufacturer name field is blank.\n'
    
    if manufacturer_country == '':
        inputCorrect = False
        error_message += 'County field is blank.\n'.format(manufacturer_country.upper())
    
    if manufacturer_contact_info == '':
      manufacturer_contact_info = "No contact info."
    
    if inputCorrect:
      res = update_manufacturers(authDict, manufacturer_id, manufacturer_name, manufacturer_country, manufacturer_contact_info)
      if res == 1:
        done = Troubleshoot()
        done.showDone("Updated successfully.")
      elif res == -1:
        error = Troubleshoot()
        error.showError("[!] Error connecting to database.")
      else:
        error = Troubleshoot()
        error.showError("[!] Something wrong...")
    else:
      error = Troubleshoot()
      error.showError(error_message)

class ManageSuppliersWindow(QDialog):
  def __init__(self):
    super().__init__()
    self.ui = Ui_ManageSuppliersWindow()
    self.ui.setupUi(self)
    self.init_UI()

  def init_UI(self):
    self.ui.tableWidget.setColumnWidth(0, 100)
    self.ui.tableWidget.setColumnWidth(1, 600)
    self.ui.tableWidget.setColumnWidth(2, 285)
    self.fillTable(find_suppliers(authDict))
    self.ui.search_btn.clicked.connect(self.findRecords)
    self.ui.add_supplier_btn.clicked.connect(self.open_SupplierAddingWindow)
    self.ui.update_supplier_btn.clicked.connect(self.open_SupplierUpdatingWindow)
    self.ui.refresh_btn.clicked.connect(self.refresh)

  def refresh(self):
    self.close()
    self.f = ManageSuppliersWindow()
    self.f.show()
  def findRecords(self):
    supplier_name = self.ui.search_supplier_fld.text()
    country = self.ui.search_country_fld.text()
    res = find_suppliers(authDict, supplier_name, country)
    # print(res)
    if res != 0:
      self.fillTable(res)
    elif res == -1:
      error = Troubleshoot()
      error.showError("[!] Error connecting to database.")
    else:
      error = Troubleshoot()
      error.showError("[!] Nothing was found...")
  def fillTable(self, data):
    # self.ui.tableWidget.setSortingEnabled(True)
    # print(data)
    if data != 0:
      self.ui.tableWidget.setRowCount(len(data))
      row = 0
      for tup in data:
        col = 0
        for item in tup:
          cellinfo = QTableWidgetItem(str(item))
          if col == 0:
            cellinfo = QTableWidgetItem()
            cellinfo.setData(QtCore.Qt.DisplayRole, item)
            cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ui.tableWidget.setItem(row, col, cellinfo)
          else:
            cellinfo = QTableWidgetItem(str(item))
            cellinfo.setData(QtCore.Qt.DisplayRole, item)
            cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ui.tableWidget.setItem(row, col, cellinfo)
          col += 1
        row += 1
  def open_SupplierAddingWindow(self):
    self.f = SupplierAddingWindow()
    self.f.show()
  def open_SupplierUpdatingWindow(self):
    self.f = SupplierUpdatingWindow()
    self.f.show()

class SupplierUpdatingWindow(QDialog):
  def __init__(self):
    super().__init__()
    self.ui = Ui_SupplierUpdatingWindow()
    self.ui.setupUi(self)
    self.init_UI()
  def init_UI(self):
    self.ui.get_data_supplier_btn.clicked.connect(self.getData)
    self.ui.update_supplier_btn.clicked.connect(self.updateSupplier)
  def getData(self):
    supplier_id = self.ui.supplier_id_spnbox.text()
    data = get_supplier(authDict, supplier_id)
    if data != 0:
      self.ui.supplier_name_fld.setText(data[0][1])
      self.ui.country_fld.setText(data[0][2])
      self.ui.contact_info_fld.setPlainText(data[0][3])
    else:
      error = Troubleshoot()
      error.showError("There is no supplier with this ID.")
  def updateSupplier(self):
    supplier_id = self.ui.supplier_id_spnbox.text()
    supplier_name = self.ui.supplier_name_fld.text()
    supplier_country = self.ui.country_fld.text()
    supplier_contact_info = self.ui.contact_info_fld.toPlainText()

    inputCorrect = True
    error_message = ''
    if supplier_name == '':
      inputCorrect = False
      error_message += 'Supplier name field is blank.\n'

    if supplier_country == '':
        inputCorrect = False
        error_message += 'County field is blank.\n'.format(supplier_country.upper())
    
    if supplier_contact_info == '':
      supplier_contact_info = "No contact info."
    
    if inputCorrect:
      res = update_suppliers(authDict, supplier_id, supplier_name, supplier_country, supplier_contact_info)
      if res == 1:
        done = Troubleshoot()
        done.showDone("Updated successfully.")
      elif res == -1:
        error = Troubleshoot()
        error.showError("[!] Error connecting to database.")
      else:
        error = Troubleshoot()
        error.showError("[!] Something wrong...")
    else:
      error = Troubleshoot()
      error.showError(error_message)

class SupplierAddingWindow(QDialog):
  def __init__(self):
    super().__init__()
    self.ui = Ui_SupplierAddingWindow()
    self.ui.setupUi(self)
    self.init_UI()

  def init_UI(self):
    self.ui.add_supplier_btn.clicked.connect(self.addSupplier)

  def addSupplier(self):
    inputCorrect = True
    error_message = ""
    supplier_name = self.ui.supplier_name_fld.text()
    country = self.ui.country_fld.text()
    contact_info = self.ui.contact_info_fld.toPlainText()

    if supplier_name == '':
      inputCorrect = False
      error_message += '[!] Supplier name field is blank.\n'
    if supplier_name != '' and check_suppliers(authDict, supplier_name, country) == 1:
      inputCorrect = False
      error_message += '[!] Record already exists in database.\n'
    if country == '':
      inputCorrect = False
      error_message += '[!] Country field is blank.\n'
    if len(contact_info) > 200:
      inputCorrect = False
      error_message += '[!] Contact info length must be less then 200\n'
    if contact_info == '':
      contact_info = "No contact info."
    if inputCorrect:
      res = insert_suppliers(authDict, supplier_name, country, contact_info)
      if res == -1:
        error = Troubleshoot()
        error.showError("[!] Error connecting to database.")
      else:
        self.flushFields()
        done = Troubleshoot()
        done.showDone("Added successfully.")
    else:
      error = Troubleshoot()
      error.showError(error_message)
  def flushFields(self):
    self.ui.supplier_name_fld.setText('')
    self.ui.country_fld.setText('')
    self.ui.contact_info_fld.setPlainText('')


if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=MainWindow()
    sys.exit(app.exec_())