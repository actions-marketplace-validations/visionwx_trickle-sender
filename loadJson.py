import argparse
import json

def parseArgs():
    # 获取脚本参数
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--jsonFile", required=True, 
        type=str, default=None, help="local json file")
    args = vars(ap.parse_args())
    return args

def main():
    # 获取脚本参数
    args = parseArgs()

    r = json.load(open(args['jsonFile'],'r'))

    print(json.dumps(r))


if __name__ == "__main__":
    main()