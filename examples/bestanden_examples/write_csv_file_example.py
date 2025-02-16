import csv

def main():
    data = [
        ["Name", "Age", "City"],
        ["Alice", 30, "New York"],
        ["Bob", 25, "Los Angeles"],
        ["Charlie", 35, "San Francisco"]
    ]
    file = open("data.csv", "w", newline="")
    writer = csv.writer(file)
    writer.writerows(data)
    file.close()

if __name__ == '__main__':
    main()
    
    