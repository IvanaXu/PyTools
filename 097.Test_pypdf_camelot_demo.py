import camelot
tables = camelot.read_pdf('097.Test_pypdf_camelot_foo.pdf')
print(tables)

tables.export('097.Test_pypdf_camelot_foo.csv', f='csv', compress=True)

print(tables[0].parsing_report)
print(tables[0].df)
