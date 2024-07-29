from week13.file_exercise.src.classes.file_handler import FileHandler
from week13.file_exercise.src.file_processing_error import FileProcessingError


class FileProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        file_handler = FileHandler(self.file_path, 'r')
        try:
            with file_handler.open() as file:
                return file.read()
        except FileProcessingError as e:
            return e.message

    def write_file(self, content):
        file_handler = FileHandler(self.file_path, 'w')
        try:
            with file_handler.open() as file:
                file.write(content)
                return "File written successfully."
        except FileProcessingError as e:
            return e.message
