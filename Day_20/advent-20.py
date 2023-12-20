
file_name = './Day_20/sample-20.1.txt'
file_name = './Day_20/sample-20.2.txt'

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

for name, module in modules.items():
    x = [modules[source_name][3].update({name: 0}) for source_name in sources.keys() if source_name in module[2]]

# Now, modules contains all module mappings.
# For conjunctions & there is a fourth field containing all inputs as map name:state
[print(m,v) for m,v in modules.items()]

def process(signal):
    source, value, target = signal
    new_signals = []
    type, info, *targets = modules[target]
    if type == 'b':
        new_signals = [('broadcaster', value, t) for t in targets[0]]
    elif type == '%':
        if value == 0: # HI
            new_state = 1 - info
            modules[target][1] = new_state
            new_signals = [(target, modules[target][1],t) for t in targets[0]] # TODO: ignore 1 signals to %?
    elif type == '&':
        for key in targets[1].keys():
            targets[1][key] = modules[key][1]
        if all(targets[1].values()):
            # send low to outputs
            new_signals = [(target, 0, t) for t in targets[0]]
            pass
        else:
            # send high to outputs
            new_signals = [(target, 1, t) for t in targets[0]]
            pass
        pass
    return new_signals

signal_count = [0, 0]
for i in range(4): # Push the button!
    signals = [('-', 0, 'broadcaster')]
    while len(signals) > 0:
        # take first element from 
        signal = signals[0]
        signals = signals[1:]

        signals.extend(process(signal))
        signal_count[signal[1]] += 1

print('Low/Hi:', signal_count[0], signal_count[1])
print('Task 1: %d' % (signal_count[0] * signal_count[1] * 1000 * 1000))