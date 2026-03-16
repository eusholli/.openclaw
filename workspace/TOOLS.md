# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Web Tools

### web_search
- **Provider:** Brave Search API (`BRAVE_API_KEY`)
- **Expected latency:** ~1–3s
- **Best for:** All B2B research queries — fast, structured results

### web_fetch
- **Provider:** Built-in HTTP + Firecrawl fallback (`FIRECRAWL_API_KEY`)
- **Expected latency:** ~2–5s
- **Best for:** Extracting content from a specific URL. Firecrawl auto-activates for JS-heavy pages.

## AI Event Planner Write Gateway

### [PENDING_ACTION] Pattern

Instead of direct HTTP calls (which are blocked from Docker), use the [PENDING_ACTION] text pattern. ws-proxy intercepts these blocks and routes confirmation through the browser UI.

**Format:**
```
[PENDING_ACTION id="<uuid>" tool="<toolName>" eventId="<slug>" args='<JSON>']
```

**Rules:**
- NEVER use `exec`, `curl`, `python`, `python3`, or `web_fetch` to call the event-planner API
- One [PENDING_ACTION] per message — stop and wait for human confirmation
- Generate a unique UUID v4 for each action's `id`
- Use `eventSlug` (not eventId UUID) from [ActionCtx] as the `eventId` in the block
- After emitting the block, tell the user you've proposed the action and are waiting for confirmation

**Available write tools:**

| tool | description | required args |
|------|-------------|---------------|
| `createMeeting` | Create a new meeting | `title, date (YYYY-MM-DD), startTime (HH:mm), endTime (HH:mm)` |
| `cancelMeeting` | Cancel a meeting | `meetingId` |
| `updateMeeting` | Update meeting fields | `meetingId` + any fields to change |
| `addAttendee` | Add attendee to event | `name, email, title, company` |
| `updateCompany` | Update company data | `companyId` + fields |
| `updateROITargets` | Update ROI targets | any target fields; `targetCompanyNames?: string[]` resolved/created by name |

**Example output when user asks to create a meeting:**
```
I'll create a "Q2 Pipeline Review" meeting on March 20 at 2:00–3:00 PM. Confirming this will add it to the event calendar.

[PENDING_ACTION id="a1b2c3d4-e5f6-4789-abcd-ef0123456789" tool="createMeeting" eventId="my-event-slug" args='{"title":"Q2 Pipeline Review","date":"2026-03-20","startTime":"14:00","endTime":"15:00"}']

I've proposed this action and am waiting for your confirmation in the chat.
```

**Read operations:** You cannot call read APIs directly. Describe what you would look up and ask the user to confirm what they see in the app, or navigate them to the relevant page.

## Examples

```markdown
### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.
