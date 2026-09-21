from otter.test_files import test_case

OK_FORMAT = False

name = "q2"
points = 3

@test_case(points=None, hidden=False)
def test_n_clusters_at_height(n_clusters_at_height):
    import numpy as np
    Z_t = np.array([[0.0, 1.0, 1.0, 2.0], [2.0, 3.0, 5.0, 3.0]])
    assert n_clusters_at_height(Z_t, 0.5) == 3, 'no merge performed below 0.5'
    assert n_clusters_at_height(Z_t, 1.0) == 2, 'a merge AT the cut height counts as performed'
    assert n_clusters_at_height(Z_t, 3.0) == 2
    assert n_clusters_at_height(Z_t, 10.0) == 1

@test_case(points=None, hidden=False)
def test_cut_gives_three(n_clusters_at_height, h_cut_3, Z_by_method, k_biggest_gap, n_samples):
    from scipy.cluster.hierarchy import fcluster
    assert n_clusters_at_height(Z_by_method['ward'], h_cut_3) == 3, 'h_cut_3 must yield exactly 3 clusters'
    assert len(set(fcluster(Z_by_method['ward'], h_cut_3, criterion='distance'))) == 3
    assert 1 <= k_biggest_gap <= n_samples

