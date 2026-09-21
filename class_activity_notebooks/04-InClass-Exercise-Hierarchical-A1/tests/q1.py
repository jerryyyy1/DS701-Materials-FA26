from otter.test_files import test_case

OK_FORMAT = False

name = "q1"
points = 3

@test_case(points=None, hidden=False)
def test_linkage_shapes(Z_by_method, n_merges, METHODS, n_samples):
    import numpy as np
    assert set(Z_by_method) == set(METHODS), 'Z_by_method needs exactly the four METHODS as keys'
    for m in METHODS:
        Z = np.asarray(Z_by_method[m])
        assert Z.shape == (n_samples - 1, 4), f'{m}: linkage matrix must be (n-1, 4), got {Z.shape}'
        assert Z[-1, 3] == n_samples, f'{m}: the final merge must contain all {n_samples} points'
        assert np.all(np.diff(Z[:, 2]) >= -1e-12), f'{m}: merge heights must be non-decreasing'
    assert isinstance(n_merges, int) and n_merges == n_samples - 1

