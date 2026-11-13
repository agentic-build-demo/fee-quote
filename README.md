# fee-quote

A small Python library and command line tool that quotes the fee for an amount and a customer tier.

This repository exists to show an agentic build process from start to end, in public. Every step is a real GitHub object you can open.

## The process

| Step | Who acts | Where to see it |
|---|---|---|
| Proposal | Human or agent | The proposal in [Discussions](../../discussions) |
| PBI issue | Agent drafts, human steers | The PBI (product backlog item) issue, with the criteria and the task table |
| PBI agreed | Human | The `agreed` label on the PBI issue. It starts the tasks. |
| Implement | Human or agent | One task issue, one plan comment, one branch, one pull request |
| Independent review | Agent | A PASS or FAIL comment on each pull request, from a reviewer that did not build it. Up to 5 rounds. |
| Human merges | Human | The merge of each pull request |
| Release | Human or agent | The tag and the release notes |

Rules for every task:

- No code without an agreed task issue.
- The builder comments a plan on the task issue before any code.
- Each changed file serves a numbered acceptance criterion of the PBI.
- The reviewer runs every criterion's check and writes PASS or FAIL. It never fixes and never merges.
- After a fifth FAIL, the task goes back to a human, or back to its plan and definition.

## Status

Under construction, one task at a time. See the PBI issue for the current state.
