import click
import capas.getjornals

@click.command()
@click.option('--start', help='First date. Format: 2021-12-21')
@click.option('--end', help='Last Date. Format: 2021-12-21')
def main(start, end):
    jornals = capas.getjornals.GetJornals()
    jornals.get_jornals_range(start, end)

if __name__ == "__main__":
    main()
