# =============================================================
# Module 2 · Class 2: Tokenization in practice (Tokenização na prática)
# =============================================================
#
# Carried forward from module 2 class 1 (what is a token) — nothing to carry
# forward in code, that class had no exercise.
#
# So far you've only estimated token counts by eye. Today: actually count
# them, the way real code does — every provider exposes its tokenizer (or a
# counting endpoint), and open libraries replicate it offline. In Python,
# tiktoken (OpenAI's library) is the standard for GPT-family encodings.
#
# RUN:
#   source class_py/venv/bin/activate
#   python class_py/module_2/class_2/exercise.py
# =============================================================

# TODO 1: import tiktoken (already in class_py/venv — see class_py/requirements.txt)
import tiktoken

# -------------------------------------------------------------
# STEP 1: get an encoding
# -------------------------------------------------------------
# tiktoken.get_encoding(name) returns an "encoding" object: .encode(text) turns
# text into a list[int] of token ids, .decode(token_ids) turns ids back into text.
# The book uses "o200k_base" — the encoding behind OpenAI's GPT-4o family.
#
# TODO 2: enc = tiktoken.get_encoding(...)
enc = tiktoken.get_encoding("o200k_base")

# -------------------------------------------------------------
# STEP 2: count tokens for the same sentence in two languages
# -------------------------------------------------------------
frase_en = "The quick brown fox jumps over the lazy dog"
frase_pt = "A rápida raposa marrom pula sobre o cachorro preguiçoso"

# TODO 3: print len(enc.encode(...)) for both frase_en and frase_pt.
# Expect PT to cost noticeably more tokens for the same meaning — this is the
# chapter's "language tax" (imposto do idioma): BPE merges are learned from
# training corpora dominated by English, so they favor what's frequent there.
print(len(enc.encode(frase_en)))  # ~9 tokens
print(len(enc.encode(frase_pt)))  # ~14 tokens: mais tokens para o mesmo sentido

# -------------------------------------------------------------
# STEP 3: peek at the pieces one word gets split into
# -------------------------------------------------------------
palavra = "despretensiosamente"

# TODO 4: encode `palavra`, then decode each resulting token id ONE AT A TIME
# (enc.decode([t]) for each t in the encoded list) and print the list of
# pieces. This shows a token is usually a sub-word fragment (a BPE merge),
# not a whole word.
print([enc.decode([t]) for t in enc.encode(palavra)])

# -------------------------------------------------------------
# STEP 4: a reusable counting helper
# -------------------------------------------------------------
# The chapter says token counting belongs in three places in real code:
#   - before sending a request (does it fit the context window? what will it cost?)
#   - after receiving a response (how much did the output cost?)
#   - when projecting monthly cost for a product
# You don't have an API key to actually send anything, but write the helper
# as if you would plug it in right before a request.
#
def count_tokens(text, encoding_name="o200k_base"):
    encoding = tiktoken.get_encoding(encoding_name)
    return len(encoding.encode(text))


# TODO 6: call count_tokens on a short prompt and on a longer paragraph (write
# your own text for both) and print the results.
prompt_curto = "Resuma esse texto em uma frase."
prompt_longo = (
    "Você é um assistente que ajuda desenvolvedores a entender tokenização. "
    "Explique, com exemplos práticos, por que o mesmo conteúdo em português "
    "costuma gastar mais tokens do que em inglês, e o que isso significa "
    "para o custo e para a janela de contexto de uma aplicação real."
)

print(count_tokens(prompt_curto))
print(count_tokens(prompt_longo))


# =============================================================
# TEST
# =============================================================
#   python class_py/module_2/class_2/exercise.py
#
# Expect to see printed:
#   - token counts for frase_en and frase_pt (PT higher)
#   - the decoded pieces of "despretensiosamente"
#   - count_tokens() results for your own short/long test strings
#
# REFLECT (answer in NOTES.md):
#   1. Your EN and PT counts for the same sentence — by how much (%) did PT
#      cost more? Does that roughly match the chapter's "20% to 50% more"?
#   2. "despretensiosamente" splits into pieces that aren't real words on
#      their own. Why does that matter for an "is my string within the
#      context window" check — could you just count characters or words
#      instead of calling encode()?
#   3. The chapter says to compare providers by tokenizing YOUR OWN corpus in
#      each one, not by comparing list price per million tokens. Why isn't
#      list price alone enough?
# =============================================================
