from otter.test_files import test_case

OK_FORMAT = False

name = "q3"
points = 3

@test_case(points=None, hidden=False)
def test_flat_sizes_basic(flat_sizes, sizes_k3, ari_k3, METHODS, n_samples):
    import numpy as np
    Z_t = np.array([[0.0, 1.0, 1.0, 2.0], [2.0, 3.0, 5.0, 3.0]])
    assert flat_sizes(Z_t, 2) == [2, 1], 'sizes must be a list sorted largest first'
    assert flat_sizes(Z_t, 1) == [3]
    for m in METHODS:
        s = sizes_k3[m]
        assert isinstance(s, list) and len(s) == 3, f'{m}: three cluster sizes expected'
        assert sum(s) == n_samples, f'{m}: sizes must add up to {n_samples}'
        assert s == sorted(s, reverse=True), f'{m}: sort largest first'
        assert -1.0 <= ari_k3[m] <= 1.0

