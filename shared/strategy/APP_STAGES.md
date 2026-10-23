# App Stages

Durable status file for all Tiny Toolshed apps.  
**黑媽媽** and other bots should read this file to know the current stage of each app.

Last updated: 2026-10-23

## Stage Definitions

| Stage | Name | Description | Owner / When user is notified |
|-------|------|-------------|-------------------------------|
| 1 | Ideation / Validation | Idea generation. Marketing Master evaluates market, ASO, competitors, and feasibility. | User decides; Marketing Master advises |
| 2 | Development (pre-build) | Coding in progress. No testable build yet. | Hands-off. Notify only when ready for Stage 3 |
| 3 | TestFlight ready | Built and available on TestFlight for internal testing. Not yet submitted to App Store. | Notify user as soon as build is ready |
| 4 | Submitted to App Store | Submitted for review (or waiting for approval). Not yet live. | Notify user of review result (approved / rejected) |
| 5 | Live + Growth | Live on App Store. Marketing is active. Regular builds based on user feedback. | User approves Marketing Master’s weekly suggestion list before changes |

**Notes**
- Stage 2 and Stage 3 are fully hands-off for the user. Notify only when a build is ready.
- Rejection stays in Stage 4 until fixed and resubmitted.
- app1 and app2 are archived / ignored. Do not track or work on them.

## Post-Change Workflow (Stages 2–5)

1. 可憐的碼農 finishes changes
2. → 漏洞大師 scans for secrets / issues → fix until clean
3. → 胖嘟嘟阿姨 tests → issues go back to 可憐的碼農
4. → 黑媽媽 + user confirm
5. → 蘋果大師 builds / submits

## Weekly Feedback Loop (Stage 5 and late Stage 4)

- 小編們 continue weekly learning schedule
- 行銷大師 weekly summarizes community replies → suggestion list
- User reviews and approves the list
- 可憐的碼農 implements → follow the Post-Change Workflow above

## Current App Status

| App | Folder | Name | Current Stage | Notes |
|-----|--------|------|---------------|-------|
| app1 | `app1/` | (諧音猜猜) | **Ignored** | Do not track or work on |
| app2 | `app2/` | (急廁 Go) | **Ignored** | Do not track or work on |
| app3 | `app3/` | Been Ages / 好久沒了 | **4** | Submitted to App Store, not yet live / marketing |
| app4 | `app4/` | Decibel Meter | **4** | Submitted to App Store, not yet live / marketing |

## How to Update This File

- Only SuperGrok (or user) updates the stage table and notes.
- After any stage change, update the table and the “Last updated” date.
- Push directly to `main` (no PR needed for this documentation file).
