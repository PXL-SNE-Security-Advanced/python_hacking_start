import csv

def main():
    file = open("data.csv", "r", newline="")
    reader = csv.reader(file)
    for row in reader:
        print(row)
    file.close()

if __name__ == '__main__':
    main()
    