the_glasses={1:[1,1,1,2,2,2],
             2:[1,1,1,2,2,2],
             3:[1,1,1,2,2,2],
             4:[1,1,1,2,2,2],
             5:[1,1,1,2,2,2],
             6:[1,1,1,1,1,2,2,2],
             7:[1,1,1,2,2,2,2,2,2,2],
             8:[1,2,2,2],
             9:[1,1,1,2,2,2],
             10:[1,1,1,2,2,2],
             11:[1,1,1,2,2,2]}

probability = {1:[],
             2:[],
             3:[],
             4:[],
             5:[],
             6:[],
             7:[],
             8:[],
             9:[],
             10:[],
             11:[]}


number_of_elements = 0
for key in the_glasses:
    for N in the_glasses[key]:
        if N == 1:
            number_of_elements += 1
    chance = number_of_elements / len(the_glasses[key])
    probability[key].append(chance)
    number_of_elements = 0

print(f"Вероятность выпадения 1 в каждом стакане:")
for key in probability:
    print(f"{key}: {str(probability[key]).replace('[', '').replace(']', '')}")
