# Voice AI digest

Daily digest of voice AI news, posted to Slack.

## How it works

A Claude Code cloud routine runs in this repo every day at 09:00 IST.
It follows the instructions in [CLAUDE.md](CLAUDE.md):

1. Search the web for voice AI news from the last 24 hours.
2. Skip items already listed in [seen.md](seen.md).
3. Write a plain-text digest to `/tmp/digest.txt`.
4. Post it with [scripts/post_to_slack.py](scripts/post_to_slack.py).
5. Append the posted items to `seen.md`, commit, and push to `main`.

## Configuration

`SLACK_WEBHOOK_URL`: the Slack Workflow Builder webhook URL. Set it as an
environment variable in the routine's cloud environment. Do not commit it.

The webhook receives a JSON body with one variable:

```json
{"message": "<digest text>"}
```

## Test the script locally

```sh
printf 'Voice AI update – test\n• Test item – hello https://example.com\n' > sample.txt
SLACK_WEBHOOK_URL=... python3 scripts/post_to_slack.py sample.txt
```

The script uses the Python 3 standard library only. It prints the HTTP status
and exits non-zero on a missing env var, a missing file, or a non-2xx response.
