def intersect(c, p1, p2, p3, p4):
    return (
        point_in_rectangle(c, p1, p4)
        or rectangle_intersects_circle(c, p1, p2)
        or rectangle_intersects_circle(c, p1, p3)
        or rectangle_intersects_circle(c, p2, p3)
        or rectangle_intersects_circle(c, p2, p4)
    )


def point_in_rectangle(c, p0, p1):
    cx, cy, _ = c
    x0, y0 = p0
    x1, y1 = p1
    if x0 > x1:
        x0, x1 = x1, x0
    if y0 > y1:
        y0, y1 = y1, y0
    return x0 <= cx and cx <= x1 and y0 <= cy and cy <= y1


def rectangle_intersects_circle(c, p1, p2):
    (p1x, p1y), (p2x, p2y), (cx, cy, r) = p1, p2, c
    (x1, y1), (x2, y2) = (p1x - cx, p1y - cy), (p2x - cx, p2y - cy)
    dx, dy = (x2 - x1), (y2 - y1)
    dr = (dx**2 + dy**2) ** 0.5
    big_d = x1 * y2 - x2 * y1
    discriminant = r**2 * dr**2 - big_d**2

    if discriminant < 0:  # No intersection between circle and line
        return False
    else:  # There may be 0, 1, or 2 intersections with the segment
        intersections = [
            (
                cx
                + (big_d * dy + sign * (-1 if dy < 0 else 1) * dx * discriminant**0.5)
                / dr**2,
                cy + (-big_d * dx + sign * abs(dy) * discriminant**0.5) / dr**2,
            )
            for sign in ((1, -1) if dy < 0 else (-1, 1))
        ]  # This makes sure the order along the segment is correct
        fraction_along_segment = [
            (xi - p1x) / dx if abs(dx) > abs(dy) else (yi - p1y) / dy
            for xi, yi in intersections
        ]
        intersections = [
            pt
            for pt, frac in zip(intersections, fraction_along_segment)
            if 0 <= frac <= 1
        ]

        return len(intersections) > 0
