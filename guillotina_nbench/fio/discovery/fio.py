import asyncio
import json
import re
import sys
from asyncio.subprocess import PIPE, STDOUT

json_body = []


async def run_fio():
    proc = await asyncio.create_subprocess_shell(
        'docker run --rm -v ~/Downloads/fio/:/fio ljishen/fio --output-format=json --bandwidth-log --eta-newline=1 --client=192.168.86.29 /fio/test.fio',
        stdout=asyncio.subprocess.PIPE,
        stdin=asyncio.subprocess.PIPE,
    )
    try:
        await asyncio.wait([print_stream(proc.stdout), print_stream(proc.stderr)])
        json_parsed = json.loads(''.join(json_body))
        # pass this to grifana some how or another.
    except Exception:
        # Terminate process on all exceptions
        proc.terminate()


async def print_stream(stream):
    json_started = False
    try:
        while True:
            line = await stream.readline()
            if line:
                #print(line.decode('utf-8'), end='')
                text = line.decode('utf-8')
                if json_started:
                    json_body.append(text)
                else:
                    if 'Jobs' in text:
                        # TODO: pass this to Grafinna
                        print("Running output: {}".format(text))
                        #m = re.search(r"\[([A-Za-z0-9_]+)\]", text)
                        m = re.findall(r"\[.*?\]", text)
                        if len(m) > 0:
                            print(m[0])
                            print(m[1])

                    elif '{' in text:
                        json_started = True
                        json_body.append(text)
            else:
                break
    except AttributeError as E:
        pass


if __name__ == '__main__':
    try:
        asyncio.run(run_fio())
    except KeyboardInterrupt:
        print('\n Killed servers')
