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

## Webapp Action Tool (AI Event Planner)

### webapp_action

This tool lets you perform CRUD operations on the AI Event Planner database. An `[ActionCtx]` block will appear at the end of user messages when event context is available.

**How to parse [ActionCtx]:**
The `[ActionCtx]` block looks like:
```
[ActionCtx appUrl="https://..." token="<action_token>" eventId="<uuid_or_slug>" eventSlug="<slug>" role="admin"]
```
Extract these fields at the start of each message and store them for use in tool calls.

**HTTP Request:**
- Method: `POST`
- URL: `{appUrl}/api/intelligence/actions`
- Headers: `Authorization: Bearer {token}`, `Content-Type: application/json`
- Body: `{ "tool": "<tool_name>", "eventId": "<eventId>", "args": { ... } }`
- Response: `{ "result": { ... } }`

**Available tools:**

| tool | description | args |
|------|-------------|------|
| `listEvents` | Search all accessible events — use when eventId is missing | `{ search? }` — **no eventId needed in request** |
| `getMeetings` | List meetings with filters | `{ date?, roomId?, search?, statuses?, tags?, meetingTypes?, attendeeIds?, isApproved?, calendarInviteSent? }` |
| `createMeeting` | Create a new meeting | `{ title, date (YYYY-MM-DD), startTime (HH:mm), endTime (HH:mm), purpose?, roomId?, attendeeEmails? }` |
| `cancelMeeting` | Cancel a meeting | `{ meetingId }` |
| `getAttendees` | List attendees with filters | `{ search?, company?, title?, types?, isExternal?, email? }` |
| `addAttendee` | Add/connect an attendee to the event | `{ name, email, title, company }` |
| `getRooms` | List rooms | `{ search?, minCapacity?, maxCapacity? }` |
| `getRoomAvailability` | Check room availability | `{ roomId, date, startTime, endTime }` |
| `getROITargets` | Get ROI targets and actuals | `{}` |
| `updateROITargets` | Update ROI targets | `{ expectedPipeline?, winRate?, expectedRevenue?, targetCustomerMeetings?, budget? }` |
| `getEvent` | Get event details | `{}` |
| `getNavigationLinks` | Get UI navigation URLs | `{ resource: "meeting"/"attendee", action: "create"/"read"/"update", id? }` |

**Roles and permissions:**
- `root`, `admin`, `marketing`: can read and write
- `user`: read-only (write operations will return 403)

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
