import pandas as pd 

# lire un fichier html

simpsons = pd.read_html('https://fr.wikipedia.org/wiki/Liste_des_%C3%A9pisodes_des_Simpson')
# this returns all the list in the html file.
print(len(simpsons)) # 36
# copy the value of the simpsons var in a text file


# Open the text file in write mode
file_path = "./simpsons.txt"
file_mode = "w"
encoding = "utf-8"

file = open(file_path, file_mode, encoding=encoding)

for table in simpsons:
    try:
        table_str = "\t".join(str(item) for item in table)  # Convert each element to a string
        file.write(table_str + "\n")  # Write the table string to the file with a newline character
    except UnicodeEncodeError:
       # Handle the encoding error by replacing or ignoring the problematic characters
        table_str = "\t".join(str(item).encode(encoding, errors='ignore').decode(encoding) for item in table)
        file.write(table_str + "\n")
file.close()