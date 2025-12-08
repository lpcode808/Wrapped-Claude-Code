#!/usr/bin/env python3
"""
Count actual user inputs (what YOU typed) vs total messages.
This gives non-technical users a clearer understanding of engagement.
"""

import json
import os
from pathlib import Path
from collections import defaultdict

def count_messages_in_file(filepath):
    """Count user inputs and total messages in a JSONL conversation file."""
    user_messages = 0
    assistant_messages = 0
    tool_uses = 0
    total_lines = 0

    try:
        with open(filepath, 'r') as f:
            for line in f:
                total_lines += 1
                try:
                    data = json.loads(line)
                    msg_type = data.get('type', '')

                    if msg_type == 'user':
                        user_messages += 1
                    elif msg_type == 'message' and data.get('message', {}).get('role') == 'assistant':
                        assistant_messages += 1
                    elif msg_type == 'tool_use':
                        tool_uses += 1

                except json.JSONDecodeError:
                    continue
    except Exception as e:
        pass

    return {
        'user': user_messages,
        'assistant': assistant_messages,
        'tools': tool_uses,
        'total': total_lines
    }

def main():
    claude_dir = Path.home() / '.claude' / 'projects'

    if not claude_dir.exists():
        print("❌ Claude Code projects directory not found")
        return

    # Stats collection
    total_stats = {'user': 0, 'assistant': 0, 'tools': 0, 'total': 0}
    session_details = []
    project_stats = defaultdict(lambda: {'user': 0, 'assistant': 0, 'tools': 0, 'sessions': 0})

    # Process all conversation files (exclude agents)
    for jsonl_file in claude_dir.rglob('*.jsonl'):
        if 'agent-' in jsonl_file.name:
            continue

        stats = count_messages_in_file(jsonl_file)

        if stats['total'] > 0:
            # Accumulate totals
            for key in ['user', 'assistant', 'tools', 'total']:
                total_stats[key] += stats[key]

            # Extract project name
            project = jsonl_file.parent.name.replace('-Users-justinlai-Coding-', '')
            if project == '-Users-justinlai-Coding':
                project = 'Coding (root)'

            project_stats[project]['user'] += stats['user']
            project_stats[project]['assistant'] += stats['assistant']
            project_stats[project]['tools'] += stats['tools']
            project_stats[project]['sessions'] += 1

            session_details.append({
                'project': project,
                **stats
            })

    # Print results
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║       USER INPUT ANALYSIS (What YOU Actually Typed)         ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print()

    num_sessions = len(session_details)
    avg_user = total_stats['user'] / num_sessions if num_sessions > 0 else 0
    multiplier = total_stats['total'] / total_stats['user'] if total_stats['user'] > 0 else 0

    print(f"✍️  You typed:                        {total_stats['user']} messages")
    print(f"🤖 Claude responded:                  {total_stats['assistant']} messages")
    print(f"🔧 Tools used:                        {total_stats['tools']} tool calls")
    print(f"📊 Total message exchanges:           {total_stats['total']} lines")
    print(f"💬 Across {num_sessions} conversations")
    print()
    print(f"📈 Your input multiplier:             {multiplier:.1f}x")
    print(f"   (Each message you type generates {multiplier:.1f} total exchanges)")
    print(f"📊 Average per conversation:          {avg_user:.1f} messages from you")
    print()

    print("═══ Your Most Active Conversations (By Your Input) ═══")
    print()

    for i, session in enumerate(sorted(session_details, key=lambda x: x['user'], reverse=True)[:10], 1):
        emoji = "🔥" if session['user'] > 30 else "💬" if session['user'] > 15 else "✉️"
        print(f"{i:2}. {emoji} {session['user']:3} messages - {session['project']}")
        print(f"      Claude: {session['assistant']} responses | Tools: {session['tools']} calls")

    print()
    print("═══ By Project ═══")
    print()

    for project, stats in sorted(project_stats.items(), key=lambda x: x[1]['user'], reverse=True):
        if stats['user'] > 0:
            avg_per_session = stats['user'] / stats['sessions']
            print(f"📁 {project}")
            print(f"   You typed: {stats['user']} messages ({stats['sessions']} sessions, {avg_per_session:.1f} avg)")
            print()

    print("═══ What This Means ═══")
    print()
    print("✅ USER MESSAGES: What you actually typed to Claude")
    print("✅ CLAUDE RESPONSES: Claude's direct answers to you")
    print("✅ TOOL CALLS: Claude using tools (Read, Write, Bash, etc.)")
    print()
    print(f"The {total_stats['total']} total 'messages' in the data includes EVERYTHING:")
    print(f"  • Your {total_stats['user']} inputs")
    print(f"  • Claude's {total_stats['assistant']} responses")
    print(f"  • {total_stats['tools']} tool operations")
    print(f"  • Plus system messages, snapshots, metadata")
    print()
    print("🎯 FOR NON-TECHNICAL FOLKS:")
    print(f'  "I had {total_stats['user']} back-and-forth exchanges with Claude"')
    print(f"  is clearer than")
    print(f'  "There were {total_stats['total']} total message events"')

if __name__ == '__main__':
    main()
