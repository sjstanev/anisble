import csv

neighbours_list = []

def network_neigbours(network_neighbours):
    # create headers
    header = ['local_interface','neighbour', 'platform', 'port', 'dummy_device']

    # open the file in the write mode
    with open('csv_file', 'w')as f:

        # create the csv writer
        writer = csv.writer(f)
        writer.writerow(header)

        print('-' * 80)
        for int,neihbours in network_neighbours.items():
            # find how many neighbour thare are on that interface
            count_neighbours = len(neihbours)
            if count_neighbours > 1:
                print (f'The neighbour on interface {int} is a dummy device')
                print(f'\nOn interface {int} there {count_neighbours} neighbour(s).')
                dummy_device = 'yes'
            else:
                print(f'\nOn interface {int} there {count_neighbours} neighbour(s).')
                dummy_device = 'no'

            for neihbour in neihbours:

                # print result in csv format
                print (f'interface {int} : neighbour { neihbour["host"] }, platform: {neihbour["platform"]}, port {neihbour["port"]},"dummy_device": {dummy_device}')

                # create csv file
                writer.writerow([int, neihbour["host"], neihbour["platform"], neihbour["port"], dummy_device])

                # create a dictionary with whole information
                neighbours_list.append({"local_interface":int, "neighbour": neihbour["host"], "platform": neihbour["platform"], "port": neihbour["port"], "dummy_device": dummy_device })
        
        print("-" * 80)
    return neighbours_list