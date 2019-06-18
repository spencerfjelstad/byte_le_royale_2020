import unittest

import game.testing.tests


def main():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromModule(game.testing.tests))

    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(suite)


if __name__ == '__main__':
    main()
