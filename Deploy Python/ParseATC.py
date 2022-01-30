import re

fileDATA = []
atcDATA = {}

with open('./ATC1.ttl', 'r') as f:
    fileDATA = f.readlines()

def getAtc():
    if fileDATA[l].startswith('\tskos:prefLabel'):
      name = re.search('\tskos:prefLabel \"*([a-zA-Z., -]+)\"*.+', fileDATA[l])
      if name:
        name = name.group(1)
        if fileDATA[l+1] != "\n":
          code = re.search('\tskos:notation \"*([A-Za-z0-9]+)\"*.+', fileDATA[l+1])
        else:
          code = re.search('\tskos:notation \"*([A-Za-z0-9]+)\"*.+', fileDATA[l-1])
        if code:
          code = code.group(1)
          return [code, name]
        else:
          return 0

for l in range(0, len(fileDATA)-1):
    codeName = getAtc()
    if not codeName:
      continue
    code = codeName[0]
    name = codeName[1]
    if len(code) == 1:
      atcDATA[code] = {'name':name}

for l in range(0, len(fileDATA)-1):
  codeName = getAtc()
  if not codeName:
    continue
  code = codeName[0]
  name = codeName[1]
  if len(code) == 3:
    lvl1Code = code[0]
    # lvl2Code = code[1:3]
    for key1, value1 in atcDATA.items():
      if key1 != 'name' and lvl1Code == key1[0]:
        value1[code] = {'name':name}

for l in range(0, len(fileDATA)-1):
    codeName = getAtc()
    if not codeName:
      continue
    code = codeName[0]
    name = codeName[1]
    if len(code) == 4:
      lvl1Code = code[0]
      lvl2Code = code[1:3]
      # lvl3Code = code[3]
      for key1, value1 in atcDATA.items():
        if key1 != 'name' and lvl1Code == key1[0]:
          for key2, value2 in value1.items():
            if key2 != 'name' and lvl2Code == key2[1:3]:
              value2[code] = {'name':name}

for l in range(0, len(fileDATA)-1):
    codeName = getAtc()
    if not codeName:
      continue
    code = codeName[0]
    name = codeName[1]
    if len(code) == 5:
      lvl1Code = code[0]
      lvl2Code = code[1:3]
      lvl3Code = code[3]
      # lvl4Code = code[4]
      for key1, value1 in atcDATA.items():
        if key1 != 'name' and lvl1Code == key1[0]:
          for key2, value2 in value1.items():
            if key2 != 'name' and lvl2Code == key2[1:3]:
              for key3, value3 in value2.items():
                if key3 != 'name' and lvl3Code == key3[3]:
                  value3[code] = {'name':name}

for l in range(0, len(fileDATA)-1):
    codeName = getAtc()
    if not codeName:
      continue
    code = codeName[0]
    name = codeName[1]
    if len(code) == 7:
      lvl1Code = code[0]
      lvl2Code = code[1:3]
      lvl3Code = code[3]
      lvl4Code = code[4]
      # lvl5Code = code[5:]
      for key1, value1 in atcDATA.items():
        if key1 != 'name' and lvl1Code == key1[0]:
          for key2, value2 in value1.items():
            if key2 != 'name' and lvl2Code == key2[1:3]:
              for key3, value3 in value2.items():
                if key3 != 'name' and lvl3Code == key3[3]:
                  for key4, value4 in value3.items():
                    if key4 != 'name' and lvl4Code == key4[4]:
                      value4[code] = {'name':name}

with open('./sql/atc_f.sql', 'w+') as f:
  for key1, value1 in atcDATA.items():
    print("CODE: {}  NAME: {}".format(key1, value1.get('name')))
    f.write("INSERT INTO atc_anatomical_gr (atc_code, name) values ('{}','{}');\n".format(
      key1,
      value1.get('name')))
    for key2, value2 in value1.items():
      if (key2 != 'name'):
        print("  CODE: {}  NAME: {}".format(key2, value2.get('name')))
        f.write("INSERT INTO atc_therapeutic_subgr (atc_code, name, atc_anatomical_gr_id) values ('{}', '{}', ({}));\n".format(
          key2,
          value2.get('name'),
          "SELECT id FROM atc_anatomical_gr WHERE atc_code='{}'".format(key1)))
        for key3, value3 in value2.items():
          if (key3 != 'name'):
            print("    CODE: {}  NAME: {}".format(key3, value3.get('name')))
            f.write("INSERT INTO atc_pharmacological_subgr (atc_code, name, atc_therapeutic_subgr_id) "+
                    "values ('{}', '{}', ({}));\n".format(
                      key3,
                      value3.get('name'),
                      "SELECT id FROM atc_therapeutic_subgr WHERE atc_code='{}'".format(key2)))
            for key4, value4 in value3.items():
              if (key4 != 'name'):
                print("      CODE: {}  NAME: {}".format(key4, value4.get('name')))
                f.write("INSERT INTO atc_chemical_subgr (atc_code, name, atc_pharmacological_subgr_id) "+
                        "values ('{}', '{}', ({}));\n".format(
                          key4,
                          value4.get('name'),
                          "SELECT id FROM atc_pharmacological_subgr WHERE atc_code='{}'".format(key3)))
                for key5, value5 in value4.items():
                  if (key5 != 'name'):
                    print("        CODE: {}  NAME: {}".format(key5, value5.get('name')))
                    f.write("INSERT INTO atc_chemical_substance (atc_code, name, atc_chemical_subgr_id) "+
                            "values ('{}', '{}', ({}));\n".format(
                              key5,
                              value5.get('name'),
                              "SELECT id FROM atc_chemical_subgr WHERE atc_code='{}'".format(key4)))
