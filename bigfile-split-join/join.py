import os

def join_files(part1, part2, original_filename):
    with open(original_filename, 'wb') as outfile:
        with open(part1, 'rb') as p1:
            outfile.write(p1.read())
        with open(part2, 'rb') as p2:
            outfile.write(p2.read())
    
    os.remove(part1)
    os.remove(part2)
    print(f"Joined {part1} and {part2} into {original_filename} and deleted the parts.")

def main():
    exclude_files = {os.path.basename(__file__), "split.py", "join.bat", "split.bat"}
    files = [f for f in os.listdir('.') if os.path.isfile(f) and f not in exclude_files]
    
    part1_files = [f for f in files if '_part1' in f]
    
    for part1 in part1_files:
        part2 = part1.replace('_part1', '_part2')
        if part2 in files:
            original_filename = part1.replace('_part1', '')
            print(f"Joining {part1} and {part2} into {original_filename}...")
            join_files(part1, part2, original_filename)
        else:
            print(f"Error: {part2} not found for {part1}")

if __name__ == "__main__":
    main()
