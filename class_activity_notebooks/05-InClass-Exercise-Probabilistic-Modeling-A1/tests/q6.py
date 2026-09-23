from otter.test_files import test_case

OK_FORMAT = False

name = "q6"
points = 0

@test_case(points=None, hidden=False)
def test_ci95_and_coverage(ci95, coverage_30, coverage_5, mean_width_30, mean_width_120):
    import numpy as np
    lo, hi = ci95(np.array([1.0, 2.0, 3.0, 4.0, 5.0]))
    assert abs(lo - (3 - 1.959964 * np.sqrt(0.5))) < 0.0001 and abs(hi - (3 + 1.959964 * np.sqrt(0.5))) < 0.0001, 'ci95 should be xbar +/- 1.96 * s/sqrt(n) with s using ddof=1'
    for c in (coverage_30, coverage_5):
        assert isinstance(c, float) and 0.5 <= c <= 1.0
    assert 0.9 <= coverage_30 <= 0.97, 'with n = 30 the coverage should be in the low-to-mid 90s'
    assert coverage_5 < coverage_30, 'small samples from a skewed population under-cover'
    assert 1.6 < mean_width_30 / mean_width_120 < 2.4, '4x the data should roughly halve the width (1/sqrt(n))'

