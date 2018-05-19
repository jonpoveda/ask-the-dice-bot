# -*- coding: utf-8 -*-
""" Test suite for commands.py """
import random
import unittest
from itertools import filterfalse
from itertools import repeat
from math import sqrt
from unittest import skip

from numpy import histogram
from scipy.stats import chisquare

from src.commands import roll_parser

# Number of iterations to run the test to ensure random functions always return
# values in an expected range


# pylint: disable=line-too-long, invalid-name,


class TestCommands(unittest.TestCase):
    def test_roll_parser_results_are_in_range_when_rolling_1d10(self):
        n_iterations = 1_000
        results = map(roll_parser, repeat('1d10', n_iterations))
        not_in_range = filterfalse(
            lambda x: 1 <= x[0] <= 10,
            results)
        self.assertEqual(0, len(list(not_in_range)))

    def test_roll_parser_distribution_is_centered_when_rolling_1d10(self):
        n_iterations = 1_000_000
        results = map(roll_parser, repeat('1d10', n_iterations))
        average = sum(r[0] for r in results) / n_iterations
        self.assertAlmostEqual((10 - 0) / 2, average, delta=0.1)

    def test_roll_parser_number_of_results_when_rolling_xd10(self):
        n_iterations = 1_000
        for _ in range(n_iterations):
            n_dice = random.randint(1, 100)
            results = roll_parser(f'{n_dice}d10')
            self.assertEqual(n_dice, len(results))

    def test_roll_parser_results_are_in_range_when_rolling_1dX(self):
        n_iterations = 1_000
        for _ in range(n_iterations):
            die_type = random.randint(2, 100)
            results = map(roll_parser, repeat(f'1d{die_type}', n_iterations))
            not_in_range = filterfalse(
                lambda x: 1 <= x[0] <= die_type,
                results)
            self.assertEqual(0, len(list(not_in_range)))

    @skip('WIP')
    def test_roll_parser_distribution_is_statiscally_good_when_rolling_d10(self):
        """ Checking sample distribution using Chi-Square GoF test

        Null hyphotesis: Results follow an uniform distribution of mean 5
        """
        n_samples = 1000
        population_mean = 5.0

        results = map(roll_parser, repeat('1d10', n_samples))
        sample_mean = sum(results) / n_samples

        results = map(roll_parser, repeat('1d10', n_samples))
        # std = np.std(list(results))
        std_dev = sqrt(sum(map(lambda x: (x - population_mean) ** 2,
                               results))
                       / n_samples)

        t_score = (sample_mean - population_mean) / \
                  (std_dev / sqrt(n_samples))
        print(
            f'Mean of {sample_mean} ({population_mean}) '
            f'with an std dev of {std_dev}.\n'
            f'Results in a t-score of {t_score}')

        # threshold_for_1000_samples_couting_a_alpha_of_five_percent
        threshold = 1.646
        self.assertTrue(t_score < threshold)

    @skip('WIP')
    def test_roll_parser_distribution_is_statiscally_good_when_rolling_d10_2(self):
        """ Checking sample distribution using Chi-Square GoF test

        Null hyphotesis: Results follow an uniform distribution of mean 5
        """
        n_samples = 1000
        population_mean = 5.0

        results = map(roll_parser, repeat('1d10', n_samples))
        results = list(results)

        print(list(range(1, 11)))
        expected_frequencies = [n_samples / 10] * 10

        frequencies, bins = histogram(list(results),
                                      bins=[0.4, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5,
                                            6.5, 7.5, 8.5, 9.5])
        print(frequencies, bins, expected_frequencies)

        # results = map(roll_parser, repeat('1d10', N_ITERATIONS))
        frequencies, bins = histogram(list(results), bins=list(range(1, 12)))
        print(frequencies, bins, expected_frequencies)
        print(sum(frequencies))

        chisq, pvalue = chisquare(frequencies, expected_frequencies)
        print(chisq, pvalue)
