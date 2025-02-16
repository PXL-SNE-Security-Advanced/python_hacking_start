import json

def main():
    data = {
        "name": "Alice",
        "age": 30,
        "city": "New York"
    }
    file = open("data.json", "w")
    json.dump(data, file)
    file.close()

if __name__ == '__main__':
    main()
    
    
    