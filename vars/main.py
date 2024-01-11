a = 10
b = 15

c = "hello"

# print(type(a))

# print(c, a + b)

# print(f"Output: {a + b}")

a = 10.501285

# print(f"{a + b:.2f}")

playing = False 
# print(type(playing))

my_str = "hello world"

lst = [1, 245, 5, 2, 124, 2]

def find_sub_ten(lst):
    new_lst = []
    for item in lst:
        if item < 10:
            new_lst.append(item)
    return new_lst


def remove_left_letter(string):
    new_str = string[1:]
    return new_str

def return_abs(num):
    abs_val = abs(num)
    return abs_val

if __name__ == "__main__":
    print(f"New list: {find_sub_ten(lst)}")
    print(f"New string: {remove_left_letter(my_str)}")
    print(return_abs(-15))