'''this is run all the func'''
import os

def run_all_math():
    '''this func runs all the functions of math '''
    
    # all_math_folder=os.listdir()
    all_math_folder=[]

    for i in range(1, 21):
        if i<9:
            all_math_folder.append('math00'+str(i))
        elif i>9:
            all_math_folder.append('math0'+str(i))
    

    for folder in all_math_folder:
        ans_path = os.path.join(folder, 'solution.py')
        print(ans_path)
        # print(f'\n')
        # print(f'below is solution for {folder}\n')
        # os.system( 'python3 '+ ans_path)
        



if __name__ == "__main__":
    run_all_math()


