# Voice AI digest routine

This repo runs a daily Claude Code cloud routine at 09:00 IST.
The routine finds voice AI news from the last 24 hours and posts a digest
to Slack through a Slack Workflow Builder webhook.

Do the steps below in order.

## Rule

Never print, log, echo, or commit the webhook URL (`SLACK_WEBHOOK_URL`).
Do not write it to any file. Do not run `env` or `printenv` without a filter.

## Steps

### a. Search for news

Search the web for voice AI news from the last 24 hours.

Scope:
- New speech-to-text (STT), text-to-speech (TTS), speech-to-speech, and
  realtime voice models.
- Model updates and releases.
- Voice agent platforms and APIs.
- Major funding rounds or acquisitions.
- Important research papers.

Sources:
- Vendor blogs: OpenAI, Google, ElevenLabs, Deepgram, AssemblyAI, Cartesia,
  Anthropic, Meta, Microsoft, Sarvam AI.
- Hugging Face (models, blog, papers).
- arXiv (cs.CL, cs.SD, eess.AS).
- Hacker News.
- Tech news sites.

### b. Remove duplicates

Read `seen.md`. Skip any item already listed. Match by item name or by URL.

### c. Verify

Keep only items verified with a real source link that you opened.
Do not invent items or links. If you cannot confirm the date or the link,
drop the item.

### d. Write the digest

Write the digest to `/tmp/digest.txt`:

- First line: `Voice AI update – <date>`, for example
  `Voice AI update – 23 Sep 2026`. Use the IST date.
- Up to 8 items, most important first.
- One line per item: `• <name> – <one-line summary> <link>`
- If there are no new items, write this single line after the header:
  `No major voice AI updates today.`
- Plain text only. No Markdown tables.

Example:

```
Voice AI update – 23 Sep 2026
• Example TTS v2 – Lower-latency streaming TTS with 30 new voices https://example.com/blog/tts-v2
• Example STT – Open-weights STT model tops the Open ASR leaderboard https://huggingface.co/example/stt
```

### e. Post to Slack

Run:

```
python3 scripts/post_to_slack.py /tmp/digest.txt
```

Confirm that the script prints a 2xx status and exits with code 0.

### f. Update seen.md

Only after a successful post, append one line per posted item to the
end of `seen.md`:

```
- YYYY-MM-DD | <item name> | <source URL>
```

If the digest had no new items, do not change `seen.md`.

### g. Commit and push

Commit with the message `digest: <YYYY-MM-DD>` and push to `main`.
If `seen.md` did not change, skip the commit.

### h. On failure

If posting fails (missing env var, non-2xx status, or a network error):
- Do not change `seen.md`.
- Do not commit.
- Report the error and the HTTP status. Do not include the webhook URL.
