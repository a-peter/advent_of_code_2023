
file_name = './Day_20/sample-20.1.txt'
file_name = './Day_20/sample-20.2.txt'
file_name = './Day_20/input-advent-20.txt'

# % -> FlipFlop, initially off 0. high -> nothing. low -> toggle on/off. off/on -> send hi. off/on -> send lo
# & -> Conjunct, 

modules = {} # name : [symbol, state, targets, sources]
sources = {}
for line in open(file_name).read().splitlines():
    module, targets = line.split(' -> ')
    if module.startswith('%'):
        modules[module[1:]] = ['%', 0, targets.split(', ')]
    elif module.startswith('&'):
        modules[module[1:]] = ['&', 0, targets.split(', '), {}]
        sources[module[1:]] = list()
    else:
        modules[module] = ['b', 0, targets.split(', ')]

new_modules = {}
for name, module in modules.items():
    [modules[source_name][3].update({name: 0}) for source_name in sources.keys() if source_name in module[2]]
    for target in module[2]:
        if not target in modules.keys():
            new_modules[target] = ['d', 0, []]
modules.update(new_modules)

# Graphviz output
# def graphviz_output():
#     print('digraph {')
#     for name, module in modules.items():
#         if module[0] == '&':
#             print(f'\t{name} [shape=box];')
#         elif module[0] == 'b':
#             print(f'\t{name} [shape=hexagon];')
#         for target in module[2]:
#             if modules[target][0] == '&':
#                 print(f'\t{name} -> {target} [color=blue];')
#             else:
#                 print(f'\t{name} -> {target};')
#     print('}')
# graphviz_output()

# Now, modules contains all module mappings.
# For conjunctions & there is a fourth field containing all inputs as map name:state
[print(m,v) for m,v in modules.items()]

def process(signal):
    new_signals = []
    source, pulse, target = signal
    type, info, *targets = modules[target]

    if type == 'b':
        new_signals = [('broadcaster', pulse, t) for t in targets[0]]
    elif type == '%':
        if pulse == 0: # LO executed. HI ignored
            new_state = 1 - info
            modules[target][1] = new_state
            new_signals = [(target, new_state, t) for t in targets[0]] # TODO: ignore 1 signals to %?
    elif type == '&':
        modules[target][3][source] = pulse
        if all(modules[target][3].values()):
            new_signals = [(target, 0, t) for t in targets[0]]  # send low to outputs
            modules[target][1] = 1
        else:
            new_signals = [(target, 1, t) for t in targets[0]] # send high to outputs
            modules[target][1] = 0
    # elif type == 'd':
    #     modules[target][1] = pulse
    return new_signals

def engine_state() -> str:
    return ' - '.join([f'{k}={v[1]}' for k,v in modules.items()])

signal_count = [0, 0]
hashes = []
print(engine_state())
button_press = 0
relevant = [name for name, module in modules.items() if module[0] == '&']
product = 1
while len(relevant) > 0:
    button_press += 1
    signals = [('button', 0, 'broadcaster')]
    while len(signals) > 0:
        # take first element from 
        signal = signals.pop(0) # signals[0]
        # print([print(x, end=' ') for x in signal])

        if signal[2] in relevant and signal[1] == 1:
            product *= button_press
            relevant.remove(signal[2])
            print(signal[2], signal[1], button_press)
        signals.extend(process(signal))
        signal_count[signal[1]] += 1

    if button_press == 1000:
        print('Low/Hi:', signal_count[0], signal_count[1])
        print('Task 1: %d' % (signal_count[0] * signal_count[1]))

print('Task 2: %d' % product)
# sample 1: 32000000 / sample 2: 11687500 / input: 703315117