from otter.test_files import test_case

OK_FORMAT = False

name = "q5"
points = 0

@test_case(points=None, hidden=False)
def test_clt_shapes(sample_means, sd_of_means, sd_predicted, n_values, lam_hat):
    import numpy as np
    out = sample_means(5, 10, np.random.default_rng(0))
    assert np.asarray(out).shape == (10,), 'sample_means(n, R, rng) must return R sample means'
    assert set(sd_of_means) == set(n_values) and set(sd_predicted) == set(n_values)
    sds = [sd_of_means[n] for n in n_values]
    assert all((sds[i] > sds[i + 1] for i in range(len(sds) - 1))), 'the spread of the sample mean must shrink as n grows'
    for n in n_values:
        assert np.isclose(sd_predicted[n], np.sqrt(lam_hat / n)), 'sd_predicted[n] = sqrt(lambda / n)'

