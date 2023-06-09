#!/usr/bin/python3
def element_at(my_list, idx):
    if idx<0 or idx>(len(my_list)-1):
              return None
    return f"Element at index {idx} is {my_list[idx]}"
