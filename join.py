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
    return generate_header(first_csv, second_csv, column_name) + new_csv_body


def fill_missing(left_file_row, right_file_row, join_type, column_name):
    if join_type == 'left':
        return ','.join(left_file_row.values()) + ',' * (len(right_file_row)) + '\n'
    elif join_type == 'right':
        temp = ""
        for key in left_file_row:
            if key == column_name:
                temp += right_file_row.pop(column_name)
            temp += ','
        return temp + ','.join(right_file_row.values()) + '\n'


def left_join(left_csv: str, right_csv: str, column_name: str):
    with open(left_csv, 'r') as left_file:
        new_csv_body = ""
        left_iterator = csv.DictReader(left_file)
        for left_file_row in left_iterator:
            new_csv_chunk = ""
            with open(right_csv, 'r') as right_file:
                right_iterator = csv.DictReader(right_file)
                for right_file_row in right_iterator:
                    if left_file_row[column_name] == right_file_row[column_name]:
                        new_csv_chunk += ','.join(left_file_row.values()) + ','
                        right_file_row.pop(column_name)
                        new_csv_chunk += ','.join(right_file_row.values()) + '\n'
                if new_csv_chunk == "":
                    new_csv_chunk += fill_missing(left_file_row, right_file_row, 'left', column_name)
            new_csv_body += new_csv_chunk
    return generate_header(left_csv, right_csv, column_name) + new_csv_body


def right_join(left_csv: str, right_csv: str, column_name: str):
    with open(right_csv, 'r') as right_file:
        new_csv_body = ""
        right_iterator = csv.DictReader(right_file)
        for right_file_row in right_iterator:
            new_csv_chunk = ""
            with open(left_csv, 'r') as left_file:
                left_iterator = csv.DictReader(left_file)
                for left_file_row in left_iterator:
                    if right_file_row[column_name] == left_file_row[column_name]:
                        new_csv_chunk += ','.join(left_file_row.values()) + ','
                        left_file_row.pop(column_name)
                        new_csv_chunk += ','.join(left_file_row.values()) + '\n'
                if new_csv_chunk == "":
                    new_csv_chunk += fill_missing(left_file_row, right_file_row, 'right', column_name)
            new_csv_body += new_csv_chunk
    return generate_header(left_csv, right_csv, column_name) + new_csv_body


def join(first_csv: str, second_csv: str, column_name: str, join_type='inner'):
    if join_type == 'inner':
        return inner_join(first_csv, second_csv, column_name)
    elif join_type == 'left':
        return left_join(first_csv, second_csv, column_name)
    elif join_type == 'right':
        return right_join(first_csv, second_csv, column_name)
