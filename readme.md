# ShellMate: The AI-Powered CLI Assistant
## Hey Devs, Here's Something You'll Love!

Let's be real - we've all been there. Staring at the terminal, trying to remember that one Linux command. It doesn't matter if you're just starting out or if you've been in the game for years; sometimes those commands just slip your mind. And sure, you could open a browser, search through stacks of docs, but isn't that just... tedious? That's where ShellMate jumps in!

## The Real Problem? Our Forgetful Brains!

We're software developers. We write elegant code, tackle complex algorithms, and create amazing apps. But remembering every single command and its syntax? That's asking a bit much. Who hasn't forgotten a command or two, right? So, instead of losing time Googling or scrolling through manuals, why not have a quick, in-terminal helper? Enter ShellMate - your CLI's new best friend!


## Key Features
- AI-Powered Explanations: Understand any command in plain English with a simple query.
- All Platforms Welcome: Whether you're on Linux, Windows, or MacOS, it's got your back.
- Find Commands Fast: Describe what you want to do, and ShellMate will find the command for you.
- Stay in the Zone: All of this happens within your beloved terminal. No more context switching!
## How to Install

```bash
pip install shellmate
```

That's it! No complex setups, just a simple pip command.

# How to Use ShellMate

## Setting your API key
```bash
shellmate set_api_key <YOU_OPENAI_API_KEY_HERE>
```
And even if you forget to this and just start running commands, you will first be asked to enter your apikey. You can also change your api key with this command.

## Need a Command Reminder?
```bash
shellmate explain "ls -l" -os linux
```
## Looking for the Right Command?

```bash
shellmate find "how to see disk usage" -os windows
```
## Examples
```python
# Forgot how to list files in detail on Linux?
shellmate explain "ls -l" -os linux

# Need to check disk usage on Windows but can't remember how?
shellmate find "how to see disk usage" -os windows
```

## Join the Forgetful Devs Club!
We're all in this together - a community of brilliant minds who sometimes forget the basics. ShellMate isn't just a tool; it's our little helper in those "Oops, I forgot again" moments. So, embrace it, use it, and keep coding without those pesky interruptions!
