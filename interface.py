import random
numbers = input('[?] Enter number of nodes: ')
numbers = int(numbers)
print('[+] Creating a graph with random edges (unweighted, undirectional, not multigrahp)...')


with open('kargerMinCut-version.txt', 'w') as infile:
    for i in range(1, numbers+1):
        line = '' + str(i)
        print('[+] Creating the ', i, '-th node...')
        number_of_nodes = random.randint(1, int(numbers))
        for j in range(1, number_of_nodes+1):
            this_node = random.randint(1, int(numbers))
            if not this_node == i:
                line += ' ' + str(this_node)
        print('[+] The ', i, '-th line is created: ', line)
        line += '\n'
        infile.write(line)