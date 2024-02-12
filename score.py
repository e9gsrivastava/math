"""this is run all the func"""
import os


def run_all_math():
    """this func runs all the functions of math"""

    all_folder = os.listdir()
    all_math_folder = [folder for folder in all_folder if "math" in folder]
    all_math_folder = sorted(all_math_folder)

    for folder in all_math_folder:
        ans_path = os.path.join(folder, "solution.py")
        print(f"\n")
        print(f"below is solution for {folder}\n")
        os.system("python3 " + ans_path)


if __name__ == "__main__":
    run_all_math()
