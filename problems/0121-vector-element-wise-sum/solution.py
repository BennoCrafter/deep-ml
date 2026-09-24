def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	if len(a) != len(b):
		return -1

	res = []
	for ap, bp in zip(a, b):
		res.append(ap+bp)

	return res