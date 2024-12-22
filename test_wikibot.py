from wikibot import scrap

from click.testing import CliRunner

def test_scrap():
    runner = CliRunner()
    result = runner.invoke(scrap, ['--name','Microsoft', '--length', '10'])
    assert result.exit_code == 0
    assert 'Microsoft' in  result.output

