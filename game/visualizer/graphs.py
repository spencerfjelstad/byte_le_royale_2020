import pygame

def health_bar(info, surf):
    structure = int(info['player'].get('city').get('structure'))
    population = int(info['player'].get('city').get('population'))
    struct = pygame.Rect(100, 600, structure//10, 50)
    pop = pygame.Rect(100,550,population//10,50)
    pygame.draw.rect(surf, pygame.Color(255,0,0), struct)
    pygame.draw.rect(surf, pygame.Color(255,255,0), pop)


def lineGraph(population_list, surf):
    #For now, here's how to draw a basic graph with random points
    #Game results, gotten from logs
    max_population = population_list.max()
    max_turns = len(population_list)

    #Border
    #Variables and rectangle declaration
    x_coord = 100
    y_coord = 100
    width = 400
    length = 200
    border = pygame.Rect(x_coord,y_coord,width,length)
    inner_border = pygame.Rect(x_coord + 2, y_coord + 2, width-4, length-4)
    #Draw rectangles
    pygame.draw.rect(surf, pygame.Color(0,0,0), border)
    pygame.draw.rect(surf, pygame.Color(0,255,255), inner_border)

    # Ticks
    #Calculating values at each tick for x and y
    #Note: Only works if length is divisible by max population
    double


    #Num of ticks to be a constant 10, the turn and pop values divided to fit
    for i in range(0,9):
        #x-axis ticks
        pygame.draw.line(surf, pygame.Color(0,0,0), (x_coord + (width*(i+1)/10), y_coord + length), (x_coord + (width*(i+1)/10), y_coord + length - 4))
        #y-axis ticks
        pygame.draw.line(surf, pygame.Color(0,0,0), (x_coord, y_coord + (length*(i+1)/10)), (x_coord + 4, y_coord + (length*(i+1)/10)))

    #Draw lines in graph
    x_origin = x_coord
    y_origin = y_coord + length
    #Test values for y value
    values = [50,67,10,100,79,56,24,79,35,78,36,35,78,17,96,46,86,23,67,56]
    for i in range(0,19):
        pygame.draw.line(surf, pygame.Color(0,0,0), (x_origin,y_origin),(x_coord + (20*(i+1)), y_coord + length - values[i]))
        x_origin = x_coord + (20*(i+1))
        y_origin = y_coord + length - values[i]

    #surf.draw.rect