import argparse

def recover_jpegs(input_file_path):
    with open(input_file_path, 'rb') as file:
        data = file.read()
# Jpeg signatures in raw bytes FF D8 ... FF D9
    jpeg_start = b'\xFF\xD8\xFF'
    jpeg_end = b'\xFF\xD9'

    pos = 0
    file_count = 0

    while True:
        start = data.find(jpeg_start, pos)
        if start == -1:
            break

        end = data.find(jpeg_end, start)
        if end == -1:
            print("Found start without end — skipping.")
            break

        end += len(jpeg_end)

        jpeg_data = data[start:end]

        with open(f"recovered_{file_count}.jpg", 'wb') as img:
            img.write(jpeg_data)
            print(f"Recovered: recovered_{file_count}.jpg")

        file_count += 1
        pos = end

    print(f"Total JPEGs recovered: {file_count}")

# Main entry point
if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Recover JPEG images from a raw binary file.")
    parser.add_argument("input_file", help="Path to the raw binary file containing deleted JPEGs.")

    # Parse arguments
    args = parser.parse_args()

    # Call the recovery function with the provided file path
    recover_jpegs(args.input_file)
