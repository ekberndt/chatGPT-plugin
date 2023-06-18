import os
import numpy as np

def read_data():
    src_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(src_dir, '../data/data.txt')
    with open(data_path) as file:
        lines = [lines.rstrip() for line in file]
    return lines

def truncate_prompt(prompt_list):
    uncompleted_prompts = []
    for prompt in prompt_list:
        random_index = np.random.randint(0, len(prompt))
        truncated_prompt = prompt[0:random_index]
        uncompleted_prompts.append(truncated_prompt)
    return uncompleted_prompts    

def main():
    completed_prompts = read_data()
    uncompleted_prompts = truncate_prompt(completed_prompts)    

if __name__ == "__main__":
    main()