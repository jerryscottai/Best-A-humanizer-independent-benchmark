# BytePlus (ModelArk) Seedance 2.5: setup and next steps

## Status (2026-10-13)
- Direct BytePlus replaces fal for presenter clips (cheaper). Key works in a NEW session: GET https://ark.ap-southeast.bytepluses.com/api/v3/models returned 200.
- Video model ID: `dreamina-seedance-2-5-260628`.
- Do NOT look for the key in env vars or files, and never ask the user to paste it. It is attached to requests for ark.ap-southeast.bytepluses.com. Call the API with no auth header, unless the session reports a BYTEPLUS_API_KEY variable, then use `Authorization: Bearer $BYTEPLUS_API_KEY` and never print it.
- Old sessions (started before the key was saved) return 401 and won't pick it up.

## Price (secondhand, verify on the account)
- BytePlus lists ~$10.70 per 1M tokens (no video input), vs fal ~$21.40 per 1M.
- tokens ≈ H x W x FPS x duration / 1024. 16s 720p 24fps ≈ 345k tokens ≈ $3.70 (fal was ~$7.40).
- ModelArk page advertises "Draft Mode": cheap 480p preview, then upgrade to final with consistent content. Unverified: price, and whether it works with reference audio.

## Before any paid generation
1. Read the Create-video-generation-task docs (docs.byteplus.com) for the real request fields: reference audio support, duration type, resolution, how to poll a task. Do not guess fields.
2. State the estimated cost to the user and wait for a yes.
3. Run each generation ONCE. Never re-run to retry.
4. Real-person/face rejection behaviour on BytePlus is unknown. Describe the presenter in words; no face reference images/videos.

## First test (needs user OK)
Re-create the 16s student presenter clip: one combined clip (hook line, ~2s beat, closing line) with two reference audios (ElevenLabs signed URLs, Jalisa voice 1DC6VAfJKAscIyFOOTRa, eleven_v4). Record the real cost from the account and compare quality with the fal clip.

## Other saved assets
- Project docs: claude/short-video-builder/student-v2/* and WORKFLOW.md.
- Music library (cloud): artifact https://claude.ai/artifact/NpibdkZ1LVXwKXSwAfC9Ln (bed-A, bed-B).
