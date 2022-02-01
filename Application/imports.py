import sys, os
from PyQt5              import QtCore
from dbfunc2            import *
from PyQt5.QtGui        import QMovie
from PyQt5.QtCore       import QUrl
from PyQt5.QtWidgets    import QDialog, QMainWindow, QMessageBox, QApplication
from PyQt5.QtWidgets    import QTableWidgetItem
from windows_py.MainWindow         import Ui_MainWindow
from windows_py.DrugAddingWindow   import Ui_DrugAddingWindow
from windows_py.ManageDrugsWindow  import Ui_ManageDrugsWindow
from windows_py.DrugIssuingWindow  import Ui_DrugIssuingWindow
from windows_py.DrugUpdatingWindow import Ui_DrugUpdatingWindow
from windows_py.IssueLogWindow     import Ui_IssueLogWindow
from windows_py.LoginWindow        import Ui_LoginWindow
from windows_py.ManageProhibitionsWindow   import Ui_ManageProhibitionsWindow
from windows_py.ProhibitionAddingWindow    import Ui_ProhibitionAddingWindow
from windows_py.ManageManufacturersWindow  import Ui_ManageManufacturersWindow
from windows_py.ManufacturerAddingWindow   import Ui_ManufacturerAddingWindow
from windows_py.ManufacturerUpdatingWindow import Ui_ManufacturerUpdatingWindow
from windows_py.ManageSuppliersWindow      import Ui_ManageSuppliersWindow
from windows_py.SupplierAddingWindow       import Ui_SupplierAddingWindow
from windows_py.SupplierUpdatingWindow     import Ui_SupplierUpdatingWindow
from windows_py.DeleteProhibitionWindow    import Ui_DeleteProhibitionWindow
from windows_py.DeliveryLogWindow          import Ui_DeliveryLogWindow
# from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent