from pathlib import Path
import re
import shutil


def generate_template(url: str) -> None:
    """Generate a template for atcoder problem.
    
    Args:
        url (str): URL of the contest top page.
    """
    template_directory = Path('./src/template')

    # Get the contest name
    contest_name = url.split('/')[4]

    contest_kind = re.search(r'abc|arc|agc', contest_name).group()
    contest_number = re.search(r'\d{3}', contest_name).group()

    # Create a directory for the contest
    source_root_directory = Path('./src')

    # Create a file for the contest
    contest_directory = shutil.copytree(
        template_directory,
        source_root_directory / contest_kind / contest_number)


if __name__ == '__main__':
    url = input('URL: ')
    generate_template(url)
