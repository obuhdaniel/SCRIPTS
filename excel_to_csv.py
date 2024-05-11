import pandas as pd

def convert_xls_to_csv(xls_file, csv_file):

    df = pd.read_excel(xls_file, header=None)

    df.to_csv(csv_file, index=False, header=None)




def main():
    input = 'input.xls'
    output = 'converted_to_csv.csv'
    convert_xls_to_csv(input, output)


if __name__ == "__main__":
    main()