from World import *

class Simulator:
    """
    Game of Life simulator. Handles the evolution of a Game of Life ``World``.
    Read https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life for an introduction to Conway's Game of Life.
    """

    def __init__(self, world = None, birth = [3], survival = [2,3], age = None):
        """
        Constructor for Game of Life simulator.

        :param world: (optional) environment used to simulate Game of Life.
        """
        self.generation = 0
        if world == None:
            self.world = World(20)
        else:
            self.world = world

        self.age = age
        self.birth = birth
        self.survival = survival

    def update(self) -> World:
        """
        Updates the state of the world to the next generation. Uses rules for evolution.

        :return: New state of the world.
        """
        self.generation += 1

        # Iterate over all the cells.
        newworld = World(self.world.width, self.world.height)

        # Determine if age rules are implemented.
        if self.age is None:
            birthvalue = 1
            deadvalue = 0
        elif self.age is not None:
            birthvalue = self.age - 2
            deadvalue = 0 + 2

        for x in range(self.world.width):
            for y in range(self.world.height):
                neighbors = self.world.get_neighbours(x, y)  # Haal de buren op van een cel.
                neighborcount = sum(neighbors)
                if self.world.get(x,y) == 0:  # Cel is dood
                    if neighborcount in self.birth:
                        newworld.set(x,y,1)
                    # if sum(neighbors) == 3:  # Moet er precies drie zijn!!
                    #     newworld.set(x,y,1)
                    else:  # Anders gebeurt er niks.
                        newworld.set(x,y,0)
                elif self.world.get(x,y) == 1:  # Cel is levend.
                    if neighborcount in self.survival:
                        newworld.set(x,y,1)
                    # if sum(neighbors) < 2:  # Een cel met minder dan twee levende buren gaat dood.
                    #     newworld.set(x,y,0)
                    # elif sum(neighbors) > 3:  # Een cel met meer dan drie levende buren gaat dood.
                    #     newworld.set(x,y,0)
                    else:  # Anders gebeurt er niks.
                        newworld.set(x,y,0)

        self.world = newworld

        return self.world

    def get_generation(self):
        """
        Returns the value of the current generation of the simulated Game of Life.

        :return: generation of simulated Game of Life.
        """
        return self.generation

    def get_world(self):
        """
        Returns the current version of the ``World``.

        :return: current state of the world.
        """
        return self.world

    def set_world(self, world: World) -> None:
        """
        Changes the current world to the given value.

        :param world: new version of the world.

        """
        self.world = world