from otter.test_files import test_case

OK_FORMAT = False

name = "q6"
points = 2

@test_case(points=None, hidden=False)
def test_bridge_shape(sizes_bridge_k3, largest_bridge, ari_bridge, METHODS, n_samples):
    for m in METHODS:
        assert sum(sizes_bridge_k3[m]) == n_samples + 12, f'{m}: sizes must cover all {n_samples + 12} rows'
        assert largest_bridge[m] == max(sizes_bridge_k3[m])
        assert -1.0 <= ari_bridge[m] <= 1.0

