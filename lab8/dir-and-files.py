# task 1
# import os
# current = os.listdir()
# print(current)
# print(os.listdir('/Users/kamalkamalov/PP2practice'))

# task 2
# import os
# def check_path_access(path):
#     if os.path.exists(path):
#         print(f"The path '{path}' exists.")
        
#         if os.access(path, os.R_OK):
#             print(f"You have read access to '{path}'.")
#         else:
#             print(f"You don't have read access to '{path}'.")
        
#         if os.access(path, os.W_OK):
#             print(f"You have write access to '{path}'.")
#         else:
#             print(f"You don't have write access to '{path}'.")
        
#         if os.path.isdir(path):
#             if os.access(path, os.X_OK):
#                 print(f"You have execute access to the directory '{path}'.")
#             else:
#                 print(f"You don't have execute access to the directory '{path}'.")
#         else:
#             print("Executable access is not applicable for files.")
#     else:
#         print(f"The path '{path}' does not exist.")

# specified_path = "/Users/kamalkamalov/PP2practice/lab8/text.txt"
# check_path_access(specified_path)

# task 3
import os

def analyze_path(input_path):
    if os.path.exists(input_path):
        print(f"The path '{input_path}' exists.")
        
        dirname = os.path.dirname(input_path)
        filename = os.path.basename(input_path)
        
        print(f"Directory: {dirname}")
        print(f"Filename: {filename}")
    else:
        print(f"The path '{input_path}' does not exist.")

given_path = "/Users/kamalkamalov/PP2practice/lab8/text.txt"
analyze_path(given_path)



# task 4
# def how_much_lines(road_to_file):
#     try:
#         with open(road_to_file,'r') as file:
#             count_lines= sum(1 for line in file)
#             print(f"Количество строк в файле '{road_to_file}': {count_lines}")
#     except FileNotFoundError:
#         print(f"Файл '{road_to_file}' не найден.")
#     except Exception as error:
#         print(f"Произошла ошибка: {error}")
# road_to_file = "text.txt"
# how_much_lines(road_to_file)

# task 5
# def write_list_to_file(file_path, input_list):
#     try:
#         with open(file_path, 'w') as file:
#             for item in input_list:
#                 file.write(str(item) + '\n')
#         print(f"Список был записан в файл'{file_path}'.")
#     except Exception as error:
#         print(f"Произошла ошибка: {error}")
# my_list = ['item1', 'item2', 'item3', 'item4', 'item5']
# file_path = "text.txt"
# write_list_to_file(file_path, my_list)

# task 6
# import string
# def generate_files():
#     for letter in string.ascii_uppercase:
#         file_name = f"{letter}.txt"
#         with open(file_name, 'w') as file:
#             file.write(f"This is the content of {file_name}")

# if __name__ == "__main__":
#     generate_files()

# task 7
# def copy_file(source_path, destination_path):
#     try:
#         with open(source_path, 'r') as source_file:
#             content = source_file.read()
        
#         with open(destination_path, 'w') as destination_file:
#             destination_file.write(content)

#         print(f"Contents copied from '{source_path}' to '{destination_path}'.")
#     except FileNotFoundError:
#         print(f"One of the specified files was not found.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# file_1 = "text.txt"
# file_2 = "text2.txt"
# copy_file(file_1, file_2)

# task 8
# import os
# def delete_file(file_path):
#     if os.path.exists(file_path):
#         if os.access(file_path, os.W_OK):
#             try:
#                 os.remove(file_path)
#                 print(f"File '{file_path}' deleted successfully.")
#             except Exception as e:
#                 print(f"Error deleting file: {e}")
#         else:
#             print(f"You don't have permission to delete the file '{file_path}'.")
#     else:
#         print(f"The file '{file_path}' does not exist.")

# file_to_delete = "text2.txt"
# delete_file(file_to_delete)
