import click

@click.command()
@click.argument('integer_1', type=int)
@click.argument('integer_2', type=int)
def add_two_numbers(integer_1, integer_2):
    """Add two integers together."""
    click.echo(f"The sum of {integer_1} and {integer_2} is {integer_1 + integer_2}")

if __name__ == "__main__":
    add_two_numbers()
