from jinja2 import Environment, FileSystemLoader

def render_svg(angle1, angle2):
    env = Environment(loader=FileSystemLoader("assets"))
    template = env.get_template("protractor_base.svg")
    return template.render(angle1=angle1, angle2=angle2)
