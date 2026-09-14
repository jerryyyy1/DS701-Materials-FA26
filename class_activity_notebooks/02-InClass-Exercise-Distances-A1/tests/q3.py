from otter.test_files import test_case

OK_FORMAT = False

name = "q3"
points = 6

@test_case(points=None, hidden=False)
def test_nearest_and_accuracy_helpers(nearest, loo_1nn_accuracy):
    import numpy as np
    D = np.array([[0.0, 1.0, 4.0, 2.0], [1.0, 0.0, 3.0, 5.0], [4.0, 3.0, 0.0, 1.5], [2.0, 5.0, 1.5, 0.0]])
    assert list(nearest(D, 0, 2)) == [1, 3], 'closest first, and never the row itself'
    assert list(nearest(D, 2, 1)) == [3]
    y = np.array([0, 0, 1, 1])
    assert abs(loo_1nn_accuracy(D, y) - 1.0) < 1e-12, "every row's nearest neighbor shares its label here"
    assert abs(loo_1nn_accuracy(D, np.array([0, 1, 0, 1])) - 0.0) < 1e-12

@test_case(points=None, hidden=False)
def test_part3_variables_exist(nn_by_metric, acc_raw, acc_std, nn_std, dominant_feature, dominant_share, feature_names, QUERY):
    assert set(nn_by_metric) == {'euclidean', 'manhattan', 'cosine', 'jaccard'}
    for m, idx in nn_by_metric.items():
        assert len(idx) == 5 and QUERY not in idx, f'{m}: 5 neighbors, not including the query'
    assert 0.0 <= acc_raw <= 1.0 and 0.0 <= acc_std <= 1.0
    assert acc_std > acc_raw, 'standardizing should improve 1-NN accuracy on the wine data'
    assert dominant_feature in feature_names, 'dominant_feature must be a feature NAME'
    assert 0.5 < dominant_share <= 1.0, 'one feature dominates the variance here'

