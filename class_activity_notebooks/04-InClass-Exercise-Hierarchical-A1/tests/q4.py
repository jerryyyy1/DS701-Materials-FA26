from otter.test_files import test_case

OK_FORMAT = False

name = "q4"
points = 2

@test_case(points=None, hidden=False)
def test_ari_scale_shape(ari_scale):
    assert set(ari_scale) == {'cm', 'mm', 'standardized'}, 'keys must be cm / mm / standardized'
    assert all((-1.0 <= v <= 1.0 for v in ari_scale.values()))
    assert ari_scale['mm'] < ari_scale['cm'], "the unit change should hurt Ward's ARI"

