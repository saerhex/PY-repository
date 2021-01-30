from string import ascii_lowercase

rates = {v: i for i, v in enumerate(ascii_lowercase)}

def prize_draw(st, we, n):
    if n > len(we): return 'Not enough participants'
    if not n: 'No participants'
    names, w_nums = st.split(','), {}
    for i in range(len(we)):
        w_nums[names[i]] = we[i] * get_som(names[i])
    
    
def get_som(name):
    ords = sum(rates[sym.lower()] for sym in name)
    return len(name) + ords