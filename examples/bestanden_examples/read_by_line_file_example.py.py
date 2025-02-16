def main():
    file = open("tekst.txt", "r")
    for line in file:
        print(line, end="")
    file.close()

if __name__ == '__main__':
    main()
    
    
    