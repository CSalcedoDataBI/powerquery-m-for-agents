# Evals

Planned (spec §7): an A/B hallucination eval. Each question is answered twice by the same
model, once alone and once with the catalogue rows for its category. Every M library name
inside a code block (`Category.Name` or a `#` literal) is looked up in
`skills/m-reference/generated/catalog.json`; a name that is not there is an invention.
No model judges another: the count is a lookup.

Nothing lives here until the catalogue exists. An eval against an empty catalogue would count
every real function as invented.
