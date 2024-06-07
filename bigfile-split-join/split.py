import os

def split_file(filename, part_size):
    with open(filename, 'rb') as f:
        part1 = filename + '_part1'
        part2 = filename + '_part2'
        
        # Read and write part 1
        with open(part1, 'wb') as p1:
            p1.write(f.read(part_size))
        
        # Read and write part 2
        with open(part2, 'wb') as p2:
            p2.write(f.read())
    
    os.remove(filename)
    print(f"{filename} split into {part1} and {part2} and original deleted.")

def main():
    exclude_files = {os.path.basename(__file__), "join.py", "join.bat", "split.bat"}
    files = [f for f in os.listdir('.') if os.path.isfile(f) and f not in exclude_files]
    
    for filename in files:
        size = os.path.getsize(filename)
        part_size = size // 2
        print(f"Splitting {filename}...")
        split_file(filename, part_size)

if __name__ == "__main__":
    main()
