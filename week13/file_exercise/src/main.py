from week13.file_exercise.src.classes.file_processor import FileProcessor


def file_processing_system():
    file_path = input("Enter the file path: ")
    operation = input("Enter the operation (read/write): ").strip().lower()

    processor = FileProcessor(file_path)

    if operation == "write":
        content = input("Enter the content to write to the file: ")
        result = processor.write_file(content)
    elif operation == "read":
        result = processor.read_file()
    else:
        result = "Invalid operation. Please enter 'read' or 'write'."

    print(result)


# Run the main function
if __name__ == "__main__":
    file_processing_system()
