def sort_csv(csv):
    n, p, s = (line.split(';') for line in csv.split('\n'))
    names = {n[i] : (p[i], s[i]) for i in range(len(n))}
    n, p, s = 
    return '\n'.join(';'.join(name) for name)

post_sorting = (
             "Dentzil;myjinxin2015;raulbc777;smile67;SteffenVogel_79\n"
             "3907;17945;10091;10088;10132\n"
             "48;2;12;13;11"
        )
    
print(sort_csv(post_sorting))