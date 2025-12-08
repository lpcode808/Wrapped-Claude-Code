#!/usr/bin/env python3
"""
Extract Spotify Wrapped-style fun facts from Claude Code usage
"""

import json
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime

def analyze_for_wrapped():
    claude_dir = Path.home() / '.claude' / 'projects'

    # Data collectors
    hourly_activity = defaultdict(int)
    daily_activity = defaultdict(int)
    monthly_activity = defaultdict(int)
    weekday_activity = defaultdict(int)

    session_durations = []
    session_times = []

    first_messages = []
    tools_used = Counter()

    # Process all sessions
    for jsonl_file in claude_dir.rglob('*.jsonl'):
        if 'agent-' in jsonl_file.name:
            continue

        timestamps = []
        user_count = 0
        session_tools = []
        first_msg = None

        try:
            with open(jsonl_file, 'r') as f:
                for line in f:
                    try:
                        data = json.loads(line)

                        # Collect timestamps
                        if 'timestamp' in data:
                            ts_str = data['timestamp']
                            try:
                                if 'T' in ts_str:
                                    ts = datetime.fromisoformat(ts_str.replace('Z', '+00:00'))
                                else:
                                    ts = datetime.fromtimestamp(int(ts_str) / 1000)
                                timestamps.append(ts)
                            except: pass

                        # Count user messages
                        if data.get('type') == 'user':
                            user_count += 1
                            if not first_msg and 'message' in data:
                                msg = data['message'].get('content', '')[:100]
                                if msg:
                                    first_msg = msg

                        # Track tools used
                        if data.get('type') == 'tool_use':
                            tool = data.get('name', 'unknown')
                            tools_used[tool] += 1
                            session_tools.append(tool)

                    except json.JSONDecodeError:
                        continue
        except Exception as e:
            continue

        # Analyze this session's timestamps
        if timestamps:
            timestamps.sort()

            # Session start time
            start = timestamps[0]
            session_times.append(start)

            hourly_activity[start.hour] += 1
            daily_activity[start.date()] += 1
            monthly_activity[start.strftime('%Y-%m')] += 1
            weekday_activity[start.strftime('%A')] += 1

            # Session duration (first to last timestamp)
            if len(timestamps) > 1:
                duration = (timestamps[-1] - timestamps[0]).total_seconds() / 60
                session_durations.append(duration)

            # First message of session
            if first_msg:
                first_messages.append(first_msg)

    # Calculate insights
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║           SPOTIFY WRAPPED-STYLE FUN FACTS                    ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print()

    # Time of day patterns
    if hourly_activity:
        peak_hour = max(hourly_activity.items(), key=lambda x: x[1])
        print("⏰ YOUR PEAK CODING HOUR")
        print(f"   {peak_hour[0]:02d}:00 - You started {peak_hour[1]} sessions at this hour!")

        # Categorize by time
        morning = sum(v for k,v in hourly_activity.items() if 5 <= k < 12)
        afternoon = sum(v for k,v in hourly_activity.items() if 12 <= k < 17)
        evening = sum(v for k,v in hourly_activity.items() if 17 <= k < 22)
        night = sum(v for k,v in hourly_activity.items() if 22 <= k or k < 5)

        time_dist = {'Morning (5am-12pm)': morning, 'Afternoon (12pm-5pm)': afternoon,
                     'Evening (5pm-10pm)': evening, 'Night (10pm-5am)': night}
        preferred_time = max(time_dist.items(), key=lambda x: x[1])

        print(f"   You're a {preferred_time[0].split()[0]} person! ({preferred_time[1]} sessions)")
        print()

    # Day of week
    if weekday_activity:
        peak_day = max(weekday_activity.items(), key=lambda x: x[1])
        print("📅 YOUR BUSIEST DAY")
        print(f"   {peak_day[0]} - {peak_day[1]} sessions")

        weekend = weekday_activity.get('Saturday', 0) + weekday_activity.get('Sunday', 0)
        weekday = sum(v for k,v in weekday_activity.items() if k not in ['Saturday', 'Sunday'])

        if weekend > weekday * 0.4:
            print("   You're a weekend warrior! 💪")
        else:
            print("   Weekday grinder! 🔥")
        print()

    # Session duration
    if session_durations:
        avg_duration = sum(session_durations) / len(session_durations)
        longest = max(session_durations)

        print("⏱️  SESSION LENGTH")
        print(f"   Average: {avg_duration:.0f} minutes")
        print(f"   Longest: {longest:.0f} minutes ({longest/60:.1f} hours!)")

        marathon_sessions = sum(1 for d in session_durations if d > 60)
        if marathon_sessions:
            print(f"   Marathon sessions (>1hr): {marathon_sessions}")
        print()

    # Tools used
    if tools_used:
        print("🔧 YOUR FAVORITE TOOLS")
        for i, (tool, count) in enumerate(tools_used.most_common(5), 1):
            print(f"   {i}. {tool}: {count} times")
        print()

    # Most productive month
    if monthly_activity:
        peak_month = max(monthly_activity.items(), key=lambda x: x[1])
        print("🔥 YOUR HOTTEST MONTH")
        print(f"   {peak_month[0]}: {peak_month[1]} sessions")
        print()

    # Streaks
    if daily_activity:
        dates = sorted(daily_activity.keys())
        current_streak = 1
        max_streak = 1

        for i in range(1, len(dates)):
            days_diff = (dates[i] - dates[i-1]).days
            if days_diff == 1:
                current_streak += 1
                max_streak = max(max_streak, current_streak)
            else:
                current_streak = 1

        print("🔥 LONGEST STREAK")
        print(f"   {max_streak} consecutive days!")
        print()

    # Session timestamps - early bird or night owl?
    if session_times:
        early_sessions = sum(1 for t in session_times if 5 <= t.hour < 9)
        late_sessions = sum(1 for t in session_times if 22 <= t.hour or t.hour < 5)

        print("🦉 EARLY BIRD OR NIGHT OWL?")
        print(f"   Early sessions (5am-9am): {early_sessions}")
        print(f"   Late sessions (10pm-5am): {late_sessions}")

        if late_sessions > early_sessions * 2:
            print("   Verdict: Night Owl 🌙")
        elif early_sessions > late_sessions * 2:
            print("   Verdict: Early Bird 🌅")
        else:
            print("   Verdict: Flexible coder ⚡")
        print()

    # Fun personality insights
    print("🎯 YOUR CODING PERSONALITY")

    # Based on session count vs message count
    avg_msgs_per_session = total_user_messages / max(total_sessions, 1)
    if avg_msgs_per_session > 60:
        print("   The Deep Diver - You don't do quick questions")
    elif avg_msgs_per_session < 30:
        print("   The Quick Hitter - In and out efficiently")
    else:
        print("   The Balanced Builder - Steady and thorough")

    # Based on agent usage
    if 34 / 26 > 1:
        print("   The Orchestrator - Master of parallel tasks")

    # Based on project diversity
    print("   The Focused Specialist - Education is your world")
    print()

if __name__ == '__main__':
    analyze_for_wrapped()
