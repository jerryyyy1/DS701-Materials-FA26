from otter.test_files import test_case

OK_FORMAT = False

name = "q1"
points = 4

@test_case(points=None, hidden=False)
def test_gaussian_fit_shape(mu_hat, sigma2_hat, sigma_hat, mu_sp, sigma_sp, x):
    import numpy as np
    for v in (mu_hat, sigma2_hat, sigma_hat, mu_sp, sigma_sp):
        assert isinstance(v, float), 'store plain Python floats'
    assert x.min() < mu_hat < x.max(), 'mu_hat should sit inside the data range'
    assert sigma2_hat > 0 and np.isclose(sigma_hat ** 2, sigma2_hat), 'sigma_hat must be the square root of sigma2_hat'
    assert np.isclose(mu_hat, mu_sp, atol=1e-06), "your mu_hat should match scipy's norm.fit"
    assert np.isclose(sigma_hat, sigma_sp, atol=1e-06), "your sigma_hat should match scipy's (did you divide by N, not N-1?)"

