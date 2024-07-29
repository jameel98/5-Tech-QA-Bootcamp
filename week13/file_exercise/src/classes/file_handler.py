from contextlib import contextmanager

from week13.file_exercise.src.file_processing_error import FileProcessingError


class FileHandler:
    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode
        self.file = None

    @contextmanager
    def open(self):
        try:
            self.file = open(self.file_path, self.mode)
            yield self.file
        except FileNotFoundError:
            raise FileProcessingError("File not found.")
        except PermissionError:
            raise FileProcessingError("Permission denied.")
        except IOError:
            raise FileProcessingError("An error occurred during file operations.")
        except Exception as e:
            raise FileProcessingError(f"An unexpected error occurred: {e}")
        finally:
            if self.file is not None:
                self.file.close()
