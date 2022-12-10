""" Solves Day Seven of  Advent of Code 2022 https://adventofcode.com/2022/day/7"""


def get_dir_sizes() -> list:
    """creates a list of dir sizes, -1 is root"""
    dir_stack = []
    dirs = []
    with open("day7/input.txt", encoding="UTF-8") as file:
        for line in file.readlines():
            line = line.replace("\n", "")
            parts = line.split(" ")

            if parts[0] == "$":
                if parts[1] == "cd" and parts[2] == "..":
                    size = dir_stack.pop()
                    dirs.append(size)
                    dir_stack[-1] += size
                elif parts[1] == "cd":
                    dir_stack.append(0)

            elif parts[0] != "dir":
                dir_stack[-1] += int(parts[0])

    # collect last dirs
    while len(dir_stack) > 0:
        size = dir_stack.pop()
        dirs.append(size)
        # add to parent dir
        if len(dir_stack) > 0:  # wasnt last to pop?
            dir_stack[-1] += size

    return dirs


def total_size_of_dirs_with(max_dir_size: int) -> int:
    """sums dirs with less than max_dir_size"""
    return sum(d for d in get_dir_sizes() if d < max_dir_size)


print("total_size_of_dirs_with:", total_size_of_dirs_with(100_000))


def optimal_size_to_delete(filesystem_size: int, update_size: int) -> int:
    """finds the dir size closest to needed place to instell the update"""
    dirs = get_dir_sizes()
    unused_space = filesystem_size - dirs[-1]  # -1 is root
    space_to_free = update_size - unused_space

    return sorted(d for d in dirs if d > space_to_free)[0]


print("optimal_size_to_delete:", str(
    optimal_size_to_delete(70_000_000, 30_000_000)))
