# создать генератор геометрической прогресии

def geometric_progression(number: int, denominator: int, length_progression: int):
    counter = 0
    while length_progression > 0:
        if counter != 0:
            number *= denominator
            length_progression -= 1
            counter += 1
            yield number
        else:
            length_progression -= 1
            counter +=1
            yield number


gen_five = geometric_progression(5, 2, 4)
print(next(gen_five))
print(next(gen_five))
print(next(gen_five))
print(next(gen_five))




