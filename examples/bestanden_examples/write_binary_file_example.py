def main():
    # Data to be written (example: bytes representing "Hello")
    data = b'\x48\x65\x6c\x6c\x6f'  # 'Hello' in ASCII
    file = open("binary.bin", "wb")
    file.write(data)
    file.close()

if __name__ == '__main__':
    main()
    
    