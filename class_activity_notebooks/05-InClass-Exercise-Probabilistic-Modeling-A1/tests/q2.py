from otter.test_files import test_case

OK_FORMAT = False

name = "q2"
points = 4

@test_case(points=None, hidden=False)
def test_fit_check_ranges(frac_within_1, frac_within_2, p_tail_model, p_tail_emp, n_expected_hot, N):
    for v in (frac_within_1, frac_within_2, p_tail_model, p_tail_emp):
        assert isinstance(v, float) and 0.0 <= v <= 1.0, 'fractions/probabilities must be floats in [0, 1]'
    assert frac_within_1 < frac_within_2, 'more of the data lies within 2 sigma than within 1 sigma'
    assert 0.6 < frac_within_1 < 0.75 and 0.9 < frac_within_2 < 0.99, 'for a roughly Gaussian month these should land near 0.68 and 0.95'
    assert p_tail_model < 0.2 and p_tail_emp < 0.2, 'the tail beyond T0 is a small probability'
    assert abs(n_expected_hot - N * p_tail_model) < 1e-06, 'n_expected_hot = N * p_tail_model'

