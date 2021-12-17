from os import getcwd,listdir,walk
from argparse import  ArgumentParser
from os.path import basename, isfile, isdir, join as join_paths, abspath


founds = 0
found_files = 0

def search(file_path,string):
    global founds
    try:
        with open(file_path,"r") as file: lines = file.readlines()

        for index,line in enumerate(lines):
            if line.find(string) != -1:
                print(f"String Found at file > {abspath(file_path)}")
                print(f'At line No.{index+1} \n {line}')
                print("-"*len(line))
                founds += 1
    except: pass



def main(string:str, path:str=None) -> None:
    """
    @param string (str) > string to search
    @param path (str)   > working dir path (If not passed pwd is taken)
    @returns > None
    """
    global founds, found_files
    path = path if path else getcwd()

    with open("formats.txt","r") as file: formats = str(file.read()).split("\n")
    
    for root, dir, files in walk(path,topdown=True):
        for file in files:
                file_path = join_paths(root, file)
                for format in formats: 
                    if basename(file_path).endswith(format):
                        search(file_path,string)
                        found_files += 1
                        break


    print(f"\nTotal {founds} founds in {found_files} files")

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-s", "--string",required=True,
                        help="A String to search")
    parser.add_argument("-p","--path",required=False,
                        help="Working Directory Path (Optional) ")

    args = vars(parser.parse_args())

    main(args["string"],args["path"])

