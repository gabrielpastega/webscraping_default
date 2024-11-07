from mitmproxy.tools.main import mitmdump
import os
from pathlib import Path

username = os.getenv("DEFAULT_PROXY_USERNAME")
password = os.getenv("DEFAULT_PROXY_PASSWORD")
server = os.getenv("DEFAULT_PROXY_SERVER", 'brd.superproxy.io')
port = os.getenv("DEFAULT_PROXY_PORT", 22225)

mitmdump(args=[
    "-s", "src/mimt/addon/proxy_controller.py",
    "--mode", f"upstream:http://{server}:{port}",
    "--upstream-auth", f"{username}:{password}",
    "--set stream_large_bodies=5g",
    "--set connection_strategy=lazy",
    "--set upstream_cert=false",
    "--ssl-insecure"
]

)