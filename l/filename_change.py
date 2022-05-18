import os
import re

import pandas as pd

dir_path = "C:/Users/kumar/Projects/GraphemeLabs/all_zip_files/OneDrive_01_5-13-2022"

file_path = "C:/Users/kumar/Projects/GraphemeLabs/testcases/orbit 1.xlsx"

df = pd.read_excel(file_path)
print(df.columns)
key_0 = df.columns[0]
key_1 = df.columns[1]

print(df)

os.chdir(dir_path)
dir_content = os.listdir('.')
print(dir_content)
for it, row in df.iterrows():
    new_name = row[key_0]
    link = row[key_1]
    project_id = re.search(r'(\d+)', new_name)
    if project_id:
        project_id = project_id.group(0)
    else:
        continue
    file_name = link.split('/')[-1]
    print(project_id, new_name, file_name)
    if os.path.exists(file_name):
        print(f"Moving {file_name} to 'Project {project_id}.xml'")
        os.rename(file_name, "Project " + str(project_id) + ".xml")
        print(f'Moved {file_name}, "Project " + {str(project_id)} + ".xml"')

