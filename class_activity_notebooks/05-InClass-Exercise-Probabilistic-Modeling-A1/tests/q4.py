from otter.test_files import test_case

OK_FORMAT = False

name = "q4"
points = 0

@test_case(points=None, hidden=False)
def test_lln_shape(running_mean, err_at, draws, lam_hat):
    import numpy as np
    running_mean = np.asarray(running_mean)
    assert running_mean.shape == (5000,), 'one running mean per draw'
    assert np.isclose(running_mean[0], draws[0]), 'the first running mean is just the first draw'
    assert set(err_at) == {10, 100, 1000, 5000}, 'err_at needs keys 10, 100, 1000, 5000'
    assert err_at[5000] < 0.05, 'after 5000 draws the mean should be within 0.05 of lambda'

