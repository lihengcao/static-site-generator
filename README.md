# static-site-generator

## Motivation

I don't like Jekyll :P

I initially wanted to write a very very simple markdown interpreter, but decided against that. Going in the backlog.

## Overview

Takes .md files from `_posts/` folder, converts them to .html files, and then writes the output to `docs/` folder.

Why these folder names? `_posts/` is used by Jekyll as the input, and `docs/` is used by GitHub Pages for hosting.

## TODO/Reminders/Backlog

### Rust

Rewrite in rust to practice??

### Optimization

Necessary optimization: if the generated file is newer than the source file, don't do anything.

### Options file

Allow changing of input and output folder

- Name of author, blog, +

### Don't use a library for markdown conversion

Write a simple markdown interpreter. Probably support only a small subset of all markdown features.
