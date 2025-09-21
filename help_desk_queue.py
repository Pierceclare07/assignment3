
from node import Node

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:
            # empty queue
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None
        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return value

    def peek(self):
        return None if self.front is None else self.front.value

    def print_queue(self):
        if self.front is None:
            print("[empty]")
            return
        curr = self.front
        print("Front")
        while curr:
            print(f"  {curr.value}")
            curr = curr.next
        print("Rear")


def run_help_desk():
    # Create an instance of the Queue class
    queue = Queue()

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ").strip()
            if name:
                # Add the customer to the queue
                queue.enqueue(name)
                print(f"{name} added to the queue.")
            else:
                print("No name entered.")
        elif choice == "2":
            # Help the next customer in the queue and return message that they were helped
            name = queue.dequeue()
            if name is None:
                print("No customers waiting.")
            else:
                print(f"Helping next customer: {name}")

        elif choice == "3":
            # Peek at the next customer in the queue and return their name
            name = queue.peek()
            if name is None:
                print("No customers waiting.")
            else:
                print(f"Next customer: {name}")

        elif choice == "4":
            # Print all customers in the queue
            print("\nWaiting customers:")
            queue.print_queue()

        elif choice == "5":
            print("Exiting Help Desk System.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_help_desk()


