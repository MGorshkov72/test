import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    jsonArray = []
    with open(INPUT_FILENAME, encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=',', quotechar='\n')
    for row in reader:
        jsonArray.append(row)
    with open(OUTPUT_FILENAME, 'w') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)



if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")