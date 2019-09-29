import pygame

def health_bar(info, surf):
    structure = int(info['player'].get('city').get('structure'))
    population = int(info['player'].get('city').get('population'))
    struct = pygame.Rect(100, 600, structure, 50)
    pop = pygame.Rect(100,550,population,50)
    pygame.draw.rect(surf, pygame.Color(255,0,0), struct)
    pygame.draw.rect(surf, pygame.Color(255,255,0), pop)


def lineGraph(population_list, final_width, final_height):
    #For now, here's how to draw a basic graph with random points
    #Game results, gotten from logs
    max_population = max(population_list)
    max_turns = len(population_list)

    #surface to be returned
    data_surf = pygame.Surface((max_turns,max_population))
    surf = pygame.Surface((final_width + 4, final_height + 4))

    #Border
    #Variables and rectangle specifications based on population and turns. To be scaled down to length and width
    x_coord = 0
    y_coord = 0
    height = max_population + 5
    width = max_turns

    data_surf.fill(pygame.Color(0, 255, 255))

    #Draw lines in graph
    x_origin = x_coord
    y_origin = y_coord + height
    #Test values for y value
    #values = [50,67,10,100,79,56,24,79,35,78,36,35,78,17,96,46,86,23,67,56]
    for i in range(0,max_turns):
        population = population_list.pop(0)
        if(i != 0):
            pygame.draw.line(data_surf, pygame.Color(0,0,0), (x_origin,y_origin),(x_coord + i, y_coord + height - population))
        x_origin = x_coord + i
        y_origin = y_coord + height - population

    data_surf = pygame.transform.scale(data_surf,(final_width,final_height))

    border_width = final_width + 4
    border_height = final_height + 4

    border = pygame.Rect(x_coord, y_coord, border_width, border_height)
    #Inner border
    #inner_border = pygame.Rect(x_coord + 2, y_coord + 2, width - 4, height - 4)
    # Draw rectangles
    pygame.draw.rect(surf, pygame.Color(0, 0, 0), border)
    #Inner border
    surf.blit(data_surf, (2,2))
    #pygame.draw.rect(data_surf, pygame.Color(0, 255, 255), inner_border)

    # Ticks
    # Calculating values at each tick for x and y
    # Note: Only works if length is divisible by max population

    # Num of ticks to be a constant 10, the turn and pop values divided to fit
    for i in range(0, 9):
        # x-axis ticks
        pygame.draw.line(surf, pygame.Color(0, 0, 0), (x_coord + (border_width * (i + 1) / 10), y_coord + border_height),
                         (x_coord + (border_width * (i + 1) / 10), y_coord + border_height - 4))
        # y-axis ticks
        pygame.draw.line(surf, pygame.Color(0, 0, 0), (x_coord, y_coord + (border_height * (i + 1) / 10)),
                         (x_coord + 4, y_coord + (border_height * (i + 1) / 10)))

    return surf
    #surf.draw.rect