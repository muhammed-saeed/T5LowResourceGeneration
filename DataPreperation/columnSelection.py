import argparse
import pandas as pd

df = pd.read_csv("/local/musaeed/NaijaDiscourseClassification/PDTBNaija/pdtb2.csv")
print(df.head())
print(df.columns)
print(f"{df['Conn1'].head()} and {df['Conn2'].head()} ")
ARG1 = df["Arg1_RawText"].tolist()
ARG2 = df["Arg2_RawText"].tolist()
FULLTEXT  = df["FullRawText"].tolist()
print(f"{FULLTEXT[4]} \n and {ARG1[4]} and \n {ARG2[4]}")


explicit_lines = df[df['Relation'] == 'Explicit']
conn1 = explicit_lines['Conn1'].tolist()
conn2 = explicit_lines['Conn2'].tolist()
Arg1 = explicit_lines['Arg1_RawText'].tolist()
Arg2 = explicit_lines['Arg2_RawText'].tolist()
connective_raw_text = explicit_lines['Connective_RawText'].tolist()
FULLTEXT  = explicit_lines["FullRawText"].tolist()

print(f"{conn1[:2]} \n {Arg1[:2]} \n {Arg2[:2]} \n {FULLTEXT[:2]} \n {conn2[:2]} \n {connective_raw_text[:2]}")

conn1 = explicit_lines['Conn1']
conn2 = explicit_lines['Conn2']
connective_raw_text = explicit_lines['Connective_RawText']
print(conn1.isna().sum().sum())
print(conn2.isna().sum().sum())
print(connective_raw_text.isna().sum().sum())