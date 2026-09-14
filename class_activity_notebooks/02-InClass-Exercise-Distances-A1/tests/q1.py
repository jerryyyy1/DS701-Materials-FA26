from otter.test_files import test_case

OK_FORMAT = False

name = "q1"
points = 6

@test_case(points=None, hidden=False)
def test_lp_on_lecture_points(lp_distance):
    import numpy as np
    A_pt, B_pt = (np.array([3.0, 4.0]), np.array([1.0, 1.0]))
    assert abs(lp_distance(A_pt, B_pt, 1) - 5.0) < 1e-09, 'Manhattan distance of (3,4),(1,1) is 5'
    assert abs(lp_distance(A_pt, B_pt, 2) - np.sqrt(13)) < 1e-09, 'Euclidean distance is sqrt(13)'
    assert abs(lp_distance(A_pt, A_pt, 2)) < 1e-12, 'distance from a point to itself is 0'
    assert isinstance(lp_distance(A_pt, B_pt, 2), float), 'return a plain float'

@test_case(points=None, hidden=False)
def test_cosine_and_jaccard_basics(cosine_distance, jaccard_distance):
    import numpy as np
    u = np.array([1.0, 2.0, 0.0])
    assert abs(cosine_distance(u, 3 * u)) < 1e-09, 'same direction -> cosine distance 0'
    assert abs(cosine_distance(np.array([1.0, 0.0]), np.array([0.0, 1.0])) - 1.0) < 1e-09, 'orthogonal -> 1'
    a = np.array([1, 1, 1, 1, 0])
    b = np.array([1, 1, 1, 0, 1])
    assert abs(jaccard_distance(a, b) - 0.4) < 1e-09, '3 shared of 5 in the union -> 1 - 3/5'
    assert abs(jaccard_distance(a, a)) < 1e-12

@test_case(points=None, hidden=False)
def test_distance_matrix_shape(distance_matrix, lp_distance):
    import numpy as np
    P = np.array([[0.0, 0.0], [3.0, 4.0], [1.0, 1.0]])
    D = np.asarray(distance_matrix(P, lambda u, v: lp_distance(u, v, 2)))
    assert D.shape == (3, 3), 'distance_matrix must be n x n'
    assert np.allclose(np.diag(D), 0), 'zero diagonal'
    assert np.allclose(D, D.T), 'symmetric'
    assert abs(D[0, 1] - 5.0) < 1e-09 and abs(D[1, 2] - np.sqrt(13)) < 1e-09

