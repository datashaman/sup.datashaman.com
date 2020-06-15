import click
import frontmatter
import parsedatetime
import re
import os
import sys

from datetime import datetime
from github import Github
from pytz import timezone

from dotenv import load_dotenv
load_dotenv()

cal = parsedatetime.Calendar()

def create_post(entry, tz):
    pattern = re.compile(r'^((?P<date>[^:]*):\s+)?\s*(?P<body>.*)$', re.MULTILINE)
    match = pattern.match(entry)
    metadata = match.groupdict()

    if metadata['date']:
        metadata['date'], _ = cal.parseDT(datetimeString=metadata['date'], tzinfo=timezone(tz))
    else:
        metadata['date'] = datetime.now(tz=timezone(tz))

    categories = re.findall(r'@([^@\s]+)\b', metadata['body'])
    if categories:
        metadata['categories'] = categories
    tags = re.findall(r'#([^#\s]+)\b', metadata['body'])
    if tags:
        metadata['tags'] = tags

    content = metadata['body'].strip()
    del metadata['body']

    return frontmatter.Post(content, **metadata)

@click.command()
@click.option('--branch', help='Branch where post content is created')
@click.option('--posts', default='_posts', help='Folder where post content is created')
@click.option('--repo', help='GitHub content repository')
@click.option('--token', help='GitHub personal access token')
@click.option('--tz', default='UTC', help='TZ database time zone')
@click.argument('entry', nargs=-1)
def cli(branch, posts, repo, token, tz, entry):
    if not entry:
        click.echo('sup', err=True)
        sys.exit(1)

    post = create_post(' '.join(entry), tz)

    github = Github(token)
    repo = github.get_user().get_repo(repo)

    filename = post['date'].strftime('%Y-%m-%d-%H%M%S')
    path = f'{posts}/{filename}.md'
    message = 'sup'
    content = frontmatter.dumps(post)

    params = {}

    if branch:
        params['branch'] = branch

    response = repo.create_file(
        path,
        message,
        content,
        **params
    )

    click.echo(response['content'].html_url)

def main():
    cli(auto_envvar_prefix='SUP')

if __name__ == '__main__':
    main()
