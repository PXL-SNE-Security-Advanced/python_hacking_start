def main():
    file = open("tekst.txt", "a")
    file.write("Dit is een nieuwe regel")
    # file.write("\nDit is een nieuwe regel")

    file.close()

if __name__ == '__main__':
    main()
    
    