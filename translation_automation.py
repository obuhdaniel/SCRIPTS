import csv


def csv_to_dict(csv_file_path):
    
    data_dict = {}
    
    with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        for row in csv_reader:
            if len(row) == 2:
                chinese_word, english_word = row
                data_dict[chinese_word.strip()] = english_word.strip() 
            else:
                print("Invalid row format")
    return data_dict    

translated_dict = csv_to_dict('converted_xls_to_csv.csv')


def replace_previous_codebase_to_translated_codebase(previous_codebase, new_codebase_dictionary):
    
    modify = previous_codebase
    for previous_codebase_word, new_codebase_word in new_codebase_dictionary.items():
        modify = modify.replace(previous_codebase_word, new_codebase_word)
   
    return modify





def main(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        lines_of_code = file.readlines()



    translated_lines = []

    for line in lines_of_code:
        translated_line = replace_previous_codebase_to_translated_codebase(line,translated_dict)
        translated_lines.append(translated_line)

    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.writelines(translated_lines)
        print("Code Conversion Successful")



if __name__ == '__main__':
    input = 'input_code.txt'
    output = 'translated_code.txt'
    main(input, output)