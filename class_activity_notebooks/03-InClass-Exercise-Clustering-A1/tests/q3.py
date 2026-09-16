from otter.test_files import test_case

OK_FORMAT = False

name = "q3"
points = 3

@test_case(points=None, hidden=False)
def test_k_sweep(wcss_by_k, best_k_elbow, elbow_k):
    assert wcss_by_k is not None, 'run sweep_k on X and store the result in wcss_by_k'
    assert len(wcss_by_k) == 10, 'wcss_by_k needs one entry per k in range(1, 11)'
    assert all((wcss_by_k[i] >= wcss_by_k[i + 1] - 1e-06 for i in range(9))), 'WCSS must be non-increasing in k'
    assert best_k_elbow in range(1, 11), 'best_k_elbow must be one of the swept k'
    toy = [100.0, 10.0, 9.5, 9.2, 9.0]
    assert elbow_k(toy) == 2, f'elbow_k on an obvious curve returned {elbow_k(toy)}'

