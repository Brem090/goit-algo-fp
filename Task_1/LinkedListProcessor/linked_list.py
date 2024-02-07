from node import Node

class LinkedList:
    def __init__(self):
        self.start_node = None

    def append_value(self, value):
        if not self.start_node:
            self.start_node = Node(value)
        else:
            current_node = self.start_node
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = Node(value)

    def display_list(self):
        current_node = self.start_node
        while current_node:
            print(current_node.value, end=' ')
            current_node = current_node.next_node
        print()

    def reverse_list(self):
        previous_node = None
        current_node = self.start_node
        while current_node is not None:
            next_node = current_node.next_node
            current_node.next_node = previous_node
            previous_node = current_node
            current_node = next_node
        self.start_node = previous_node

    def merge_sort(self, node):
        if node is None or node.next_node is None:
            return node

        middle_node = self.get_middle_node(node)
        next_to_middle_node = middle_node.next_node

        middle_node.next_node = None

        left_half = self.merge_sort(node)
        right_half = self.merge_sort(next_to_middle_node)

        sorted_list = self.merge_sorted_lists(left_half, right_half)
        return sorted_list

    def get_middle_node(self, start_node):
        if start_node is None:
            return start_node

        slow_node = start_node
        fast_node = start_node

        while fast_node.next_node is not None and fast_node.next_node.next_node is not None:
            slow_node = slow_node.next_node
            fast_node = fast_node.next_node.next_node
            
        return slow_node
    
    def merge_sorted_lists(self, left_list, right_list):
        if left_list is None:
            return right_list
        if right_list is None:
            return left_list

        if left_list.value <= right_list.value:
            result = left_list
            result.next_node = self.merge_sorted_lists(left_list.next_node, right_list)
        else:
            result = right_list
            result.next_node = self.merge_sorted_lists(left_list, right_list.next_node)
        return result