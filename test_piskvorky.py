from piskvorky import vyhodnot

def test_vyhodnot():
	assert vyhodnot('xxx') == 'x'
	assert vyhodnot('ooxxxoo') == 'x'
	assert vyhodnot('ooo') == 'o'
	assert vyhodnot('xxoooxx') == 'o'
	assert vyhodnot('ox') == '!'
	assert vyhodnot('-ox---') == '-'