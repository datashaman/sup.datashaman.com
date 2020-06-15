import click
import frontmatter
import parsedatetime
import re
import os
import uuid

from datetime import datetime
from github import Github
from pytz import timezone

from dotenv import load_dotenv
load_dotenv()

cal = parsedatetime.Calendar()
TZ = os.getenv('TZ')

def create_post(entry):
    pattern = re.compile(r'^((?P<date>[^:]*):)?\s*(?P<body>.*)$', re.MULTILINE)
    match = pattern.match(entry)
    metadata = match.groupdict()

    if metadata['date']:
        metadata['date'], _ = cal.parseDT(datetimeString=metadata['date'], tzinfo=timezone(TZ))
    else:
        metadata['date'] = datetime.now(tz=timezone(TZ))

    metadata['categories'] = re.findall(r'@([^@\s]+)\b', metadata['body'])
    metadata['tags'] = re.findall(r'#([^#\s]+)\b', metadata['body'])

    content = metadata['body'].strip()
    del metadata['body']

    return frontmatter.Post(content, **metadata)

@click.command()
@click.argument('entry', nargs=-1)
def cli(entry):
    post = create_post(' '.join(entry))

    g = Github(os.getenv('GITHUB_TOKEN'))

    posts = os.getenv('GITHUB_POSTS', '_posts')
    published = post['date'].strftime('%Y-%m-%d')
    post_id = uuid.uuid4()
    path = f'{posts}/{published}-{post_id}.md'
    message = 'sup'
    content = frontmatter.dumps(post)
    g.get_user().get_repo(os.getenv('GITHUB_REPO')).create_file(path, message, content)
