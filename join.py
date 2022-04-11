import csv
import sys


def generate_header(first_csv: str, second_csv: str, column_name: str):
    with open(first_csv, 'r') as first_file:
        with open(second_csv, 'r') as second_file:
            first_file_cols = list(csv.DictReader(first_file).fieldnames)
            second_file_cols = list(csv.DictReader(second_file).fieldnames)
            second_file_cols.pop(
                second_file_cols.index(column_name))  # removing duplicate of column we join on from second csv file
            header = ','.join(first_file_cols + second_file_cols)
    print(header)


def inner_join(first_csv: str, second_csv: str, column_name: str):
    with open(first_csv, 'r') as first_file:
        first_iterator = csv.DictReader(first_file)
        for first_file_row in first_iterator:
            with open(second_csv, 'r') as second_file:
                second_iterator = csv.DictReader(second_file)
                for second_file_row in second_iterator:
                    new_csv_chunk = ""
                    if first_file_row[column_name] == second_file_row[column_name]:
                        new_csv_chunk += ','.join(first_file_row.values()) + ','
                        second_file_row.pop(column_name)
                        new_csv_chunk += ','.join(second_file_row.values())
                        print(new_csv_chunk)


def fill_missing(left_file_row, right_file_row, join_type, column_name):
    if join_type == 'left':
        print(','.join(left_file_row.values()) + ',' * (len(right_file_row) - 1))
    elif join_type == 'right':
        temp = ""
        for key in left_file_row:
            if key == column_name:
                temp += right_file_row.pop(column_name)
            temp += ','
        print(temp + ','.join(right_file_row.values()))


def left_join(left_csv: str, right_csv: str, column_name: str):
    with open(left_csv, 'r') as left_file:
        left_iterator = csv.DictReader(left_file)
        for left_file_row in left_iterator:
            matched = False
            with open(right_csv, 'r') as right_file:
                right_iterator = csv.DictReader(right_file)
                for right_file_row in right_iterator:
                    new_csv_chunk = ""
                    if left_file_row[column_name] == right_file_row[column_name]:
                        new_csv_chunk += ','.join(left_file_row.values()) + ','
                        right_file_row.pop(column_name)
                        new_csv_chunk += ','.join(right_file_row.values())
                        print(new_csv_chunk)
                        matched = True
                if not matched:
                    fill_missing(left_file_row, right_file_row, 'left', column_name)


def right_join(left_csv: str, right_csv: str, column_name: str):
    with open(right_csv, 'r') as right_file:
        right_iterator = csv.DictReader(right_file)
        for right_file_row in right_iterator:
            count = 0
            with open(left_csv, 'r') as left_file:
                left_iterator = csv.DictReader(left_file)
                for left_file_row in left_iterator:
                    new_csv_chunk = ""
                    if right_file_row[column_name] == left_file_row[column_name]:
                        new_csv_chunk += ','.join(left_file_row.values()) + ','
                        left_file_row.pop(column_name)
                        new_csv_chunk += ','.join(left_file_row.values())
                        print(new_csv_chunk)
                        count = 1
                if count == 0:
                    fill_missing(left_file_row, right_file_row, 'right', column_name)


def column_exist(file_header, column_name):
    if column_name not in file_header:
        return False
    return True


def valid_csv(file_name, column_name):
    try:
        with open(file_name, 'r') as first_file:
            file_iterator = csv.DictReader(first_file)
            if not column_exist(file_iterator.fieldnames, column_name):
                print(f'ERROR! Column given to join on does not exist in {file_name}', file=sys.stderr)
                return False
            col_number = len(file_iterator.fieldnames)
            for row in file_iterator:
                if col_number - 1 != str(row.values()).count(','):
                    print(f'ERROR! {file_name} is not a valid csv.', file=sys.stderr)
                    return False
    except FileNotFoundError:
        print('ERROR! Wrong filepath was given.', file=sys.stderr)
        return False
    return True


def files_fine(first_file, second_file, column_name):
    if not valid_csv(first_file, column_name) or not valid_csv(second_file, column_name):
        return False
    return True


def validate_arguments(argv):
    if len(argv) < 4:
        print('ERROR! Not enough parameters.', file=sys.stderr)
        return False
    elif not files_fine(argv[1], argv[2], argv[3]):
        return False
    return True


def join(argv):
    if validate_arguments(argv):
        first_csv = argv[1]
        second_csv = argv[2]
        column_name = argv[3]
        if len(argv) == 4:
            join_type = 'inner'
        else:
            join_type = argv[4]
        generate_header(first_csv, second_csv, column_name)
        if join_type == 'inner':
            inner_join(first_csv, second_csv, column_name)
        elif join_type == 'left':
            left_join(first_csv, second_csv, column_name)
        elif join_type == 'right':
            right_join(first_csv, second_csv, column_name)
        else:
            print('ERROR! Wrong join type was given. Possible types are inner/left/right.', file=sys.stderr)
