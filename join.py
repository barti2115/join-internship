import csv


def generate_header(first_csv: str, second_csv: str, column_name: str):
    with open(first_csv, 'r') as first_file:
        with open(second_csv, 'r') as second_file:
            first_file_cols = list(csv.DictReader(first_file).fieldnames)
            second_file_cols = list(csv.DictReader(second_file).fieldnames)
            second_file_cols.pop(
                second_file_cols.index(column_name))  # removing duplicate of column we join on from second csv file
            header = ','.join(first_file_cols + second_file_cols) + '\n'
            return header


def inner_join(first_csv: str, second_csv: str, column_name: str):
    with open(first_csv, 'r') as first_file:
        new_csv_body = ""
        first_iterator = csv.DictReader(first_file)
        for first_file_row in first_iterator:
            with open(second_csv, 'r') as second_file:
                second_iterator = csv.DictReader(second_file)
                for second_file_row in second_iterator:
                    if first_file_row[column_name] == second_file_row[column_name]:
                        new_csv_body += ','.join(first_file_row.values()) + ','
                        second_file_row.pop(column_name)
                        new_csv_body += ','.join(second_file_row.values()) + '\n'
    return new_csv_body


def fill_missing(first_file_row, second_file_row, join_type):
    if join_type == 'left':
        return ','.join(first_file_row.values()) + ',' * (len(second_file_row)) + '\n'
    #TODO solve the problem of value we join on from right table when right join and no row matches
    elif join_type == 'right':
        return ',' * (len(first_file_row)) + ','.join(second_file_row.values()) + '\n'


def left_right_join(first_csv: str, second_csv: str, column_name: str, join_type: str):
    with open(first_csv, 'r') as first_file:
        new_csv_body = ""
        first_iterator = csv.DictReader(first_file)
        for first_file_row in first_iterator:
            new_csv_chunk = ""
            with open(second_csv, 'r') as second_file:
                second_iterator = csv.DictReader(second_file)
                for second_file_row in second_iterator:
                    if first_file_row[column_name] == second_file_row[column_name]:
                        new_csv_chunk += ','.join(first_file_row.values()) + ','
                        second_file_row.pop(column_name)
                        new_csv_chunk += ','.join(second_file_row.values()) + '\n'
                if new_csv_chunk == "":
                    new_csv_chunk += fill_missing(first_file_row, second_file_row, join_type)
            new_csv_body += new_csv_chunk
    return new_csv_body
