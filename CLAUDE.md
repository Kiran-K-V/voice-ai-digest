# Voice AI digest routine

You run as an unattended Claude Code cloud routine every day at 09:00 IST.
Your job: find every significant voice AI development since the last digest,
verify each one, and post a short digest to Slack. Readers are engineers who
build voice agents. They want to know what shipped, what changed, and what
they can use. Missing a major release is worse than posting a short digest.
Posting an invented or wrong item is worst of all.

Do the steps below in order. Do not skip a step.

## Hard rules

1. Never print, log, echo, or commit the webhook URL (`SLACK_WEBHOOK_URL`).
   Do not write it to any file. Do not run `env`, `printenv`, or `set`
   without a filter.
2. Never invent an item, a detail, or a link. Every item must come from a
   page you opened in this run.
3. If the Slack post fails, do not change `seen.md` and do not commit.

## Step 1: Sync and set the time window

1. Run `git pull --rebase origin main`.
2. Get today's date in IST: `TZ=Asia/Kolkata date +%F`.
3. Read `seen.md`. Find the most recent entry date.
4. Set the time window start:
   - Default: 24 hours before now.
   - If the most recent entry is older than yesterday, start at 09:00 IST
     on that entry's date. This covers days when a run failed.
   - Never go back more than 72 hours. If `seen.md` has no entries,
     use 72 hours.
   The window ends now. The duplicate check in Step 3 removes overlap.

## Step 2: Search

Search broadly. Run many searches (at least 15). Do not stop after the first
few results. Use several phrasings per topic, and add the current month and
year to queries to get fresh results.

### Topics in scope

- Models: new or updated speech-to-text (STT/ASR), text-to-speech (TTS),
  speech-to-speech, realtime voice, voice cloning, speech translation,
  audio language models, and voice activity or turn detection models.
  Include open-weights releases and new versions of existing models.
- APIs and pricing: new voice APIs, new endpoints, major price cuts,
  new languages, latency improvements, general availability (GA) launches.
- Voice agent platforms and frameworks: new features, major releases,
  new integrations, deprecations.
- Telephony and infrastructure for voice agents: SIP, WebRTC, phone
  numbers, call handling, if the change matters to voice agent builders.
- Benchmarks and leaderboards: new results that change rankings
  (for example the Hugging Face Open ASR Leaderboard, TTS Arena).
- Funding rounds (about USD 10M or more), acquisitions, and shutdowns of
  voice AI companies.
- Research papers with a clear new result (new SOTA, new architecture,
  new open dataset or model).
- Regulation or policy that directly affects voice AI (for example rules
  on voice cloning or AI phone calls).

### Companies and projects to check

Check each group. For vendors with a blog, changelog, or GitHub repo,
look at it directly, not only through news search.

- Frontier labs: OpenAI (Realtime API, audio models), Google (Gemini Live,
  Gemini TTS, Chirp), Anthropic (voice mode), Meta (Seamless, MMS),
  Microsoft (Azure Speech, VibeVoice), Amazon (Nova Sonic, Polly,
  Transcribe), Apple, NVIDIA (Parakeet, Canary, Riva), xAI (Grok voice),
  Mistral (Voxtral).
- Voice model vendors: ElevenLabs, Deepgram, AssemblyAI, Cartesia,
  Speechmatics, Gladia, Soniox, Rev, Hume AI, Rime, PlayAI, Resemble AI,
  Fish Audio, Kyutai, Sesame, Inworld, Smallest.ai, Murf, WellSaid.
- Voice agent platforms and frameworks: LiveKit (Agents framework, Cloud,
  turn detector), Pipecat and Daily, Vapi, Retell AI, Bland AI, Synthflow,
  Ultravox, Vocode, Twilio (ConversationRelay, Voice), Telnyx, Agora,
  Sierra, Decagon, PolyAI, Parloa.
- China and Asia: Alibaba Qwen (Qwen-Audio, Qwen-TTS), ByteDance
  (Seed speech models), StepFun, MiniMax (speech models), Moonshot (Kimi-Audio).
- India: Sarvam AI, AI4Bharat, Krutrim, Gnani.ai, Smallest.ai.
- Open source: Hugging Face (new trending audio models, blog), GitHub
  releases of whisper, faster-whisper, Coqui/XTTS forks, Kokoro, F5-TTS,
  Chatterbox, Dia, Orpheus, CSM, Moshi.

For framework repos (LiveKit Agents, Pipecat), report only releases with new
features or breaking changes. Skip patch releases that only fix bugs.

### Sources

- Vendor blogs, changelogs, docs release notes, and GitHub releases.
- Hugging Face: models sorted by trending (audio tasks), blog, daily papers.
- arXiv: cs.CL, cs.SD, eess.AS (new submissions in the window).
- Hacker News (search "voice", "speech", "TTS", "STT", "realtime").
- Tech news: TechCrunch, The Verge, VentureBeat, The Decoder,
  MarkTechPost, Inc42 and YourStory (for India).
- X/Twitter and LinkedIn posts from official company accounts, if a
  search result shows them.

### Example queries

Adapt these. Replace <Month YYYY> with the current month and year.

- `new text-to-speech model <Month YYYY>`
- `speech-to-text model release <Month YYYY>`
- `realtime voice API launch`
- `voice agent platform funding <Month YYYY>`
- `LiveKit agents release` / `Pipecat release`
- `<vendor> announces` for each major vendor above
- `open source TTS model Hugging Face`
- `arxiv speech language model` / `arxiv text-to-speech`

## Step 3: Filter

Remove an item if any of these is true:

- It is already in `seen.md`. Match by URL, by item name, or by the same
  underlying announcement under a different URL or name. A follow-up on a
  seen item is allowed only if it adds a real new fact (for example GA after
  preview, open weights after API-only, new pricing).
- Its publish date is outside the time window.
- It is out of scope: consumer gadgets or apps that only add a voice feature,
  opinion pieces, listicles, tutorials, webinars, hiring news, minor partner
  announcements, rumors, or small bug-fix releases.
- Two or more results describe the same announcement. Keep one item and use
  the primary source.

## Step 4: Verify

For each remaining item:

1. Open the link. Confirm the page loads and describes the item.
2. Confirm the publish date is inside the time window.
3. Prefer the primary source (vendor blog, release notes, GitHub release,
   arXiv abstract page) over news coverage. Use news coverage only when no
   primary source exists, for example for funding rounds.
4. Take facts for the summary (model name, numbers, languages, price) from
   the page. Do not guess numbers.

If you cannot confirm the page or the date, drop the item.

## Step 5: Rank

Order items by importance to voice agent builders:

1. New models or major versions from major vendors, and GA launches.
2. Open-weights models that reach or beat the state of the art.
3. Major platform and framework releases (for example LiveKit, Pipecat, Vapi).
4. Big pricing, latency, or language coverage changes.
5. Funding and acquisitions.
6. Research papers and benchmarks.

Keep the top 8. If more than 8 items qualify, drop the least important.

## Step 6: Write the digest

Write the digest to `/tmp/digest.txt`:

- First line: `Voice AI update – <date>`, for example
  `Voice AI update – 23 Sep 2026`. Use the IST date.
- Then up to 8 lines, one per item, most important first:
  `• <name> – <one-line summary> <link>`
- `<name>`: the product or model name and the company, for example
  `Deepgram Nova-4`.
- `<one-line summary>`: at most 25 words. Say what is new and why it matters,
  with one concrete fact (a number, a language count, a price, a benchmark).
  No hype words ("revolutionary", "game-changing").
- `<link>`: the verified source URL, bare, at the end of the line.
- If there are no new items, write this single line after the header:
  `No major voice AI updates today.`
- Plain text only. No Markdown headings, bold, tables, or link syntax.

Example:

```
Voice AI update – 23 Sep 2026
• Example TTS v2 – Streaming TTS with 120 ms first-byte latency and 30 new voices https://example.com/blog/tts-v2
• Example STT – Open-weights STT model with 5.1% WER, now first on the Open ASR Leaderboard https://huggingface.co/example/stt
```

Before you post, check the file:
- Every line after the header starts with `• ` and ends with a URL.
- Every URL was opened and verified in this run.
- No item is in `seen.md`.
- No more than 8 items.

## Step 7: Post to Slack

Run:

```
python3 scripts/post_to_slack.py /tmp/digest.txt
```

Confirm that the script prints a 2xx status and exits with code 0.
If it fails, go to "On failure". Do not retry more than once.

## Step 8: Update seen.md

Only after a successful post, append one line per posted item to the
end of `seen.md`:

```
- YYYY-MM-DD | <item name> | <source URL>
```

Use today's IST date and the same name and URL as in the digest.
If the digest had no new items, do not change `seen.md`.

## Step 9: Commit and push

If `seen.md` changed:

1. `git add seen.md`
2. `git commit -m "digest: <YYYY-MM-DD>"`
3. `git pull --rebase origin main`, then `git push origin main`.

If `seen.md` did not change, skip the commit.

## On failure

If posting fails (missing env var, non-2xx status, or a network error):

- Do not change `seen.md`.
- Do not commit.
- Report the error message and the HTTP status. Do not include the
  webhook URL.

## Final report

End the run with a short report: the time window used, the number of
searches run, the number of candidates found, the number posted, and the
items dropped with the reason (duplicate, out of window, unverified,
out of scope).
