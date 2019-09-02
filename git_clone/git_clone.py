import zipfile
import os
import re
import sys
import ssl
import sys
import time


try:
    from urllib.error import URLError
    from urllib import request as urllib2
except ImportError:
    from urllib2 import URLError
    import urllib2


headers = {
    'User-Agent':
    r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
    'Connection': 'keep-alive',
    'Accept-Encoding': 'identity',
}


def git_clone(git_url, path=os.getcwd(), branch_name='master'):
    git_url = git_url.replace(' ', '')
    if git_url[-1] == '/':
        git_url = git_url[:-1]
    elif git_url[-4:] == '.git':
        git_url = git_url[:-4]
    username, projectname = re.match('https://github.com/(.+)/(.+)',
                                     git_url).groups()[0:2]
    url = 'https://codeload.github.com/{}/{}/zip/{}'.format(
        username, projectname, branch_name)
    filename = path + '/' + projectname
    zipfile_name = filename + '.zip'
    try:
        urllib2.urlretrieve(url,
                            zipfile_name, reporthook=report_hook)
    except URLError:
        headers['Host'] = 'github.com'
        request = urllib2.Request(
            'https://github.com/{}/{}'.format(username, projectname),
            headers=headers)
        response = urllib2.urlopen(request)

        pattern = '/{}/{}/tree/(.*?)/'.format(username, projectname)
        b_name = re.findall(pattern, str(response.read()))[-1]
        return git_clone(git_url, path, b_name)

    with zipfile.ZipFile(zipfile_name, 'r') as f:
        f.extractall(path + '/.')
    if os.path.exists(filename + '-' + branch_name):
        os.rename(filename + '-' + branch_name, filename)
    os.remove(zipfile_name)
    print('\n{} downloaded'.format(git_url))


def report_hook(count, block_size, total_size):
    global start_time
    if count == 0:
        start_time = time.time()
        return

    duration = time.time() - start_time + 0.000001
    progress_size = int(count * block_size)
    speed = int(progress_size / (1024 * duration))
    percent = int(count * block_size * 100 / total_size)
    if 100 >= percent >= 0:
        sys.stdout.write("\r{} %, {} KB, {} KB/s, {} seconds passed         " .format(
            percent, progress_size / 1024, speed, round(duration,2)))
    else:
        sys.stdout.write("\r{} KB, {} KB/s, {} seconds passed         " .format(
            progress_size / 1024, speed, round(duration,2)))
    sys.stdout.flush()


def execute():
    length = len(sys.argv)
    if length == 2:
        git_clone(sys.argv[1])
    elif length == 3:
        git_clone(sys.argv[1], sys.argv[2])
    elif length == 4:
        git_clone(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print('Parameters Error')
