# 🚀 One-Prompt Method (For the Adventurous!)

**Don't want to clone repos or download scripts?** Just paste this prompt into Claude Code and let it build everything from scratch!

---

## How It Works

1. Open Claude Code in any directory
2. Copy the prompt below
3. Paste and run
4. Get your Wrapped summary!

Claude Code will:
- ✅ Analyze your `~/.claude/` directory
- ✅ Count your actual messages (not system events)
- ✅ Find your most active projects
- ✅ Calculate time patterns
- ✅ Generate shareable stats

---

## The Prompt

```
I want to create a "Spotify Wrapped" style summary of my Claude Code usage for 2025.

Please analyze my Claude Code data and create a comprehensive wrapped summary with:

1. **Core Metrics:**
   - How many messages I actually typed (not total events)
   - Number of conversations/sessions
   - Projects I worked on
   - Agents spawned
   - Time active (days)

2. **Fun Stats:**
   - My peak coding hours
   - Busiest day of week
   - Longest conversation (by my input)
   - Most active project
   - Early bird or night owl?
   - Hottest month
   - Coding personality profile

3. **Shareable Format:**
   - Create a markdown file with Spotify Wrapped-style reveals
   - Include social media snippets I can share
   - Make it visual and fun with emojis

**Data Sources:**
- Analyze `~/.claude/projects/` for session files (*.jsonl)
- Count messages where `type == "user"`
- Parse timestamps for time patterns
- Count agents (agent-*.jsonl files)
- Extract project names from directory structure

**Important:**
- Focus on MY messages (what I typed), not total message events
- Make metrics easy for non-technical people to understand
- Create both detailed and quick-share versions

**Output:**
- A comprehensive WRAPPED_2025.md file
- A shorter SUMMARY.md for quick sharing
- A SPOTIFY_WRAPPED.md with fun Spotify-style presentation

Please build the analysis scripts first, run them, then generate the wrapped summaries!
```

---

## What Claude Code Will Do

### Phase 1: Discovery
- Locate your `~/.claude/projects/` directory
- Find all `.jsonl` session files
- Identify agent files
- Extract project names

### Phase 2: Analysis
- Parse JSON data from sessions
- Count user messages (`type: "user"`)
- Extract timestamps
- Calculate statistics
- Identify patterns

### Phase 3: Generation
- Create detailed Wrapped summary
- Generate Spotify-style parody
- Build shareable snippets
- Add fun facts and insights

---

## Expected Output

You'll get 3 files:

### 1. WRAPPED_2025.md
**Comprehensive analysis** with:
- All metrics explained
- Project breakdowns
- Time patterns
- Personality insights
- 500+ lines of detailed stats

### 2. SUMMARY.md
**Quick shareable version** with:
- Top stats
- Best projects
- Fun facts
- Social media snippets

### 3. SPOTIFY_WRAPPED_2025.md
**Spotify parody** with:
- Big reveal style
- Emoji-heavy
- Personality profile
- "Theme song"
- Share templates

---

## Tips for Best Results

### Be Specific
Add project context if you want:
```
I mainly work on [type of projects].
Focus on sessions in: [Project1], [Project2], [Project3]
```

### Request Specific Metrics
```
Also calculate:
- Total words/characters I typed
- Average message length
- Longest single message
- Streak of consecutive days
```

### Ask for Comparisons
```
Compare my usage to typical Claude Code users.
Am I a power user? Light user? What percentile?
```

---

## Troubleshooting

**Claude says it can't find data?**
- Make sure you've actually used Claude Code before
- Verify `~/.claude/` directory exists
- Run `ls ~/.claude/projects/` to check for sessions

**Results look wrong?**
- Ask Claude to show you sample data it's finding
- Verify the JSON parsing is correct
- Request a breakdown by project to debug

**Want different metrics?**
- Just ask! Claude can calculate anything from the data
- Examples: "Also show me my most-used tools", "Which month had longest sessions?"

---

## Advanced Customization

### Add Custom Sections
```
Also include:
- My most common first messages
- Tools I used most (Read, Write, Bash, etc.)
- Average session duration
- Comparison between weekday vs weekend usage
```

### Focus on Specific Time Periods
```
Only analyze sessions from [MONTH] 2025 onwards
(when I started my [PROJECT_NAME] project)
```

### Export Formats
```
Also generate:
- A CSV file with raw stats for spreadsheet analysis
- A JSON file with all calculated metrics
- A one-page summary suitable for printing
```

---

## Why This Method Works

**Pros:**
- ✅ No repo cloning needed
- ✅ No script downloads
- ✅ Claude builds everything custom for you
- ✅ Fully interactive - ask follow-up questions
- ✅ Can customize on the fly

**Cons:**
- ⚠️ Takes longer (Claude builds from scratch)
- ⚠️ Results may vary slightly
- ⚠️ Requires understanding to debug issues

---

## Example Follow-Up Questions

After the initial analysis:

```
Can you also calculate:
- Which project had the most agents spawned?
- What time of day do I code most?
- Show me my usage trend over months

Create a version suitable for:
- LinkedIn post
- Twitter thread
- Showing to my students

Make it more fun:
- Add more emojis
- Create a "coding personality" quiz-style result
- Include funny comparisons (e.g., "typed the equivalent of X novels")
```

---

## Sample Enhanced Prompt

For even better results, try this expanded version:

```
Create a comprehensive "Spotify Wrapped 2025" analysis of my Claude Code usage.

**Analysis Requirements:**

1. Message Counting:
   - Count only messages where JSON `type == "user"`
   - Calculate total characters and words I typed
   - Find my longest single message
   - Average message length

2. Session Analysis:
   - Total sessions (exclude agent-*.jsonl files)
   - Average messages per session
   - Longest session by my input
   - Sessions per project

3. Time Patterns:
   - Parse timestamps to find peak hours
   - Busiest day of week
   - Most active month
   - Am I early bird (5am-12pm) or night owl (10pm-5am)?
   - Longest consecutive day streak

4. Project Insights:
   - List all projects with session counts
   - Top 3 by my message count
   - Which project used most agents?
   - Project-by-project breakdown

5. Advanced Metrics:
   - Agents spawned (count agent-*.jsonl files)
   - Tool usage patterns (if detectable from JSON)
   - Session duration estimates
   - Usage frequency (sessions per day)

**Output Format:**

Create 3 markdown files:

1. WRAPPED_2025.md - Detailed analysis (like the full repo version)
2. SPOTIFY_WRAPPED_2025.md - Fun Spotify parody with big reveals
3. SUMMARY.md - One-page shareable version

Include:
- Visual ASCII charts where helpful
- Emojis for personality
- Social media share templates (Twitter, LinkedIn)
- Comparisons to average users
- Fun facts and superlatives

**Technical Approach:**

1. First, examine the structure of one .jsonl file to understand the format
2. Build a Python script to parse all sessions
3. Calculate all metrics
4. Generate the markdown reports
5. Show me the key findings

Please start by exploring my ~/.claude/projects/ directory and showing me what you find!
```

---

## Next Steps

1. **Try the basic prompt** - See what Claude Code creates
2. **Review the output** - Check if stats look right
3. **Ask for refinements** - "Make it more fun", "Add more metrics", etc.
4. **Save your favorites** - Keep the markdown files Claude generates

---

**Pro Tip:** You can use this method to analyze just specific projects, specific time periods, or generate completely custom metrics. Just modify the prompt!

---

**Remember:** This is the adventurous path! If you want guaranteed consistent results, use the scripts from the main repo. If you want to explore and customize, this prompt method is perfect!

🎵 Happy Wrapping! 🎵
