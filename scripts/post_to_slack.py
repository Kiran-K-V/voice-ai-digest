#!/usr/bin/env python3
"""Post a digest file to a Slack Workflow Builder webhook.

Usage: SLACK_WEBHOOK_URL=... python3 scripts/post_to_slack.py <digest-file>
"""
import json
import os
import sys
import urllib.error
import urllib.request


def main():
    if len(sys.argv) != 2:
        print("usage: post_to_slack.py <digest-file>", file=sys.stderr)
        return 2

    url = os.environ.get("SLACK_WEBHOOK_URL")
    if not url:
        print("error: SLACK_WEBHOOK_URL is not set", file=sys.stderr)
        return 1

    path = sys.argv[1]
    try:
        with open(path, encoding="utf-8") as f:
            text = f.read()
    except OSError as e:
        print(f"error: cannot read {path}: {e.strerror}", file=sys.stderr)
        return 1

    body = json.dumps({"message": text}).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            status = resp.status
    except urllib.error.HTTPError as e:
        status = e.code
    except urllib.error.URLError as e:
        # Print only the reason; the exception text could include the URL.
        print(f"error: request failed: {e.reason}", file=sys.stderr)
        return 1

    print(f"HTTP status: {status}")
    return 0 if 200 <= status < 300 else 1


if __name__ == "__main__":
    sys.exit(main())
