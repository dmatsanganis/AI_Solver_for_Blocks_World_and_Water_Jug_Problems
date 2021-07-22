import heapq
import copy
import re


# Prints the menu
def menu():
    print("\n==============================")
    print("=============MENU=============")
    print("==============================")
    print("1. Blocks World")
    print("2. Water Jug")
    print("3. Έξοδος")
    print("==============================")


# Blocks World Problem
def blocks_world():
    print("\nΕπιλέχθηκε το πρόβλημα Blocks World")

    # Regular expression for the inputs
    regex = re.compile('[A-Z,a-z,0-9]*[,]([A-Z,a-z,0-9]*[,]*)')

    # Insert the starting state
    start_input = input("Αρχική κατάσταση: ")
    # Must match the regex
    while not regex.match(start_input):
        print("Λάθος μορφή αρχικής κατάστασης")
        start_input = input("Αρχική κατάσταση: ")
    # Create a list of lists based on the input for the starting state and print it
    list = start_input.split(',')
    start_state = []
    for letters in list:
        stack = []
        if len(letters) > 0:
            for letter in letters:
                if letter != ' ':
                    stack.append(letter)
        start_state.append(stack)
    print("Αρχική κατάσταση: " + str(start_state))

    # Insert the goal state
    goal_input = input("Τελική κατάσταση: ")
    # Must match the regex
    while not regex.match(goal_input):
        print("Λάθος μορφή τελικής κατάστασης")
        goal_input = input("Τελική κατάσταση: ")
    # Create a list of lists based on the input for the goal state and print it
    list = goal_input.split(',')
    if (len(list) < len(start_state)):
        print('Ο αριθμός των στοιβών στην τελική κατάσταση είναι μικρότερος από αυτόν στην αρχική κατάσταση')
        blocks_world()
    goal_state = []
    for letters in list:
        stack = []
        if len(letters) > 0:
            for letter in letters:
                if letter != ' ':
                    stack.append(letter)
        goal_state.append(stack)
    print("Τελική κατάσταση: " + str(goal_state))

    # Get the heuristic of the current state
    def nodeHeuristic(state):
        # Blocks in the wrong position
        wrong_position = 0
        # Blocks that the block below them is in wrong position
        below_wrong_position = 0
        # For every stack
        for i in range(len(state)):
            # If the stack is empty continue
            if len(state[i]) == 0:
                continue
            # If the goal state stack have more or the same blocks than the stack of the current state
            elif len(goal_state[i]) >= len(state[i]):
                # For every block of that stack
                for j in range(len(state[i])):
                    # If the block is not in correct position add one
                    if goal_state[i][j] != state[i][j]:
                        wrong_position += 1
                    # If the stack has more than one block
                    if j >= 1:
                        # If the block below is not in correct position add one
                        if goal_state[i][j-1] != state[i][j-1]:
                            below_wrong_position += 1
            # If the goal state stack have less blocks than the stack of the current state
            elif len(goal_state[i]) < len(state[i]):
                # Find the difference in blocks
                dif = len(state[i]) - len(goal_state[i])
                # If the goal state stack is empty add the difference to the wrong position
                if len(goal_state[i]) == 0:
                    wrong_position += dif
                # Else
                else:
                    # For every block of the goal state stack
                    for j in range(len(goal_state[i])):
                        # If the block is not in correct position add one
                        if goal_state[i][j] != state[i][j]:
                            wrong_position += 1
                        # If the stack has more than one block
                        if j >= 1:
                            # If the block below is not in correct position add one
                            if goal_state[i][j-1] != state[i][j-1]:
                                below_wrong_position += 1
                    # Add the difference
                    wrong_position += dif
        return wrong_position + below_wrong_position

    # BlocksNode Class
    class BlocksNode:
        # Initialization
        def __init__(self, state, parent=None):
            self.state = state
            self.parent = parent
            self.cost = 0
            self.heuristic = 0
            if parent:
                self.cost = parent.cost + 1

        # Create a list with BlocksNode class objects for each one of the children
        def getChildren(self, heuristicFunction=None):
            # List for the children
            children = []
            # Find all the possible moves that we can perform from the current state
            for i, stack in enumerate(self.state):
                for j, stack1 in enumerate(self.state):
                    if i != j and len(stack1):
                        temp = copy.deepcopy(stack)
                        child = copy.deepcopy(self)
                        temp1 = copy.deepcopy(stack1)
                        temp.append(temp1[-1])
                        del temp1[-1]
                        child.state[i] = temp
                        child.state[j] = temp1
                        child.parent = copy.deepcopy(self)
                        child.heuristic = heuristicFunction(child.state)
                        children.append(child)
            return children

        # Return the cost of the current path
        def getCost(self):
            return self.cost + self.heuristic

        # Check if goal is achieved and print the path and the number of moves required
        def checkGoal(self):
            if self.state == goal_state:
                state, path = self, []
                while state:
                    path.append(state.state)
                    state = state.parent
                print('\n==============================')
                print("Βρέθηκε λύση")
                print('==============================')
                print('Κινήσεις που χρειάστηκαν: ' + str(len(path)-1))
                print('==============================')
                for i in reversed(path):
                    print(i)
                print('==============================')
                return True
            else:
                return False

    aStar(BlocksNode(start_state), nodeHeuristic)


# Water Jug Problem
def water_jug():
    print("\nΕπιλέχθηκε το πρόβλημα Water Jug")

    # Insert the capacity of jug 1
    jug1 = input("Ποσότητα στην κανάτα 1: ")
    # Must be digit
    while not jug1.isdigit():
        print("Εισάγετε μόνο θετικούς ακέραιους αριθμούς")
        jug1 = input("Ποσότητα στην κανάτα 1: ")
    # Must be positive
    while int(jug1) <= 0:
        print("Εισάγετε μόνο θετικούς ακέραιους αριθμούς")
        jug1 = input("Ποσότητα στην κανάτα 1: ")

    # Insert the capacity of jug 2
    jug2 = input("Ποσότητα στην κανάτα 2: ")
    # Must be digit
    while not jug2.isdigit():
        print("Εισάγετε μόνο θετικούς ακέραιους αριθμούς")
        jug2 = input("Ποσότητα στην κανάτα 2: ")
    # Must be positive
    while int(jug2) <= 0:
        print("Εισάγετε μόνο θετικούς ακέραιους αριθμούς")
        jug2 = input("Ποσότητα στην κανάτα 2: ")

    # Create a tuple with the capacities of the two jugs
    capacities = (int(jug1), int(jug2))

    # Insert the amount of water in the goal state
    goal_jug1 = input("Τελική ποσότητα στην κανάτα 1: ")
    # Must be digit
    while not goal_jug1.isdigit():
        print("Εισάγετε μόνο θετικούς ακέραιους αριθμούς")
        goal_jug1 = input("Τελική ποσότητα στην κανάτα 1: ")
    # Must be positive and less or equal with the capacity of the jug
    while int(goal_jug1) <= 0 and int(goal_jug1) >= int(jug1):
        print("Εισάγετε μόνο θετικούς ακέραιους αριθμούς")
        goal_jug1 = input("Τελική ποσότητα στην κανάτα 1: ")

    # Insert the amount of water in the goal state
    goal_jug2 = input("Τελική ποσότητα στην κανάτα 2: ")
    # Must be digit
    while not goal_jug2.isdigit():
        print("Εισάγετε μόνο θετικούς ακέραιους αριθμούς")
        goal_jug2 = input("Τελική ποσότητα στην κανάτα 2: ")
    # Must be positive and less or equal with the capacity of the jug
    while int(goal_jug2) <= 0 and int(goal_jug2) > int(jug2):
        print("Εισάγετε μόνο θετικούς ακέραιους αριθμούς")
        goal_jug2 = input("Τελική ποσότητα στην κανάτα 2: ")

    # Create a tuple with the amount of water in the jugs for the goal state
    goal = (int(goal_jug1), int(goal_jug2))

    # Gets the possible legal moves and return a list with the childrens
    def getWaterChildren(jug1, jug2):
        # jug1 and jug2 are the current amount of water in each jug
        # List for the children
        children = []
        # Capacities of the jugs
        (cap1, cap2) = capacities
        # Check for every possible legal move
        if(jug1 < cap1):
            children.append(((cap1, jug2), 'Γέμισε την κανάτα 1', 1))
        if(jug2 < cap2):
            children.append(((jug1, cap2), 'Γέμισε την κανάτα 2', 1))
        if jug1 > 0:
            children.append(((0, jug2), 'Άδειασε την κανάτα 1', 1))
        if jug2 > 0:
            children.append(((jug1, 0), 'Άδειασε την κανάτα 2', 1))
        if jug1+jug2 <= cap1:
            sum = jug1+jug2
            children.append(
                ((sum, 0), 'Άδειασε όλη την κανάτα 2 στην κανάτα 1', 1))
        if jug1+jug2 <= cap2:
            sum = jug1+jug2
            children.append(
                ((0, sum), 'Άδειασε όλη την κανάτα 1 στην κανάτα 2', 1))
        if jug1+jug2 > cap1:
            sum = jug1+jug2-cap1
            children.append(
                ((cap1, sum), 'Γέμισε την κανάτα 1 από τη κανάτα 2', 1))
        if jug1+jug2 > cap2:
            sum = jug1+jug2-cap2
            children.append(
                ((sum, cap2), 'Γέμισε την κανάτα 2 από τη κανάτα 1', 1))
        return children

    # Get the heuristic of the current state
    def waterHeurestic(state):
        return abs((state[0] - goal[0]) + (state[1]-goal[1]))

    # WaterNode Class
    class WaterNode:
        # Initialization
        def __init__(self, state, path, cost=0, heuristic=0):
            self.state = state
            self.path = path
            self.cost = cost
            self.heuristic = heuristic

        # Create a list with WaterNode class objects for each one of the children
        def getChildren(self, heuristicFunction=None):
            # List of WaterNode objects for the children
            children = []
            for successor in getWaterChildren(self.state[0], self.state[1]):
                # Initialization of a WaterNode object for every child
                state = successor[0]
                path = list(self.path)
                path.append(successor[1])
                cost = self.cost + successor[2]
                if heuristicFunction:
                    heuristic = heuristicFunction(state)
                else:
                    heuristic = 0
                node = WaterNode(state, path, cost, heuristic)
                children.append(node)
            return children

        # Return the cost of the current path
        def getCost(self):
            return self.cost + self.heuristic

        # Check if goal is achieved and print the path and the number of moves required
        def checkGoal(self):
            if self.state[0] == goal[0] and self.state[1] == goal[1]:
                print("\n==============================")
                print("Βρέθηκε λύση")
                print("==============================")
                print("Κινήσεις που χρειάστηκαν: " + str(len(self.path)))
                print("==============================")
                print(self.path)
                print("==============================")
                return True
            else:
                return False

    aStar(WaterNode((0, 0), [], 0, 0), waterHeurestic)


# A Star Search
def aStar(node, heuristic):
    # Class for Priority Heap
    class PriorityHeap:
        # Initialization
        def __init__(self):
            self.heap = []
            self.count = 0

        # Push an item to the list based on it's priority value
        def push(self, item, priority):
            entry = (priority, self.count, item)
            heapq.heappush(self.heap, entry)
            self.count += 1

        # Pop the item with the smallest priority value
        def pop(self):
            (_, _, item) = heapq.heappop(self.heap)
            return item

        # Check if the heap is empty
        def isEmpty(self):
            return len(self.heap) == 0

    "Search the node that has the lowest combined cost and heuristic first."
    # List for the visited states
    visited = []
    # Create a priority heap
    P = PriorityHeap()
    # Push the starting state to the priority heap and as priority value it's cost
    P.push(node, node.getCost())

    while True:
        # If the priority heap is empty, no solution can be found
        if P.isEmpty():
            print('\n==============================')
            print(
                'Δεν μπόρεσε να επιτευχθεί λύση με βάση την τελική και αρχική κατάσταση που ορίσατε')
            print('==============================')

        # Pop the first state of the heap
        node = P.pop()

        # Check if this state is a goal state
        if node.checkGoal():
            return

        # If the state is not inside the visited list
        if node.state not in visited:
            # Append the state to the visited list
            visited.append(node.state)
            # Find the children of this state
            for childNode in node.getChildren(heuristic):
                # Push each child to the priority heap and as priority value set it's path total cost
                P.push(childNode, childNode.getCost())
