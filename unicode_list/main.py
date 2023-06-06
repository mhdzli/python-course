# A python script to list all unicode characters
import sys
import unicodedata
txtfile = "unicode_table.txt"
print("creating file: " + txtfile)
with open(txtfile, "w", encoding="utf-8", errors='ignore') as file:
    for uc in range(sys.maxunicode):
        try:
            line = f"{str(uc)}, {chr(uc)}, \
{unicodedata.name(chr(uc)).lower()}, \
{unicodedata.category(chr(uc)).lower()}, {hex(uc)}\n"
        except ValueError:
            line = f"{str(uc)}, {chr(uc)}, none, none, {hex(uc)}\n"
        file.write(line)
