if __name__ == '__main__':
    N = int(input())  # Read an integer N from the user
    
    answer_list = []  # Initialize an empty list called 'answer_list' to store values
    
    for i in range(N):
        instruction = input()  # Read a user instruction as a string
        tokens = instruction.split(" ")  # Split the instruction into a list of tokens
        
        if tokens[0] == "insert":
            # If the instruction is 'insert', insert an element at the specified index
            answer_list.insert(int(tokens[1]), int(tokens[2]))
        elif tokens[0] == "print":
            # If the instruction is 'print', print the contents of 'answer_list'
            print(answer_list)
        elif tokens[0] == "remove":
            # If the instruction is 'remove', remove the first occurrence of the specified value
            answer_list.remove(int(tokens[1]))
        elif tokens[0] == "append":
            # If the instruction is 'append', add an element to the end of 'answer_list'
            answer_list.append(int(tokens[1]))
        elif tokens[0] == "sort":
            # If the instruction is 'sort', sort 'answer_list' in ascending order
            answer_list.sort()
        elif tokens[0] == "pop":
            # If the instruction is 'pop', remove and return the last element of 'answer_list'
            answer_list.pop()
        elif tokens[0] == "reverse":
            # If the instruction is 'reverse', reverse the order of elements in 'answer_list'
            answer_list.reverse()
