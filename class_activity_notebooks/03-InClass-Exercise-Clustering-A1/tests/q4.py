from otter.test_files import test_case

OK_FORMAT = False

name = "q4"
points = 2

@test_case(points=None, hidden=False)
def test_hard_sweep(wcss_hard_by_k, best_k_elbow_hard):
    assert wcss_hard_by_k is not None, 'run sweep_k on X_hard'
    assert len(wcss_hard_by_k) == 10, 'one entry per k in range(1, 11)'
    assert all((wcss_hard_by_k[i] >= wcss_hard_by_k[i + 1] - 1e-06 for i in range(9))), 'WCSS must be non-increasing in k'
    assert best_k_elbow_hard in range(1, 11)

