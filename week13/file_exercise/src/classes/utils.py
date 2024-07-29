from week13.file_exercise.src.file_processing_error import FileProcessingError


class Utils:

    @staticmethod
    def read_file(file_path):
        try:
            with open(file_path, 'r') as file:
                content = file.read()
            return content
        except FileNotFoundError:
            raise FileProcessingError("File not found.")
        except IOError:
            raise FileProcessingError("An error occurred while reading the file.")
        except Exception as e:
            raise FileProcessingError(f"An unexpected error occurred: {e}")
        finally:
            if file is not None:
                file.close()

    @staticmethod
    def write_file(file_path, content):
        file = None
        try:
            file = open(file_path, 'w')
            file.write(content)
        except PermissionError:
            raise FileProcessingError("Permission denied.")
        except IOError:
            raise FileProcessingError("An error occurred while writing to the file.")
        else:
            return "File written successfully."
        finally:
            if file is not None:
                file.close()
