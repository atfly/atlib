
def HSL2RGB(h, s, l):
	u"HSL -> RGB，返回一个元组，格式为：(r, g, b)"

	if s > 0:
		v_1_3 = 1.0 / 3
		v_1_6 = 1.0 / 6
		v_2_3 = 2.0 / 3

		q = l * (1 + s) if l < 0.5 else l + s - (l * s)
		p = l * 2 - q
		hk = h / 360.0 # h 规范化到值域 [0, 1) 内
		tr = hk + v_1_3
		tg = hk
		tb = hk - v_1_3

		rgb = [
			tc + 1.0 if tc < 0 else
			tc - 1.0 if tc > 1 else
			tc
			for tc in (tr, tg, tb)
		]

		rgb = [
			p + ((q - p) * 6 * tc) if tc < v_1_6 else
			q if v_1_6 <= tc < 0.5 else
			p + ((q - p) * 6 * (v_2_3 - tc)) if 0.5 <= tc < v_2_3 else
			p
			for tc in rgb
		]

		rgb = tuple(int(i * 256) for i in rgb)

	# s == 0 的情况
	else:
		rgb = l, l, l

	return rgb
#www.iplaypy.com