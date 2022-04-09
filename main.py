import sys
import csv

column_name = sys.argv[3]
new_csv_body = ""
with open(sys.argv[1], mode='r') as left_csv_file:
    left_csv_reader = csv.DictReader(left_csv_file, delimiter=',')
    left_file_col_names = left_csv_reader.fieldnames
    for left_row in left_csv_reader:
        with open(sys.argv[2], mode='r') as right_csv_file:
            right_csv_reader = csv.DictReader(right_csv_file, delimiter=',')
            right_file_col_names = right_csv_reader.fieldnames
            for right_row in right_csv_reader:
                if left_row[column_name] == right_row[column_name]:
                    for column in right_file_col_names:
                        new_csv_body += f"{right_row[column]},"
                    for column in left_file_col_names:
                        if column != column_name:
                            new_csv_body += f"{left_row[column]}"
                            if column != left_file_col_names[-1]:
                                new_csv_body += ','
                            else:
                                new_csv_body += '\n'
    new_csv_header = ""
    for column in right_file_col_names:
        new_csv_header += f"{column},"
    for column in left_file_col_names:
        if column != column_name:
            new_csv_header += f"{column}"
            if column != left_file_col_names[-1]:
                new_csv_header += ','
    print(new_csv_header + '\n' + new_csv_body)
