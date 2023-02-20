

import os

folder_path = r"C:\pipeline\crater-meta\lib\tk_distributed_config\apps\tk-cs-create-folders"


print('putanja ' + folder_path)
print(os.path.isdir(folder_path))



for (root,dirs,files) in os.walk(folder_path):
    for file in files:
        if file.endswith(".py"):
            print(file)
            print(root)
            putanja = os.path.join(root, file)
            print(putanja)
            if os.path.isfile(putanja) == True:
                print('Putanja je dobra, radim konverziju: ')
                os.system("python " + r"C:/Users/nikolav/Anaconda3/Scripts/futurize-script.py -w " + putanja)
                # os.system("python " + r"C:/Users/nikolav/Anaconda3/Scripts/2to3-script.py -w " + putanja)
            else: print('ne moze')
            

            
    print ('--------------------------------')

# for filename in os.listdir(folder_path):
#     print(filename)
#     if filename.endswith(".py"):
#         file_path = os.path.join(folder_path, filename)
#         print("python " + r"C:/Users/nikolav/Anaconda3/Scripts/2to3-script.py -w " + filename)
#         os.system("python " + r"C:/Users/nikolav/Anaconda3/Scripts/2to3-script.py -w " + file_path)




# def find_module(modulename, filename=None):
    
       
#     import imp
#     import sys
#     import os
#     full_path = []
#     if filename:
#         full_path.append(os.path.dirname(os.path.abspath(filename)))
#     full_path += sys.path
#     fname = imp.find_module(modulename, full_path)
#     return fname[1]
