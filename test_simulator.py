from unittest import TestCase
from Simulator import *


class TestSimulator(TestCase):
    """
    Tests for ``Simulator`` implementation.
    """
    def setUp(self):
        self.sim = Simulator()

    def test_update(self):
        """
        Tests that the update functions returns an object of World type.
        """
        self.assertIsInstance(self.sim.update(), World)

    def test_get_generation(self):
        """
        Tests whether get_generation returns the correct value:
            - Generation should be 0 when Simulator just created;
            - Generation should be 2 after 2 updates.
        """
        self.assertIs(self.sim.generation, self.sim.get_generation())
        self.assertEqual(self.sim.get_generation(), 0)
        self.sim.update()
        self.sim.update()
        self.assertEqual(self.sim.get_generation(), 2)

    def test_get_world(self):
        """
        Tests whether the object passed when get_world() is called is of World type, and has the required dimensions.
        When no argument passed to construction of Simulator, world is square shaped with size 20.
        """
        self.assertIs(self.sim.world, self.sim.get_world())
        self.assertEqual(self.sim.get_world().width, 20)
        self.assertEqual(self.sim.get_world().height, 20)

    def test_set_world(self):
        """
        Tests functionality of set_world function.
        """
        world = World(10)
        self.sim.set_world(world)
        self.assertIsInstance(self.sim.get_world(), World)
        self.assertIs(self.sim.get_world(), world)

    def test_underpopulation(self):
        """
        Evaluates a scenario in which a cell would die as if by underpopulation.
        """
        world = World(10)
        self.sim.set_world(world)
        coords = [(5,5),(5,6)]
        for coord in coords:
            self.sim.get_world().set(coord[0],coord[1])
        self.sim.update()
        self.assertEqual(self.sim.get_world().get(5, 5), 0, "Cell should be dead")
        self.assertEqual(self.sim.get_world().get(5, 6), 0, "Cell should be dead")

    def test_nothinghappens(self):
        """
        Evaluates a scenario in which nothing should happen.
        """
        world = World(10)
        self.sim.set_world(world)
        coords = [(2,2),(2,3),(3,2),(3,3)]
        for coord in coords:
            self.sim.get_world().set(coord[0],coord[1])
        self.sim.update()
        self.assertEqual(self.sim.get_world().get(2, 2), 1, "Cell should be alive")
        self.assertEqual(self.sim.get_world().get(2, 3), 1, "Cell should be alive")
        self.assertEqual(self.sim.get_world().get(3, 2), 1, "Cell should be alive")
        self.assertEqual(self.sim.get_world().get(3, 3), 1, "Cell should be alive")

    def test_overpopulation(self):
        """
        Evaluates a scenario in which a cell should die.
        """
        world = World(10)
        self.sim.set_world(world)
        coords = [(2,2),(3,2),(4,2),(3,3),(3,1)]  # Star shape, atleast the center should die.
        for coord in coords:
            self.sim.get_world().set(coord[0],coord[1])
        self.sim.update()
        self.assertEqual(self.sim.get_world().get(3,2),0,"Cell should be dead")

    def test_reproduction(self):
        """
        Evaluates a scenario in which a cell should become alive (from being dead)
        """
        world = World(10)
        self.sim.set_world(world)
        coords = [(3,3),(3,4),(3,5)]
        for coord in coords:
            self.sim.get_world().set(coord[0],coord[1])
        self.sim.update()
        self.assertEqual(self.sim.get_world().get(2, 4), 1, "Cell should be alive")
        self.assertEqual(self.sim.get_world().get(4, 4), 1, "Cell should be alive")