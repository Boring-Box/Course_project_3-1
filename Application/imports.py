import sys, os
from PyQt5              import QtCore
from dbfunc2            import *
from PyQt5.QtGui        import QMovie
from PyQt5.QtCore       import QUrl
from PyQt5.QtWidgets    import QDialog, QMainWindow, QMessageBox, QApplication
from PyQt5.QtWidgets    import QTableWidgetItem
from MainWindow         import Ui_MainWindow
from DrugAddingWindow   import Ui_DrugAddingWindow
from ManageDrugsWindow  import Ui_ManageDrugsWindow
from DrugIssuingWindow  import Ui_DrugIssuingWindow
from DrugUpdatingWindow import Ui_DrugUpdatingWindow
from IssueLogWindow     import Ui_IssueLogWindow
from LoginWindow        import Ui_LoginWindow
from ManageProhibitionsWindow   import Ui_ManageProhibitionsWindow
from ProhibitionAddingWindow    import Ui_ProhibitionAddingWindow
from ManageManufacturersWindow  import Ui_ManageManufacturersWindow
from ManufacturerAddingWindow   import Ui_ManufacturerAddingWindow
from ManufacturerUpdatingWindow import Ui_ManufacturerUpdatingWindow
from ManageSuppliersWindow      import Ui_ManageSuppliersWindow
from SupplierAddingWindow       import Ui_SupplierAddingWindow
from SupplierUpdatingWindow     import Ui_SupplierUpdatingWindow
from DeleteProhibitionWindow    import Ui_DeleteProhibitionWindow
from DeliveryLogWindow          import Ui_DeliveryLogWindow
# from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent