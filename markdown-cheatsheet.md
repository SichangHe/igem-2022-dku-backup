***Install the VSCode extension `markdownlint`
and set it as your default Markdown formatter.***

<!-- Do comments like this -->
Above is a comment. Comments are not rendered.

You can also use VSCode keyboard shortcut
(<kbd>command</kbd>+<kbd>/</kbd> on MacOS
and <kbd>control</kbd>+<kbd>/</kbd> on Windows)
to toggle comments.

Add empty lines above and below headers.

# title

## secondary header

###### sixth header

You can add *emphasize* text and **bold** in your plain text.
~~Strike through~~ is also supported.

To use inline code, use `put your exact code here`.
Code block that spans whole lines should be formatted like:

```python
print("this code block spans")
print("multiple lines")
```

with empty lines before and after.

Notice that text is rendered in the same paragraph
even if they are in different lines in the source code.
If you want to do a line break like this,\
you need to use `\` before the "enter."

If you want to have a new paragraph,
add an extra empty line.

Always press enter after typing some words to keep the lines short.
This way, it will look nice in Git when you apply changes
because Git tracks which lines change.

- Add unnumbered list items with a hyphen and a space before `-`.\
    indent the second line with four spaces to indicate
    that it is in the same item.
    Don't worry, it does not indent this much in the rendered output.\
    add empty lines before and after the unnumbered list.
    - Secondary unnumbered list should be indented as well
        - Theoretically, you can add more depth
            - if you ever want to
- To include code blocks, add empty lines before and after and indent:

    ```shell
    echo "this code block is in an unnumbered list"
    ```

- This is the last item of the unnumbered list.

1. Numbered list should always start with `1.`\
    no matter its actual index.
1. The second item will be automatically indexed as `2.`
1. The indentation rule for numbered list is the same as for unnumbered list.

<span style="color:blue">blue</span>

Inline math formulae like $\sum_ix_i$
should be wrapped with `$…$`.
Ordinary dollar signs need to be escaped as \$ 200

Wrap math formulae blocks that span whole lines with `$$…$$`:

$$
\sum_ix_i\\
\text{or even stuff like "align" in \LaTeX:}\\
\begin{align}
    f(x)&=\begin{cases}
        0&x<0\\
        x&x\geq0
    \end{cases}\\[12pt]
    t&=f(x)
\end{align}
$$

Use `\\` for new lines inside math blocks.

this|is
-|-
a|two-
line|table

align|to|the
|-|-:|:-:
left|right|center

![the text that shows when the render fails](path-of-the-picture "what you see when hovering over it")
<!-- it is broken because there is no picture in the path -->
