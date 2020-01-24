from subprocess import Popen, PIPE


import subprocess, sys, contextlib

ON_POSIX = 'posix' in sys.builtin_module_names

cmd = [
          'python3',
          '../RsaCtfTool/RsaCtfTool.py',
          '-n',
          '163325259729739139586456854939342071588766536976661696628405612100543978684304953042431845499808366612030757037530278155957389217094639917994417350499882225626580260012564702898468467277918937337494297292631474713546289580689715170963879872522418640251986734692138838546500522994170062961577034037699354013013',
          '-e',
          '65537',
          '--verbose',
          '--private'

     ]
#['python3', '../RsaCtfTool/RsaCtfTool.py', '--publickey', '../RsaCtfTool/examples/close_primes.pub', '--private' ,'--verbose', '--uncipherfile', '../RsaCtfTool/examples/close_primes.cipher' ]
process = Popen(cmd, stdout=PIPE, stderr=subprocess.STDOUT, bufsize=1, close_fds=ON_POSIX)
#stdout, stderr = process.communicate()
while 1:
    if(process.stdout.readline() is b''):
        continue

    print(str(process.stdout.readline()))

# q = Queue()
# t = Thread(target=enqueue_output, args=(p.stdout, q))
# t.daemon = True # thread dies with the program
# t.start()


# try:  line = q.get_nowait() # or q.get(timeout=.1)
# except Empty:
#     print('no output yet')
# else:
#     print(line)


'''
while True:
    line = process.stdout.readline()
    if not line: break

    print(line)

'''

'''while True:
    out = process.stdout.read(1)
    if out == b'' and process.poll() != None:
        break
    if out != '':
        
        sys.stdout.write(str(out, encoding='utf-8'))
        sys.stdout.flush()
'''