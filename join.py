import csv


def open_file(file_path):
    with open(file_path, mode='r') as left_csv_file:
        return csv.DictReader(left_csv_file, delimiter=',')

#TODO: rewrite Join to enable file to be open to prevent the i/o operation error
class Join:
    def __init__(self, first_file, second_file, column_name, join_type='inner'):
        self.first_file = open_file(first_file)
        self.second_file = open_file(second_file)
        self.column_to_join_on = column_name
        self.join_type = join_type
        self.first_file_cols = self.first_file.fieldnames
        self.second_file_cols = self.second_file.fieldnames

    def inner_join(self):
        new_csv_body = ""
        for first_file_row in self.first_file:
            for second_file_row in self.second_file:
                if first_file_row[self.column_to_join_on] == second_file_row[self.column_to_join_on]:
                    for column in self.first_file_cols:
                        new_csv_body += f"{second_file_row[column]},"
                    for column in self.second_file_cols:
                        if column != self.column_to_join_on:
                            new_csv_body += f"{first_file_row[column]}"
                            if column != self.second_file_cols[-1]:
                                new_csv_body += ','
                            else:
                                new_csv_body += '\n'
        return new_csv_body
