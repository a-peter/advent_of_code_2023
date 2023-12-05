
seeds = [] # list of numbers with seeds
seeds_ranges = []
ranges = [] # list of dictionaries

def add_line_to_map(line):
    values = [int(value) for value in line.split()]
    # print(values)
    return (values[1], values[0], values[2], values[1] + values[2] - 1, values[0] + values[2] - 1)

def add_mapping(mapping):
    if mapping[0][0] != 0:
        mapping = [(0, 0, mapping[0][0], mapping[0][0] - 1, mapping[0][0] - 1)] + mapping
    mapping.append((mapping[-1][0] + mapping[-1][2], mapping[-1][0] + mapping[-1][2], 10000000000000000000, mapping[-1][0] + 10000000000000000000, mapping[-1][0] + 10000000000000000000 ))
    ranges.append(mapping)

def read_input():
    global seeds
    state = -1
    mapping_list = []
    for line in open('Day_05/input-advent-05.1.txt'):
    # for line in open('Day_05/sample-05.01.txt'):
        if line.startswith('seeds'):
            seeds = [int(seed) for seed in line.split()[1:]]
            for i in range(0, len(seeds), 2):
                seeds_ranges.append((seeds[i], seeds[i+1]))

            # print('seeds:', seeds)
        elif line.startswith('seed-to-soil map:'):
            state += 1
            pass
        elif line.startswith('soil'):
            add_mapping(mapping_list)
            mapping_list = []
            state += 1
            pass
        elif line.startswith('fertilizer'):
            add_mapping(mapping_list)
            mapping_list = []
            state += 1
            pass
        elif line.startswith('water'):
            add_mapping(mapping_list)
            mapping_list = []
            state += 1
            pass
        elif line.startswith('light'):
            add_mapping(mapping_list)
            mapping_list = []
            state += 1
            pass
        elif line.startswith('temp'):
            add_mapping(mapping_list)
            mapping_list = []
            state += 1
            pass
        elif line.startswith('humid'):
            add_mapping(mapping_list)
            mapping_list = []
            state += 1
            pass
        elif line.startswith('\n'):
            # assing map to maps
            pass
        else:
            mapping_list.append(add_line_to_map(line))
            mapping_list.sort(key=lambda x: x[0])
    add_mapping(mapping_list)

def process_mappings():
    mappings = []
    min_location = 1000000000000000
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

def process_more_seeds():
    mappings = {}
    next_ranges = []
    min_location = 100000000000000000
    for s, seed_range in enumerate(seeds_ranges):
        if len(mappings) > 0:
            for m in mappings[7]:
                min_location = min(min_location, m[0])
        mappings[0] = [(seed_range[0], seed_range[0] + seed_range[1] - 1)]
        print('processing seed', s, ':', mappings[0])

        for index, r in enumerate(ranges):
            mappings[index + 1] = []
            for m in mappings[index]:
                for index2, section in enumerate(r):
                    if m[0] <= section[3]: # start of seed-range in section?
                        if m[1] <= section[3]: # end of seed-range in section?
                            # fits into, add whole mapping rage
                            mappings[index + 1].append((m[0] - section[0] + section[1], m[1] - section[0] + section[1]))
                            break
                        else:
                            # NOT OK!!!
                            # fitting = m[4]
                            partial_mapping = (m[0] - section[0] + section[1], section[4])
                            mappings[index + 1].append(partial_mapping)
                            next_mapping = (section[3] + 1, m[1])
                            m = next_mapping
                            continue

    for m in mappings[7]:
        min_location = min(min_location, m[0])
    return min_location


print('input:')
read_input()
print()
# print('ranges')
# [print(r) for r in ranges]
print()
print('mappings')
print('minimum location:', process_mappings())
print('minimum location 2:', process_more_seeds())

