from otter.test_files import test_case

OK_FORMAT = False

name = "q2"
points = 4

@test_case(points=None, hidden=False)
def test_matches_library(err_euc, err_man, err_cos, err_jac, D_euc, D_jac, X):
    import numpy as np
    assert np.asarray(D_euc).shape == (len(X), len(X)), 'D_euc must be n x n'
    assert np.asarray(D_jac).shape == (len(X), len(X)), 'D_jac must be n x n'
    for name, e in [('euc', err_euc), ('man', err_man), ('cos', err_cos), ('jac', err_jac)]:
        assert e < 1e-08, f'err_{name} = {e}: your matrix disagrees with the library'

@test_case(points=None, hidden=False)
def test_axiom_report_shape(axiom_report):
    import numpy as np
    D = np.array([[0.0, 1.0], [1.0, 0.0]])
    r = axiom_report(D)
    assert set(r) == {'zero_diag', 'symmetric', 'triangle'}, 'return the three named booleans'
    assert all((isinstance(v, (bool, np.bool_)) for v in r.values()))
    assert r['zero_diag'] and r['symmetric'] and r['triangle']

