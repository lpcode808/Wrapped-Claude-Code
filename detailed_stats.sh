#!/bin/bash

echo "=== DETAILED PROJECT ANALYSIS ==="
echo ""

for project in */; do
    project=${project%/}  # Remove trailing slash
  dir=$(find ~/.claude/projects -type d -name "*$project" 2>/dev/null | head -1)
  if [ -n "$dir" ]; then
    sessions=$(find "$dir" -name "*.jsonl" ! -name "agent-*.jsonl" 2>/dev/null | wc -l | tr -d ' ')
    agents=$(find "$dir" -name "agent-*.jsonl" 2>/dev/null | wc -l | tr -d ' ')
    total_msgs=$(find "$dir" -name "*.jsonl" -exec cat {} \; 2>/dev/null | wc -l | tr -d ' ')

    echo "📁 $project"
    echo "   Sessions: $sessions"
    echo "   Agents: $agents"
    echo "   Total messages: $total_msgs"

    # Get longest conversation
    longest=$(find "$dir" -name "*.jsonl" ! -name "agent-*.jsonl" -exec wc -l {} \; 2>/dev/null | sort -rn | head -1 | awk '{print $1}')
    if [ -n "$longest" ] && [ "$longest" != "0" ]; then
      echo "   Longest conversation: $longest messages"
    fi
    echo ""
  fi
done
