from what import What
w = What('python3', '../RsaCtfTool/RsaCtfTool.py', '--publickey', '../RsaCtfTool/examples/close_primes.pub', '--private' , '--verbose','--uncipherfile', '../RsaCtfTool/examples/close_primes.cipher' )

while True:
    try:
        line = w.expect('', timeout=100)
    except:
        break
    if 'exceptions' not in line:
        print(str(line))
    else: break