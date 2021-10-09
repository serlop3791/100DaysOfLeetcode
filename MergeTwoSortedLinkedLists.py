from Utils import Utils

linked_list = Utils([2, 7, 18, 31, 33, 200]).get_linked_list()
linked_list_two = Utils([4, 6, 8, 10, 11, 24, 30]).get_linked_list()

# linked_list_small = Utils([2]).get_linked_list()
# linked_list_small_two = Utils([4]).get_linked_list()
linked_list_small = Utils([2, 6, 12, 24, 48]).get_linked_list()
linked_list_small_two = Utils([4, 8, 12, 16, 32, 64]).get_linked_list()
first_head = linked_list_small.head
second_head = linked_list_small_two.head
merged_list = Utils([]).get_linked_list()
next_node = None
while first_head is not None or second_head is not None:
    if first_head is None:
        next_node = second_head
        second_head = second_head.next
    elif second_head is None:
        next_node = first_head
        first_head = first_head.next

    if second_head is not None \
            and first_head is not None:
        if first_head.data < second_head.data:
            next_node = first_head
            first_head = first_head.next
        else:
            next_node = second_head
            second_head = second_head.next
    merged_list.append(next_node.data)

print("Printing merged list!")
merged_list.print_list()
