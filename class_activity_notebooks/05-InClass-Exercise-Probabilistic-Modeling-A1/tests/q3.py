from otter.test_files import test_case

OK_FORMAT = False

name = "q3"
points = 4

@test_case(points=None, hidden=False)
def test_poisson_shapes(lam_hat, expected_counts, observed_counts, var_over_mean, p_ge3_model, p_ge3_emp, counts):
    import numpy as np
    assert isinstance(lam_hat, float) and 0 < lam_hat < 2, 'lam_hat should be a float, well under 2 deaths/year'
    assert np.asarray(expected_counts).shape == (7,) and np.asarray(observed_counts).shape == (7,)
    assert abs(np.sum(observed_counts) - len(counts)) == 0, 'observed_counts must add up to the number of corps-years'
    assert abs(np.sum(expected_counts) - len(counts)) < 0.5, 'expected_counts should add up to (almost) the number of corps-years'
    assert 0.7 < var_over_mean < 1.3, 'for Poisson-like counts variance/mean is near 1'
    assert 0 <= p_ge3_model <= 0.1 and 0 <= p_ge3_emp <= 0.1

