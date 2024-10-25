class Exceptions:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.file_name, 'r')
            return self.file
        except FileNotFoundError:
            print(f"File {self.file_name} not found")
            return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        if exc_type == FileNotFoundError:
            print(f"File {self.file_name} not found")
            return True
        return False