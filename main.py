if command == ".dbinfo":
    with open(database_file_path, "rb") as database_file:
        
        print("Logs from your program will appear here!")
        page_size = int.from_bytes(database_file.read(2), byteorder="big")
        print(f"database page size: {page_size}")
else:
    print(f"Invalid command: {command}")