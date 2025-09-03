import math
from jinja2 import Environment, FileSystemLoader

def polar_to_cartesian(center_x, center_y, radius, angle_deg):
    angle_rad = math.radians(angle_deg)
    x = center_x + radius * math.cos(angle_rad)
    y = center_y - radius * math.sin(angle_rad)
    return x, y

def describe_arc(x, y, radius, start_angle, end_angle):
    start = polar_to_cartesian(x, y, radius, start_angle)
    end = polar_to_cartesian(x, y, radius, end_angle)

    large_arc_flag = 1 if (end_angle - start_angle) % 360 > 180 else 0

    return f"M {start[0]} {start[1]} A {radius} {radius} 0 {large_arc_flag} 0 {end[0]} {end[1]}"

def render_svg(angle1, angle2):
    center_x, center_y, radius = 200, 200, 180
    x1, y1 = polar_to_cartesian(center_x, center_y, radius, angle1)
    x2, y2 = polar_to_cartesian(center_x, center_y, radius, angle2)
    arc_path = describe_arc(center_x, center_y, radius - 10, angle1, angle2)

    env = Environment(loader=FileSystemLoader("assets"))
    template = env.get_template("protractor_base.svg")
    return template.render(x1=x1, y1=y1, x2=x2, y2=y2, arc_path=arc_path)
