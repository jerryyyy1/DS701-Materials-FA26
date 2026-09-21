from otter.test_files import test_case

OK_FORMAT = False

name = "q5"
points = 2

@test_case(points=None, hidden=False)
def test_outliers_shape(sizes_out_k3, hijacked, METHODS, n_samples):
    assert set(sizes_out_k3) == set(METHODS)
    for m in METHODS:
        assert len(sizes_out_k3[m]) == 3 and sum(sizes_out_k3[m]) == n_samples + 2, f'{m}: sizes must cover all {n_samples + 2} rows'
    assert isinstance(hijacked, list) and hijacked == sorted(hijacked)
    assert set(hijacked) <= set(METHODS)

