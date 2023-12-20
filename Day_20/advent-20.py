
file_name = './Day_20/sample-20.1.txt'

# % -> FlipFlop, initially off 0. high -> nothing. low -> toggle on/off. off/on -> send hi. off/on -> send lo
# & -> Conjunct, 

modules = {}
for line in open(file_name).read().splitlines():
    module, targets = line.split(' -> ')
    if module.startswith('%'):
        modules[module[1:]] = ['%', 0, targets.split(', ')]
    elif module.startswith('&'):
        modules[module[1:]] = ['&', 0, targets.split(', ')]
    else:
        modules[module] = ['b', 0, targets.split(', ')]

[print(m,v) for m,v in modules.items()]

for name, module in modules.items():
    if module[0] == '&':
        module.append([0] * len(module[2]))

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
            new_signals = [(target, modules[target][1],t) for t in targets[0]] # TODO: ignore 1 signals to %
    elif type == '&':
        sending_module = source
        index = targets[0].index(sending_module)
        pass
    return new_signals

signals = [('-', 0, 'broadcaster')]
signal_count = [0, 0]
while len(signals) > 0:
    # take first element from 
    signal = signals[0]
    signals = signals[1:]

    signals.extend(process(signal))
    signal_count[signal[1]] += 1

print('Low/Hi:', signal_count[0], signal_count[1])