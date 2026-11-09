# LLM_learning — learning track

Purely educational project. The user is learning LLM fundamentals by working through the book
`data/fundamentos-de-llms.epub` ("Fundamentos de LLMs", Ensina Dev — 7 modules × 5 classes), after
having studied `apis-e-frameworks.epub` in the sibling `api_framework` project. The user's background
is data science / Python, so unlike that project there is no new language to learn here.

This book is conceptual, not an app to build class by class. Module 1 (what is a language model) and
module 2 class 1 (what is a token) were already read and understood before this repo started tracking
anything — no artifacts exist for them, and none should be backfilled. Tracking starts at module 2
class 2, where the book turns hands-on (tiktoken).

Not every class has a hands-on component — some stay pure reading (concepts with no code to run). Only
classes with code get an exercise file; every class still gets a `NOTES.md` and a quiz.

## Tooling

- `class_py/`: one shared venv (`python3 -m venv class_py/venv`), requirements.txt grows with what's
  needed so far. Claude sets up new dependencies directly (installing a library is plumbing, not the
  lesson) — unless a class's whole point is the setup itself.
- No paid LLM API key available: Claude Pro (claude.ai) is a chat subscription, not API credits — the
  Claude API is billed and set up separately, and the user hasn't done that. Default to free/local
  tooling: `tiktoken` for tokenization (module 2), local/open models (e.g. Ollama) if a later module
  needs a real generation call. Flag it and decide together before assuming a class needs a paid API.

## Layout

```
class_py/
├── venv/                      # gitignored
├── requirements.txt
└── module_N/class_K/
    ├── exercise.py            # only when the class has a hands-on component
    └── NOTES.md                # every class, hands-on or not
```

Run from the project root with the venv activated, e.g.:
`source class_py/venv/bin/activate && python class_py/module_2/class_2/exercise.py`.

## Workflow per class (one class at a time, never prepare ahead) — lighter touch

No strict no-edit review cycle and no per-class commit ritual here (unlike `api_framework`). More
casual, less process:

1. **Create the class folder.**
   - If the class has code: TODO skeleton with empty `TODO`s, no solution anywhere. Comments in
     English, with the book's Portuguese term in parentheses when a concept first appears, e.g.
     `tokenization (tokenização)`. Since the user already knows Python, keep syntax notes to genuinely
     new libraries/APIs (e.g. tiktoken), not language basics.
   - Point back to the book's module/class for the concept.
   - Include example commands to run/test as a block comment.
   - Also create `NOTES.md` with the template: What I learned / What confused me / Reflection.
   - If the class is pure reading (no code): just `NOTES.md`, same template minus anything code-specific.
2. **The user writes code; Claude can help directly** — point out bugs, explain, and edit the file
   when that's the fastest way to help, instead of only describing the fix. Still let the user do the
   TODOs themselves first when there's a TODO left to do; step in to fix/pair once they're stuck or ask.
3. **NOTES.md Q&A**: when the user writes a question under "What confused me", or their Reflection
   answer is missing/wrong, write the explanation directly inside `NOTES.md`, right under their
   question/answer, prefixed **Claude:** — so it stays part of their study notes.
4. **Quiz** (optional, nice-to-have): the chapter's "Quiz da aula" (answers in its "Gabarito"), via
   AskUserQuestion, max 4 questions per call, no recommended option, no hints, explain wrong answers
   after.
5. **Commit whenever it feels right** — no fixed one-commit-per-class rule; batching a few classes or
   committing mid-class is fine.

## Reading the book

Chapters are XHTML files inside the epub. Unlike `apis-e-frameworks.epub`, filenames aren't numbered —
match by module/topic slug (`toc.ncx` gives the reading order within a module if a slug is ambiguous):

```sh
unzip -Z1 data/fundamentos-de-llms.epub 'OEBPS/text/ch-modulo-2-*'                               # list module 2 chapters
unzip -p data/fundamentos-de-llms.epub \
  'OEBPS/text/ch-modulo-2-tokens-e-tokenizacao-tokenizacao-na-pratica.xhtml' \
  | sed -e 's/<\/p>/\n/g' -e 's/<\/pre>/\n/g' -e 's/<[^>]*>//g'                                  # read one as text
```

`data/` is gitignored (it holds the book).
