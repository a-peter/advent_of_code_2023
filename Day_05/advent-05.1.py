import sys

seeds = [] # list of numbers with seeds, part one
seeds_ranges = [] # list of seeds ranges, part two
mapping_ranges = [] # list of lists of tuples with mapping areas

SOURCE_START = 0
SOURCE_END =   1
DEST_START =   2
DEST_END =     3

def add_line_to_map(line):
    values = [int(value) for value in line.split()]
    return (values[1], values[1] + values[2] - 1, values[0], values[0] + values[2] - 1)

def add_mapping(mapping):
    mapping.sort(key=lambda x: x[0])
    if mapping[0][0] != 0:
        mapping = [(0, mapping[0][0] - 1, 0, mapping[0][0] - 1)] + mapping
    mapping.append((mapping[-1][0] + mapping[-1][2], mapping[-1][0] + 10000000000000000000, mapping[-1][0] + mapping[-1][2], mapping[-1][0] + 10000000000000000000 ))
    mapping_ranges.append(mapping)

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

def perform_task_1():
    mappings = []
    min_location = sys.maxsize
    for seed in seeds:
        if len(mappings) > 0:
            min_location = min(min_location, mappings[-1])
        mappings = [seed]
        m = seed
        for mapping in mapping_ranges:
            for mapping_range in mapping:
                if m <= mapping_range[SOURCE_END]:
                    mappings.append(mapping_range[DEST_START] + m - mapping_range[SOURCE_START])
                    m = mappings[-1]
                    break
    min_location = min(min_location, mappings[-1])
    return min_location

def find_minimum(current_min, mappings):
    x = current_min
    if len(mappings) > 0:
        x = min(current_min, min(mappings[7], key = lambda m: m[0])[0])
    return x

def perform_task_2():
    stage_ranges = {}
    min_location = sys.maxsize
    for seed_range in seeds_ranges:
        min_location = find_minimum(min_location, stage_ranges)
        stage_ranges[0] = [(seed_range[0], seed_range[0] + seed_range[1] - 1)]
        # iterate all mappings
        for index, mapping in enumerate(mapping_ranges):
            stage_ranges[index + 1] = []
            for stage_range in stage_ranges[index]:
                # iterate all lines of a mapping
                for section in mapping:
                    if stage_range[0] <= section[SOURCE_END]: # start of seed-range in section?
                        if stage_range[1] <= section[SOURCE_END]: # end of seed-range in section?
                            # fits into, add whole mapping rage
                            stage_ranges[index + 1].append((stage_range[0] - section[SOURCE_START] + section[DEST_START], stage_range[1] - section[SOURCE_START] + section[DEST_START]))
                            break
                        else:
                            # stage range does not fit into current mapping line
                            # split up ...
                            partial_mapping = (stage_range[0] - section[SOURCE_START] + section[DEST_START], section[DEST_END])
                            stage_ranges[index + 1].append(partial_mapping)
                            # and continue with partial range and next section in mapping
                            stage_range = (section[SOURCE_END] + 1, stage_range[1])
                            continue

    min_location = find_minimum(min_location, stage_ranges)
    return min_location

print('input:')
read_input('Day_05/input-advent-05.1.txt')
# read_input('Day_05/sample-05.01.txt')

print()
print('mappings')
print('minimum location  :', perform_task_1())
print('minimum location 2:', perform_task_2())

