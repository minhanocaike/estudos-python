### In a small town the population is p0 = 1000 at the beginning of a year.
#  The population regularly increases by 2 percent per year and moreover 50 new inhabitants per year come to live in the town. 
# How many years does the town need to see its population greater or equal to p = 1200 inhabitants?

def nb_year(p0, percent, aug, p):
    
    # O total de anos para atingit p
    nb_year = 0 

    # Loop para repetição em quanto a diferença for maior que zero
    while((p - p0) > 0):
        
        # Formula de cresciment0
        p0 += (p0 * (percent/100)) + aug;

        nb_year += 1;

    return nb_year

print(nb_year(1500, 5, 100, 5000));
