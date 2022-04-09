import csv


class join:
    def __init__(self, first_file, second_file, column_name, join_type):
        with open(first_file, mode='r') as left_csv_file:
        self.first_file = csv.DictReader(left_csv_file, delimiter=',')
        with open(second_file, mode='r') as right_csv_file:
        self.second_file = csv.DictReader(right_csv_file, delimiter=',')
        self.column_to_join_on = column_name
        self.join_type = join_type
        self.first_file_cols = self.first_file.fieldnames
        self.second_file_cols = self.second_file.fieldnames

    def open_file(self, file_path):
        with open(file_path, mode='r') as left_csv_file:
            return csv.DictReader(left_csv_file, delimiter=',')
