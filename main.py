import os
import shutil
import argparse
import time

# for safety measures
time.sleep(10)

def delete_contents(folder_path):
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):
            os.remove(item_path)
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)


def main():
    parser = argparse.ArgumentParser(description="Delete files and folders in a specified directory.")
    parser.add_argument("path", help="The path to the directory to clean.")

    args = parser.parse_args()

    if os.path.exists(args.path):
        delete_contents(args.path)
        print(f"Files and folders in {args.path} have been deleted.")
    else:
        print(f"Path {args.path} does not exist.")


if __name__ == "__main__":
    main()
