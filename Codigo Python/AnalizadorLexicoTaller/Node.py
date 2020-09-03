class Node:
    def __init__(self, type_, description, content, row, column):
        self.type_ = type_
        self.content = content
        self.description = description
        self.row = row
        self.column = column
        self.next = None
        self.previous = None

    # Get Method

    def get_type(self):
        return self.type_

    def get_description(self):
        return self.description

    def get_content(self):
        return self.content

    def get_row(self):
        return self.row

    def get_column(self):
        return self.column

    def get_next(self):
        return self.next

    def get_previous(self):
        return self.previous

    # Set Method

    def set_type(self, type_):
        self.type_ = type_

    def set_description(self, description):
        self.description = description

    def set_content(self, content_):
        self.content = content_

    def set_row(self, row_):
        self.row = row_

    def set_column(self, column_):
        self.column = column_

    def set_next(self, next_):
        self.next = next_

    def set_previous(self, previous_):
        self.previous = previous_
