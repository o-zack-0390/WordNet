import copy
import os
 
def read_file():
  global dir_list
  global file_list
  root = './data'
  list = []
  
  for directory in os.listdir(root):

    if os.path.isdir(os.path.join(root, directory)):
      dir_list.append(directory)
      path = './data' + '/' + directory

      for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
          list.append(file)
      
      file_list.append(copy.copy(list))
      list.clear()
  
  print(dir_list)


dir_list  = []
file_list = []
read_file()
dir_size  = len(dir_list)

for index in range(dir_size):
  path3    = "data/" + dir_list[index] + '/' + file_list[index][2]
  f  = open(path3, 'w', encoding="utf-8", newline='')
  f.write('')
f.close()
