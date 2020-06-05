import pandas as pd
import tabula as tb
df = tb.read_pdf('Aula12/txt.pdf', pages='1')
tb.convert_into("Aula12/txt.pdf", "Aula12/output.csv", output_format="csv", pages='1')
print(df)
