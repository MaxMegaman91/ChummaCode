from dataclasses import dataclass
from math import atan2, degrees, hypot


INCH_TO_MM = 25.4


@dataclass(frozen=True)
class Point:
	x_in: float
	y_mm: float

	def as_mm(self) -> tuple[float, float]:
		return self.x_in * INCH_TO_MM, self.y_mm


def read_point(name: str) -> Point:
	print(f"Enter {name}:")
	x_in = float(input("  xpos (inches): "))
	y_mm = float(input("  ypos (mm): "))
	return Point(x_in=x_in, y_mm=y_mm)


def distance_mm(point_a: Point, point_b: Point) -> float:
	ax, ay = point_a.as_mm()
	bx, by = point_b.as_mm()
	return hypot(bx - ax, by - ay)


def line_angle_deg(point_a: Point, point_b: Point) -> float:
	ax, ay = point_a.as_mm()
	bx, by = point_b.as_mm()
	return degrees(atan2(by - ay, bx - ax))


def normalize_angle_deg(angle: float) -> float:
	while angle <= -180:
		angle += 360
	while angle > 180:
		angle -= 360
	return angle


def point_line_distance_mm(point: Point, line_start: Point, line_end: Point) -> float:
	px, py = point.as_mm()
	ax, ay = line_start.as_mm()
	bx, by = line_end.as_mm()
	line_dx = bx - ax
	line_dy = by - ay
	line_length = hypot(line_dx, line_dy)
	if line_length == 0:
		raise ValueError("A secant line cannot be formed from identical points.")
	return abs(line_dx * (ay - py) - (ax - px) * line_dy) / line_length


def corrected_l1(pl1: Point, pu1: Point, pl2: Point, pu2: Point) -> tuple[float, float, float]:
	raw_l1 = distance_mm(pl1, pu1)
	angle_1 = line_angle_deg(pl1, pu1)
	angle_2 = line_angle_deg(pl2, pu2)
	angle_change = normalize_angle_deg(angle_2 - angle_1)

	distance_1 = point_line_distance_mm(pl1, pu1, pu2)
	distance_2 = point_line_distance_mm(pu2, pl1, pl2)
	c_l1 = (distance_1 + distance_2) / 2
	return raw_l1, c_l1, angle_change


def main() -> None:
	print("Enter four points for the two lines.")
	pl1 = read_point("pl1")
	pu1 = read_point("pu1")
	pl2 = read_point("pl2")
	pu2 = read_point("pu2")

	raw_l1, c_l1, angle_change = corrected_l1(pl1, pu1, pl2, pu2)

	print()
	print(f"l1 = {raw_l1:.3f} mm")
	print(f"c_l1 = {c_l1:.3f} mm")
	print(f"angle change = {angle_change:.3f} deg")


if __name__ == "__main__":
	main()
