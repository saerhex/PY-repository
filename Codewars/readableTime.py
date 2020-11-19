make_readable = lambda sec: ':'.join(['0'+str(t) if t < 10 else str(t) for t in [(sec // 3600), (sec // 60) % 60, sec % 60]])
#I converted it in a human-readable time format with a non-readable function.
#Ironic.