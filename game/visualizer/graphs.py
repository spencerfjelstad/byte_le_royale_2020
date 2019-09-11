import pygame

def health_bar(info, surf):
    structure = int(info['player'].get('city').get('structure'))
    population = int(info['player'].get('city').get('population'))
    struct = pygame.Rect(100, 600, structure, 50)
    pop = pygame.Rect(100,550,population,50)
    pygame.draw.rect(surf, pygame.Color(255,0,0), struct)
    pygame.draw.rect(surf, pygame.Color(255,255,0), pop)


def lineGraph(surf):
    #For now, here's how to draw a basic graph with random points
    #Game results, to be gotten from logs
    max_population = 100
    max_turns = 200
    #Border
    #Variables and rectangle declaration
    x_coord = 100
    y_coord = 100
    width = 250
    length = 200
    border = pygame.Rect(x_coord,y_coord,width,length)
    inner_border = pygame.Rect(x_coord + 2, y_coord + 2, width-4, length-4)
    #Draw rectangles
    pygame.draw.rect(surf, pygame.Color(0,0,0), border)
    pygame.draw.rect(surf, pygame.Color(0,255,255), inner_border)

    #Ticks
    #Num of ticks to be a constant 10, the turn and pop values divided to fit
    for i in range(0,9):
        pygame.draw.line(surf, pygame.Color(0,0,0), (x_coord + (width*(i+1)/10), y_coord + length -1), (x_coord + (width*(i+1)/10), y_coord + length + 1))


    #surf.draw.rect