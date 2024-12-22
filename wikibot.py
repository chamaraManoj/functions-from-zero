import wikipedia
import click

@click.command()
@click.option('--name', help = 'Page to search')
@click.option('--length', help = 'Length of the output')
def scrap(name="Microsoft", length = 1):
    results = wikipedia.summary(name, sentences=length)
    click.echo(click.style(f'results: {results}', fg='red' ))
    return results

if __name__ =='__main__':
    scrap()

