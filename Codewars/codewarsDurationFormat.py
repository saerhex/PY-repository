def format_duration(seconds):
    __years = seconds // 31536000
    __days = (seconds // 86400) % 365
    __hours = (seconds // 3600) % 24
    __minutes = (seconds // 60) % 60
    __seconds = seconds % 60

    time = {"years": __years, "days": __days, "hours": __hours,"minutes": __minutes, "seconds": __seconds}
    time_list = []
    for t in time:
        if time[t] != 0:
            time_list.append(words_ending(t,time[t]))
    return words_concate(time_list)

#Detecting words ending.
def words_ending(key,value):
    if value > 1:
        stroke = " ".join([str(value),key])
    else:
        stroke = " ".join([str(value),key[:-1]])
    return stroke

#Concating result list with ',' and 'and' separators or returning now if list is empty.
def words_concate(result_list):
    if len(result_list) > 2:
        temp_stroke = ", ".join(result_list[:-1])
        stroke = " and ".join([temp_stroke,result_list[-1]])
    elif len(result_list) == 2:
        stroke = " and ".join(result_list)
    elif len(result_list) == 1:
        stroke = result_list[-1]
    else:
        stroke = "now"
    return stroke

print(format_duration(120))