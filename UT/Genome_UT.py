import unittest
import Genome
import GAutils


class TestGenomeClass(unittest.TestCase):

    def test_Genome_range(self):
        min = 0.2
        max = 0.22
        range = [min, max]
        subject = Genome.Genome(20, 20, 50, 5, 3)
        subject.setRange(min, max)
        self.assertEqual(range, subject.getRange())
        min = 0.2
        max = 0.22
        self.assertTrue(subject.setRange(min, max))
        min = 0.2
        max = 0.18
        self.assertFalse(subject.setRange(min, max))

    def test_Genome_eval(self):
        subject = Genome.Genome(20, 20, 50, 5, 3)
        subject.evaluate()
        self.assertTrue(subject.penalty < 1 and subject.penalty > 0)
        self.assertTrue(subject.fitness < 1 and subject.fitness > 0)
        self.assertTrue(subject.fitness + subject.penalty == 1)

    def test_shade_calc(self):
        subject = Genome.Genome(20, 20, 50, 5, 3)
        subject.calculate_shade_in_solution(20)
        for i in range(GAutils.CONST_SEQUENCE_LENGTH):
            self.assertTrue(0 <= subject.getSequence()[i].shade <= 1)


if __name__ == '__main__':
    unittest.main()
