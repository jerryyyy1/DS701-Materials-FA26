from otter.test_files import test_case

OK_FORMAT = False

name = "q7"
points = 2

@test_case(points=None, hidden=False)
def test_kmeans_compare_shape(ari_kmeans, ari_best_hier, kmeans_wins, DATASETS):
    assert set(ari_kmeans) == set(DATASETS) == set(ari_best_hier)
    assert all((-1.0 <= v <= 1.0 for v in ari_kmeans.values()))
    assert isinstance(kmeans_wins, list) and set(kmeans_wins) <= set(DATASETS)

