import argparse
import json

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dict_file", required=True, help="file dict.txt want convert" )
    parser.add_argument("--json_file", default="vocab.json", help="name file json want save")
    args = parser.parse_args()

    dict_j = {}
    with open(args.dict_file, 'r') as f:
        lines = f.readlines()
        num_line = len(lines)
        for line in lines:
            word, index = line.split(' ')
            dict_j[word] = index
    out_file = open(args.json_file, "w", encoding='utf-8')
    json.dump(dict_j, out_file, ensure_ascii=False)
    out_file.close()


if __name__ == "__main__":
    main()

