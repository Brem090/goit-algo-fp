from linked_list import LinkedList

def merge_two_sorted_lists(left_list, right_list):
    if left_list is None:
        return right_list
    if right_list is None:
        return left_list

    if left_list.value <= right_list.value:
        result = left_list
        result.next_node = merge_two_sorted_lists(left_list.next_node, right_list)
    else:
        result = right_list
        result.next_node = merge_two_sorted_lists(left_list, right_list.next_node)
    return result

def main():
    first_list = LinkedList()
    first_list.append_value(10)
    first_list.append_value(5)
    first_list.append_value(15)
    first_list.append_value(20)
    first_list.append_value(3)

    print("Оригінальний Список 1:")
    first_list.display_list()

    first_list.start_node = first_list.merge_sort(first_list.start_node)
    print("Відсортований Список 1:")
    first_list.display_list()

    second_list = LinkedList()
    second_list.append_value(2)
    second_list.append_value(3)
    second_list.append_value(7)
    second_list.append_value(18)

    print("Оригінальний Список 2:")
    second_list.display_list()

    second_list.start_node = second_list.merge_sort(second_list.start_node)
    print("Відсортований Список 2:")
    second_list.display_list()

    first_list.reverse_list()
    print("Реверсований Список 1:")
    first_list.display_list()

    merged_list = LinkedList()
    merged_list.start_node = merge_two_sorted_lists(first_list.start_node, second_list.start_node)
    print("Об'єднаний Відсортований Список:")
    merged_list.display_list()

if __name__ == "__main__":
    main()