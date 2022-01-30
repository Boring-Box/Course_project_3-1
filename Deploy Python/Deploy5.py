''' This script creates (drops it and creates again if DB already exists) "pharmacy_db_Minor" database 
    in the "some_db_Major" database and fills it by data from files in "sql" directory.
'''
import psycopg2
from os.path import abspath

log_template = '  {:<30} .. {:^20} .. {:>10}'
done_msg = '[ {} ]'.format('DONE')
fail_msg = '[ {} ]'.format('FAIL')

authDB_Maj = {'dbname':'some_db_Major',
            'user':'username',
            "password":'userpassword',
            'host':'localhost'}

authDB_Min = {'dbname':'pharmacy_db_Minor',
            'user':'username',
            "password":'userpassword',
            'host':'localhost'}

deploy_files = {
  'createTables_f': abspath('./sql/createTables_f.sql'),
  'atc_f': abspath('./sql/atc_f.sql'),
  'drugs_f': abspath('./sql/drugs_f.sql'),
  'medic_ranks_f': abspath('./sql/medic_ranks_f.sql'),
  'suppliers_f': abspath('./sql/suppliers_f.sql'),
  'manufacturers_f': abspath('./sql/manufacturers_f.sql'),
  'drugs_prohibited_f': abspath('./sql/drugs_prohibited_f.sql'),
  # 'drug_supplier_f': abspath('./sql/drug_supplier_f.sql'),
  # 'drug_manufacturer_f': abspath('./sql/drug_manufacturer_f.sql'),
  # 'issued_to_medic_f': abspath('./sql/issued_to_medic_f.sql'),
  # 'users_and_privileges': abspath('./sql/users_and_privileges.sql'),
}
for key, value in deploy_files.items():
  deploy_files[key] = value.replace('\\', '/')

try:
  conn = psycopg2.connect(dbname=authDB_Maj['dbname'],
                        user=authDB_Maj['user'],
                        password=authDB_Maj['password'],
                        host=authDB_Maj['host'])
  conn.autocommit = True
  cursor = conn.cursor()
  print(log_template.format('DATABASE CONNECTING', authDB_Maj['dbname'], done_msg))

  if conn and cursor:
    try:
      toex = 'drop database {}'.format(authDB_Min['dbname'])
      cursor.execute(toex)
      print(log_template.format('DATABASE DROPPING', authDB_Min['dbname'], done_msg))
    except:
      print(log_template.format('DATABASE DROPPING', authDB_Min['dbname'], fail_msg))

    try:
      toex = 'create database {}'.format(authDB_Min['dbname'])
      cursor.execute(toex)
      print(log_template.format('DATABASE CREATING', authDB_Min['dbname'], done_msg))
    except Exception as error:
      print(log_template.format('DATABASE CREATING', authDB_Min['dbname'], fail_msg))
      print(error)
    finally:
      cursor.close()
      conn.close()
      print(log_template.format('DATABASE DISCONNECTING', authDB_Maj['dbname'], done_msg))

except Exception as error:
  print(log_template.format('DATABASE CONNECTING', authDB_Maj['dbname'], fail_msg))
  print(error)
  exit(-1)

try:
  conn = psycopg2.connect(dbname=authDB_Min['dbname'],
                        user=authDB_Min['user'],
                        password=authDB_Min['password'],
                        host=authDB_Min['host'])
  conn.autocommit = True
  cursor = conn.cursor()
  print(log_template.format('DATABASE CONNECTING', authDB_Min['dbname'], done_msg))

  if conn and cursor:
    try:
      currentFile = ''
      for f, f_path in deploy_files.items():
        currentFile = f
        with open(f_path, 'r+') as q:
          toex = q.read()
          cursor.execute(toex)
          print(log_template.format('EXECUTING FILE', currentFile, done_msg))
    except Exception as error:
      print(log_template.format('EXECUTING FILE', currentFile, fail_msg))
      print(error)
    finally:
      cursor.close()
      conn.close()
      print(log_template.format('DATABASE DISCONNECTING', authDB_Min['dbname'], done_msg))

except Exception as error:
  print(log_template.format('DATABASE CONNECTING', authDB_Min['dbname'], fail_msg))
  print(error)
  exit(-1)