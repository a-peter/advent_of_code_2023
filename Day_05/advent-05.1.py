import sys

seeds = [] # list of numbers with seeds, part one
seeds_ranges = [] # list of seeds ranges, part two
ranges = [] # list of dictionaries

def add_line_to_map(line):
    values = [int(value) for value in line.split()]
    return (values[1], values[0], values[2], values[1] + values[2] - 1, values[0] + values[2] - 1)

def add_mapping(mapping):
    mapping.sort(key=lambda x: x[0])
    if mapping[0][0] != 0:
        mapping = [(0, 0, mapping[0][0], mapping[0][0] - 1, mapping[0][0] - 1)] + mapping
    mapping.append((mapping[-1][0] + mapping[-1][2], mapping[-1][0] + mapping[-1][2], 10000000000000000000, mapping[-1][0] + 10000000000000000000, mapping[-1][0] + 10000000000000000000 ))
    ranges.append(mapping)

def read_input(file_name):
    global seeds
    mapping_list = []
    for line in open(file_name):
        if line.startswith('seeds'):
            seeds = [int(seed) for seed in line.split()[1:]]
            for i in range(0, len(seeds), 2):
                seeds_ranges.append((seeds[i], seeds[i+1]))
        elif line[0].isdigit():
            mapping_list.append(add_line_to_map(line))
        elif line.startswith('\n'):
            pass
        elif line.startswith('seed-to-soil map:'):
            pass
        else:
            add_mapping(mapping_list)
            mapping_list = []
    add_mapping(mapping_list)

def process_mappings():
    mappings = []
    min_location = sys.maxsize
    for seed in seeds:
        if len(mappings) > 0:
            min_location = min(min_location, mappings[-1])
        mappings = [seed]
        m = seed
        for index, r in enumerate(ranges):
            for index2, section in enumerate(r):
                if m <= section[0] + section[2] - 1:
                    mappings.append(section[1] + m - section[0])
                    m = mappings[-1]
                    # print(seed, index, r)
                    break
    min_location = min(min_location, mappings[-1])
    return min_location

def find_minimum(current_min, mappings):
    x = current_min
    if len(mappings) > 0:
        x = min(current_min, min(mappings[7], key = lambda m: m[0])[0])
    return x

def process_more_seeds():
    mappings = {}
    min_location = sys.maxsize
    for seed_range in seeds_ranges:
        min_location = find_minimum(min_location, mappings)
        mappings[0] = [(seed_range[0], seed_range[0] + seed_range[1] - 1)]
        for index, r in enumerate(ranges):
            mappings[index + 1] = []
            for m in mappings[index]:
                for section in r:
                    if m[0] <= section[3]: # start of seed-range in section?
                        if m[1] <= section[3]: # end of seed-range in section?
                            # fits into, add whole mapping rage
                            mappings[index + 1].append((m[0] - section[0] + section[1], m[1] - section[0] + section[1]))
                            break
                        else:
                            # NOT OK!!!
                            partial_mapping = (m[0] - section[0] + section[1], section[4])
                            mappings[index + 1].append(partial_mapping)
                            next_mapping = (section[3] + 1, m[1])
                            m = next_mapping
                            continue

    min_location = find_minimum(min_location, mappings)
    return min_location

print('input:')
read_input('Day_05/input-advent-05.1.txt')
# read_input('Day_05/sample-05.01.txt')

print()
print('mappings')
print('minimum location:', process_mappings())
print('minimum location 2:', process_more_seeds())

