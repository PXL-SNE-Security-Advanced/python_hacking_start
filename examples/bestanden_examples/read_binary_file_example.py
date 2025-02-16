import json

def main():
    # Open the binary file in read-binary mode
    with open("binary.bin", "rb") as file:
        byte_data = file.read()
    
    # Display the byte data
    print("Byte data:", byte_data)
    print("Byte data data type:", type(byte_data))
    
    # Decode the byte data to a string
    try:
        string_data = byte_data.decode('utf-8')
        print("Decoded string data:", string_data)
    except UnicodeDecodeError as e:
        print(f"Decoding failed: {e}")

if __name__ == '__main__':
    main()

