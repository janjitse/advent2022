import sys
from typing import Dict, Union, Optional


class Dir:
    def __init__(self, name: str, parent):
        self.children: Dict[str, Union[Dir, File]] = {}
        self.name = name
        self.parent = parent
        self._size: Optional[int] = None
        if self.parent is not None:
            self.full_name = self.parent.full_name + "/" + self.name
        else:
            self.full_name = self.name

    def size(self) -> int:
        if self._size is not None:
            return self._size
        else:
            total_size = sum([c.size() for c in self.children.values()])
            self._size = total_size
        return total_size

    def size_less(self, max_size=100_000) -> int:
        children_size = sum([c.size_less(max_size) for c in self.children.values()])
        self_size = self.size()
        if self_size <= max_size:
            children_size += self_size
        return children_size


class File:
    def __init__(self, name: str, parent: Dir, size: int):
        self.name = name
        self._size = size
        self.parent = parent
        self.full_name = self.parent.full_name + "/" + name

    def size(self) -> int:
        return self._size

    def size_less(self, max_size=100_000) -> int:
        return 0


directory_dict = {"/": Dir(name="/", parent=None)}

with open(sys.path[0] + "/input.txt", "r") as f:
    cur_dir: Dir = directory_dict["/"]
    for line in f:
        if line[:4] == "$ cd":
            _, _, new_dir = line.strip().split(" ")
            if new_dir == "/":
                cur_dir = directory_dict["/"]
            elif new_dir == "..":
                cur_dir = cur_dir.parent
            else:
                child_dir = cur_dir.children[new_dir]
                assert isinstance(child_dir, Dir)
                cur_dir = child_dir
        elif line[:4] == "$ ls":
            continue
        elif line[:3] == "dir":
            name = line[4:].strip()
            found_dir = Dir(name=name, parent=cur_dir)
            cur_dir.children[name] = found_dir
            directory_dict[cur_dir.children[name].full_name] = found_dir
        else:  # it's a file
            size, name = line.strip().split(" ")
            file = File(name=name, parent=cur_dir, size=int(size))
            cur_dir.children[name] = file

print(directory_dict["/"].size_less())

free_space = 70_000_000 - directory_dict["/"].size()
required = 30_000_000 - free_space

candidates = []
for d in directory_dict.values():
    d_size = d.size()
    if d_size >= required:
        candidates.append(d_size)

print(min(candidates))


# from collections import Counter

# character_counter = Counter()
# for d in directory_dict.values():
#     for c in d.children.values():
#         character_counter.update(c.name)
# print(character_counter)
# print(len(character_counter))
# print(set(list("abcdefghijklmnopqrstuvwxyz")) - set(character_counter.keys()))
