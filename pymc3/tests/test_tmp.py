from __future__ import division

import itertools
from .helpers import SeededTest
from ..vartypes import continuous_types
from ..model import Model, Point, Potential
from ..blocking import DictToVarBijection, DictToArrayBijection, ArrayOrdering
from ..distributions import (DensityDist, Categorical, Multinomial, VonMises, Dirichlet,
                             MvStudentT, MvNormal, ZeroInflatedPoisson,
                             ZeroInflatedNegativeBinomial, ConstantDist, Constant, Poisson, Bernoulli, Beta,
                             BetaBinomial, HalfStudentT, StudentT, Weibull, Pareto, InverseGamma,
                             Gamma, Cauchy, HalfCauchy, Lognormal, Laplace, NegativeBinomial,
                             Geometric, Exponential, ExGaussian, Normal, Flat, LKJCorr, Wald,
                             ChiSquared, HalfNormal, DiscreteUniform, Bound, Uniform,
                             Binomial, Wishart, SkewNormal)
from ..distributions import continuous, multivariate
from numpy import array, inf, log, exp
from numpy.testing import assert_almost_equal
import numpy.random as nr
import numpy as np

from scipy import integrate
import scipy.stats.distributions as sp
import scipy.stats


class TestMatchesScipy(SeededTest):
    def test_categorical(self):
        assert 0
        for i in [1]:
            assert 0
            yield self.check_categorical_bounds
        assert 0

    def check_categorical_bounds(self):
        assert 0
