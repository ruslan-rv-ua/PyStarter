import click

@click.command()
@click.option('--name', '-n', prompt='Your name', help='The person to greet.', default='world')
def hello(name):
    click.echo(f'Hello {name}!')

hello()

# python file.py --help
# python file.py --name Jane