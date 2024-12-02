def sort_input(input: str):
    left_list = []
    right_list = []

    for line in input.strip().split('\n'):
        a,b = line.split()
        left_list.append(int(a))
        right_list.append(int(b))

    left_list.sort()
    right_list.sort()
    return [left_list,right_list]

def calculate_total_distance(left_list, right_list):
    return sum(abs(a - b) for a,b in zip(left_list,right_list))

def similarity_score(left_list, right_list):
    return sum(right_list.count(a) * a for a, b in zip(left_list, right_list))

if __name__ == '__main__':
    f = open("input.txt", "r")
    data = sort_input(f.read())
    total_distance = calculate_total_distance(*data)
    similarity_score = similarity_score(*data)
    print("Day 1 solution:")
    print(f"The total distance is {total_distance} and the similarity score is {similarity_score}")
    print("===============")