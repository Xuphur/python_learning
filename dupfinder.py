import hashlib as hl
import os
from tkinter import Tk, filedialog
from tkinter.filedialog import askdirectory

uniq_files = []
dup_files = []

Tk().withdraw()
# del_path = askdirectory(title='Select Del Folder')
file_path = filedialog.askopenfilename()
# keep_path = askdirectory(title='Select Keep Folder')

print (file_path)

# del_list = os.walk(del_path)
# # keep_list = os.walk(keep_path)


# def delete_file():
#   try:
#     for folder, subfolder, files in del_list:
#       del_files = files
#       for file in del_files:
#           if file in uniq_files:
#             dup_files.append(file)
#             print (f'dup file found = {file}')
#           else:
#             uniq_files.append(file)
#     for file in dup_files:
#       del_file = "".join(del_path+"/"+file)
#       if os.path.exists(del_file):
#         os.remove(del_file)
#         print (f'removed: {del_file}')
#   except OSError as e:
#    pass
#    print (e)


# try:
#   delete_file()
#   print (f'total uniq files = {len(uniq_files)}')
#   print (f'total dup files = {len(dup_files)}')
# except Exception as e:
#   print (e)


