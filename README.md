# static-site-generator

# Motivation

I don't like Jekyll :P

(Maybe it would be interesting to build a markdown interpreter?)

# Overview

Takes .md files from `_posts/` folder, converts them to .html files, and then writes the output to `docs/` folder.

Why these folder names? `_posts/` is used by Jekyll as the input, and `docs/` is used by GitHub Pages for hosting.

# Supported features

- Headers

# TODO/Reminders

## Markdown features

- Bullets
- Code blocks
- Links

## Rust

Rewrite in rust to practice??

## Optimization

- Necessary optimization: if the generated file is newer than the source file, don't do anything

## multiple files

- Have an input and output folder for multiple files

## Options file

- Allow changing of input and output folder
