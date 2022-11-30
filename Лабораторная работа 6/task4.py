import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename: str, delimiter=",", newline="\n") -> list[dict]:
    with open(filename, "r", encoding="utf-8") as f:
        data_ = [item.strip(newline).split(delimiter) for item in f]
        return [{data_[0][i]:item[i] for i in range(len(data_[0]))} for item in data_[1:]]
    ...  # TODO реализовать конвертер из csv в json



print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
