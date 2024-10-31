#Lab 6 

# Defines the Node class.
class Node:
    def __init__(self, data):
        self.data = data  # Stores the data for the node.
        self.next = None  # Initializes the next pointer to None.

# Function for the list and print each node's data.
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")  # Indicates the end of the list.

# Function for the list, print each node's data, and count the nodes
def print_linked_list_with_count(head):
    current = head
    count = 0
    while current:
        print(current.data, end=" -> ")
        current = current.next
        count += 1
    print("None")  # Indicates the end of the list.
    print("Total nodes:", count)  # Prints the total node count.

# Main function to execute the program.
def main():
    # Creates individual nodes with data values.
    node1 = Node(10)  # First node with data 10
    node2 = Node(20)  # Second node with data 20
    node3 = Node(30)  # Third node with data 30

    # Link the nodes together to form a simple linked list.
    node1.next = node2  # Links node1 to node2
    node2.next = node3  # Links node2 to node3

    # Prints the original linked list.
    print("Original linked list:")
    print_linked_list(node1)

    # Exercise 1: Updates node2's data and print the list again.
    node2.data = 25  # Changes the data in the second node.
    print("\nLinked list after updating node2's data:")
    print_linked_list(node1)

    # Exercise 2: Adds a new node (node4) with a new value and link it to the list.
    node4 = Node(40)  # Creates a new fourth node with data 40
    node3.next = node4  # Links node3 to the new node4.
    print("\nLinked list after adding node4:")
    print_linked_list(node1)

    # Exercise 3: Prints the list with node count.
    print("\nLinked list with node count:")
    print_linked_list_with_count(node1)

# Call the main function.
main()

