import unittest
import angel as a
import os
import glob
import networkx as nx


class DemonTestCase(unittest.TestCase):

    def test_angel(self):
        g = nx.karate_club_graph()
        nx.write_edgelist(g, "test.csv", delimiter=" ")

        an = a.Angel("test.csv", threshold=0.6, min_comsize=3, save=True)
        coms = an.execute()
        self.assertEqual(len(coms), 4)

        os.remove("test.csv")
        os.remove("angels_coms.txt")

    def test_archangel(self):
        aa = a.ArchAngel("sgraph.txt", threshold=0.4, match_threshold=0.3)
        coms = aa.execute()
        print(coms)
        self.assertEqual(len(coms), 5)

        for f in glob.glob("ArchAngel*"):
            os.remove(f)


if __name__ == '__main__':
    unittest.main()
