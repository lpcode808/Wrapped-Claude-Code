#!/bin/bash

echo "=== REAL CLAUDE CODE USAGE: CONVERSATIONS ===="
echo ""

total_sessions=$(find ~/.claude/projects -name "*.jsonl" ! -name "agent-*.jsonl" | wc -l | tr -d ' ')
agent_sessions=$(find ~/.claude/projects -name "agent-*.jsonl" | wc -l | tr -d ' ')

echo "Main Conversations: $total_sessions"
echo "Agent Sub-tasks: $agent_sessions"
echo "Total Session Files: $((total_sessions + agent_sessions))"
echo ""
echo "=== Breakdown by Project ==="
echo ""

find ~/.claude/projects -type d -mindepth 1 -maxdepth 1 | while read dir; do
  project=$(basename "$dir" | sed 's/-Users-justinlai-Coding-//' | sed 's/-Users-justinlai-Coding$/Coding (root)/')
  sessions=$(find "$dir" -name "*.jsonl" ! -name "agent-*.jsonl" | wc -l | tr -d ' ')
  agents=$(find "$dir" -name "agent-*.jsonl" | wc -l | tr -d ' ')
  total=$((sessions + agents))

  if [ "$total" -gt 0 ]; then
    echo "$project|$sessions|$agents"
  fi
done | sort -t'|' -k2 -rn | awk -F'|' '{printf "%-40s %15s %10s\n", $1, $2, $3}'

echo ""
echo "=== Top 5 Longest Conversations ==="
echo ""

find ~/.claude/projects -name "*.jsonl" ! -name "agent-*.jsonl" -type f -exec wc -l {} + | sort -rn | head -6 | while read count file; do
  if [ "$file" != "total" ]; then
    project=$(echo "$file" | sed 's|.*/projects/-Users-justinlai-Coding-||' | sed 's|/.*||')
    echo "$count messages in $project"
  fi
done
